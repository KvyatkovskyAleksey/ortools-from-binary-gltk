# Build or-tools 9.12 with GLPK linked, for Python 3.12.
#
# Uses PyPA's manylinux_2_28_x86_64 image (glibc 2.28). Resulting binaries are
# forward-compatible with AWS Lambda Python 3.12 runtime (Amazon Linux 2023,
# glibc 2.34) and any Linux ≥ glibc 2.28.
#
# This image already ships:
#   - gcc 14, g++ 14 (more than enough for C++20)
#   - cmake 4.3 (>=3.24 required)
#   - swig 4.4
#   - Python 3.6–3.13 in /opt/python/cp3XX-cp3XX/
#
# Switched from public.ecr.aws/lambda/python:3.12 (network was unreliable from
# this build host).
#
# Usage:
#   docker build -t ortools-py312-build -f build.Dockerfile .
#   docker create --name ortools-extract ortools-py312-build
#   docker cp ortools-extract:/work/or-tools/build/python/dist/. /tmp/ortools-py312-wheel/
#   docker rm ortools-extract

FROM quay.io/pypa/manylinux_2_28_x86_64:latest

ENV PYBIN=/opt/python/cp312-cp312/bin
ENV PATH=$PYBIN:/root/.local/bin:$PATH

# Sanity: verify toolchain
RUN cmake --version && gcc --version | head -1 && python3.12 --version && swig -version | head -2

# Python build deps for the wheel target.
# - mypy provides `stubgen` which or-tools' python.cmake requires.
# - mypy-protobuf provides `protoc-gen-mypy` which protoc invokes during
#   --mypy_out generation of *_pb2.pyi stubs. If pip auto-installs it during
#   cmake configure, it lands in /root/.local/bin (not on PATH inside `protoc`'s
#   subprocess env) and the build fails. Installing it here puts it in
#   /opt/python/cp312-cp312/bin which IS on PATH.
# - virtualenv is also needed by or-tools cmake (it tries to install it
#   anyway); pre-installing avoids slow PyPI throttling during configure.
RUN python3.12 -m pip install --upgrade pip setuptools wheel build mypy mypy-protobuf virtualenv

WORKDIR /work
RUN git clone --branch v9.12 --depth 1 https://github.com/google/or-tools.git
WORKDIR /work/or-tools

# CMake configure: GLPK on, Python on, build all third-party deps.
# BUILD_DEPS=ON forces BUILD_GLPK=ON when USE_GLPK=ON.
# Force cp312 by pointing CMake at the manylinux Python.
RUN cmake -S. -Bbuild \
        -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_CXX_STANDARD=20 \
        -DBUILD_DEPS=ON \
        -DUSE_GLPK=ON \
        -DBUILD_PYTHON=ON \
        -DPython3_EXECUTABLE=/opt/python/cp312-cp312/bin/python3.12 \
        -Dstubgen_EXECUTABLE=/opt/python/cp312-cp312/bin/stubgen

# Build python_package target. Heavy build — abseil, protobuf, glpk, scip, cbc,
# clp, glop, sat, etc. all from source.
RUN cmake --build build --target python_package -v -j$(nproc)

# or-tools' python.cmake bundles Cbc/Clp/abseil into the wheel's ortools/.libs/
# but does NOT bundle libGLPK (and in some cases libhighs). Use auditwheel to
# detect needed external libs and copy them into ortools.libs/ inside the wheel,
# upgrading the platform tag from raw `linux_x86_64` to manylinux_2_28.
RUN mkdir -p /work/or-tools/build/python/dist-repaired && \
    LD_LIBRARY_PATH=/work/or-tools/build/lib64 auditwheel repair \
        --plat manylinux_2_28_x86_64 \
        -w /work/or-tools/build/python/dist-repaired \
        /work/or-tools/build/python/dist/ortools-*.whl

# Sanity check: install + GLPK smoke test in a clean venv
RUN python3.12 -m venv /tmp/verify && \
    /tmp/verify/bin/pip install /work/or-tools/build/python/dist-repaired/ortools-*.whl && \
    /tmp/verify/bin/python -c "from ortools.linear_solver import pywraplp; s = pywraplp.Solver('t', pywraplp.Solver.GLPK_MIXED_INTEGER_PROGRAMMING); print('GLPK in wheel OK:', s.SolverVersion())"

# Final wheel location: /work/or-tools/build/python/dist-repaired/ortools-*.whl
CMD ["ls", "-la", "/work/or-tools/build/python/dist-repaired/"]
