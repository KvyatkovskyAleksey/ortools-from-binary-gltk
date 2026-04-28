"""
ortools-from-binary-glpk: pre-built or-tools 9.12 wheel-equivalent with GLPK linked.

Branch `lambda-py312`: built for Python 3.12 against manylinux_2_28_x86_64
(glibc 2.28; runs on AWS Lambda Python 3.12 runtime, AL2023 glibc 2.34, and any
Linux >= glibc 2.28).

Built via the `build.Dockerfile` at the repo root using
`quay.io/pypa/manylinux_2_28_x86_64`. The wheel is repaired with auditwheel,
which bundles libGLPK.so.5.0 and a few abseil libs into ortools/.libs/.

Usage from a downstream project's requirements.txt:

    git+https://github.com/KvyatkovskyAleksey/ortools-from-binary-gltk.git@lambda-py312

For the original cp39 build, use the `lambda` branch.
"""
from os.path import dirname, join as pjoin

from setuptools import find_packages, setup
from setuptools.command.install import install
from setuptools.dist import Distribution


class BinaryDistribution(Distribution):
    """Marks this as a non-pure (binary) distribution so the platform tag is set."""

    def is_pure(self):
        return False

    def has_ext_modules(self):
        return True


class InstallPlatlib(install):
    """Force install into the platform-specific lib dir (where binary extensions go)."""

    def finalize_options(self):
        install.finalize_options(self)
        self.install_lib = self.install_platlib


def read(fname):
    return open(pjoin(dirname(__file__), fname)).read()


setup(
    name='ortools',
    version='9.12.9999',
    packages=find_packages(),
    python_requires='>=3.12',
    install_requires=[
        'absl-py>=2.0.0',
        'numpy>=1.13.3',
        'pandas>=2.0.0',
        'protobuf<5.30,>=5.29.3',
        'immutabledict>=3.0.0',
    ],
    package_data={
        # Catch-all: every package gets its compiled extensions, type stubs, and
        # Python sources bundled. This avoids per-module hardcoded filenames so
        # future minor or-tools bumps "just work" without touching setup.py.
        '': ['*.so', '*.so.*', '*.pyi'],
        # Bundled shared libraries (Cbc/Clp/Osi/Abseil/GLPK/...). The .so files
        # in ortools/ have RPATH `$ORIGIN/../../ortools/.libs` so they find
        # these at runtime.
        'ortools': ['.libs/*'],
    },
    include_package_data=True,
    license='Apache 2.0',
    author='Google LLC',
    author_email='or-tools@google.com',
    description='Google OR-Tools python libraries and modules (custom build with GLPK linked)',
    long_description=read('README.txt'),
    keywords=(
        'operations research, constraint programming, linear programming,'
        ' flow algorithms, python, glpk'
    ),
    url='https://developers.google.com/optimization/',
    download_url='https://github.com/google/or-tools/releases',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: C++',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    distclass=BinaryDistribution,
    cmdclass={'install': InstallPlatlib},
)
