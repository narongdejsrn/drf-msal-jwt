#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import re
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def get_version(*file_paths):
    """Retrieves the version from drf_msal_jwt/__init__.py"""
    filename = os.path.join(os.path.dirname(__file__), *file_paths)
    version_file = open(filename).read()
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


version = get_version("drf_msal_jwt", "__init__.py")


if sys.argv[-1] == 'publish':
    try:
        import wheel
        print("Wheel version: ", wheel.__version__)
    except ImportError:
        print('Wheel library missing. Please run "pip install wheel"')
        sys.exit()
    os.system('python setup.py sdist bdist_wheel')
    os.system('twine upload dist/*')
    sys.exit()

if sys.argv[-1] == 'tag':
    print("Tagging the version on git:")
    os.system("git tag -a %s -m 'version %s'" % (version, version))
    os.system("git push --tags")
    sys.exit()

readme = open('README.rst').read()

setup(
    name='drf-msal-jwt',
    version=version,
    description="""Connect Django Rest Framework with MSAL and JWT""",
    long_description=readme,
    author='Narongdej Sarnsuwan',
    author_email='narongdej@sarnsuwan.com',
    url='https://github.com/narongdejsrn/drf-msal-jwt',
    packages=[
        'drf_msal_jwt',
    ],
    include_package_data=True,
    install_requires=[
        'msal>=1.1.0',
        'requests>=2.23.0'
    ],
    license="MIT",
    zip_safe=False,
    keywords='drf-msal-jwt',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Django :: 2.1',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3'
    ],
)
