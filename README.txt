ortools-from-binary-glpk
========================

Custom build of Google OR-Tools with GLPK linked, distributed as a pip-
installable package. Upstream or-tools wheels on PyPI dropped GLPK around
9.7+; this fork rebuilds from source with `-DUSE_GLPK=ON` and bundles
libGLPK.so.5.0 into the wheel via auditwheel.

Branches
--------
- `lambda-py312`: or-tools 9.12, Python 3.12, manylinux_2_28_x86_64.
  Runs on AWS Lambda Python 3.12 runtime (AL2023 glibc 2.34) and any
  Linux >= glibc 2.28.
- `lambda`: legacy or-tools 9.8, Python 3.9. Kept for rollback only.

Usage
-----
In a downstream project's requirements.txt:

    git+https://github.com/KvyatkovskyAleksey/ortools-from-binary-gltk.git@lambda-py312

Or in pyproject.toml (poetry):

    ortools = { git = "https://github.com/KvyatkovskyAleksey/ortools-from-binary-gltk.git", rev = "lambda-py312" }

Rebuilding
----------
See `build.Dockerfile` at the repo root. Build steps:

    docker build -t ortools-py312-build -f build.Dockerfile .
    docker create --name ortools-extract ortools-py312-build
    docker cp ortools-extract:/work/or-tools/build/python/dist-repaired/. /tmp/wheel/
    docker rm ortools-extract

The Dockerfile clones or-tools v9.12, configures cmake with GLPK on,
builds the python_package target, and runs auditwheel repair to bundle
libGLPK and abseil into ortools/.libs/. A smoke test instantiates the
GLPK solver in a clean venv at the end of the build.

Solvers included
----------------
CP-SAT, Glop, MPSolver/ModelBuilder wrappers around CBC, CLP, GLPK, SCIP,
plus vehicle routing and graph algorithm libraries. GLPK is the addition
over upstream PyPI builds.

License
-------
Apache 2.0 (or-tools itself). GLPK is GPLv3 — bundling it makes the
combined wheel GPLv3 effectively. Do not redistribute publicly.
