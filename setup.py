from sys import executable
from os.path import join as pjoin
from os.path import dirname

setuptools_import_error_message = """setuptools is not installed for """ + executable + """
Please follow this link for installing instructions :
https://pypi.python.org/pypi/setuptools
make sure you use \"""" + executable + """\" during the installation"""

try:
    from setuptools import find_packages, setup
    from setuptools.dist import Distribution
    from setuptools.command.install import install
except ImportError:
    raise ImportError(setuptools_import_error_message)


class BinaryDistribution(Distribution):
    def is_pure(self):
        return False

    def has_ext_modules(self):
        return True


class InstallPlatlib(install):
    def finalize_options(self):
        install.finalize_options(self)
        self.install_lib = self.install_platlib


# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(pjoin(dirname(__file__), fname)).read()


setup(
    name='ortools',
    version='9.8.3309',
    packages=find_packages(),
    python_requires='>= 3.8',
    install_requires=[
        'absl-py >= 2.0.0',
        'numpy >= 1.13.3',
        'pandas >= 2.0.0',
        'protobuf >= 4.25.0',
    ],
    package_data={
        'ortools':['.libs/*','../libortools.so.9'],
        'ortools.init.python':['init.cpython-39-x86_64-linux-gnu.so', '*.pyi'],
        'ortools.algorithms.python':['knapsack_solver.cpython-39-x86_64-linux-gnu.so', '*.pyi'],
        'ortools.bop':['*.pyi'],
        'ortools.glop':['*.pyi'],
        'ortools.graph.python':[
            'linear_sum_assignment.cpython-39-x86_64-linux-gnu.so',
            'max_flow.cpython-39-x86_64-linux-gnu.so',
            'min_cost_flow.cpython-39-x86_64-linux-gnu.so',
            '*.pyi'],
        'ortools.constraint_solver':['_pywrapcp.so', '*.pyi'],
        'ortools.linear_solver':['_pywraplp.so', '*.pyi'],
        'ortools.linear_solver.python':['model_builder_helper.cpython-39-x86_64-linux-gnu.so', '*.pyi'],
        'ortools.packing':['*.pyi'],
        'ortools.pdlp':['*.pyi'],
        'ortools.pdlp.python':['pdlp.cpython-39-x86_64-linux-gnu.so', '*.pyi'],
        'ortools.sat':['*.pyi'],
        'ortools.sat.colab':['*.pyi'],
        'ortools.sat.python':['swig_helper.cpython-39-x86_64-linux-gnu.so', '*.pyi'],
        'ortools.scheduling.python':['rcpsp.cpython-39-x86_64-linux-gnu.so', '*.pyi'],
        'ortools.util.python':['sorted_interval_list.cpython-39-x86_64-linux-gnu.so', '*.pyi'],
    },
    include_package_data=True,
    license='Apache 2.0',
    author='Google LLC',
    author_email='or-tools@google.com',
    description='Google OR-Tools python libraries and modules',
    long_description=read('README.txt'),
    keywords=('operations research' + ', constraint programming' +
              ', linear programming' + ', flow algorithms' + ', python'),
    url='https://developers.google.com/optimization/',
    download_url='https://github.com/google/or-tools/releases',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: Unix',
        'Operating System :: POSIX :: Linux',
        'Operating System :: POSIX :: BSD :: FreeBSD',
        'Operating System :: MacOS',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: C++',
        'Programming Language :: Python :: Implementation :: CPython',
        'Topic :: Office/Business :: Scheduling',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    distclass=BinaryDistribution,
    cmdclass={'install': InstallPlatlib},
)
