import io
import os
import re
from setuptools import setup, find_packages


def read(*names, **kwargs):
    with io.open(
        os.path.join(os.path.dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8")
    ) as fp:
        return fp.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


long_description = read('README.md', mode='rt')

setup(
    name='cosmic_ray_parallel',
    version=find_version('cosmic_ray_parallel/version.py'),
    packages=find_packages(exclude=['contrib', 'docs', 'test*']),

    author='Franz Haas',
    description='Pytest test-runner plugin for Cosmic Ray',
    license='MIT',
    keywords='testing',
    url='https://github.com/franzhaas/cosmic_ray_parallel',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Testing',
    ],
    platforms='any',
    include_package_data=True,
    entry_points={
         'cosmic_ray.execution_engines': [
            'cosmic_ray_parallel = cosmic_ray_parallel.engine:cosmic_ray_parallel_engine',],
    },
    long_description=long_description,
)
