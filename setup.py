#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

setup(
    name='pyquickjoin',
    version='0.1.0',
    description="Quickly join two unsorted files",
    long_description=readme + '\n\n' + history,
    author="Steven Willis",
    author_email='onlynone@gmail.com',
    url='https://github.com/onlynone/pyquickjoin',
    packages=[
        'quickjoin',
    ],
    package_dir={'quickjoin':
                 'quickjoin'},
    entry_points={
        'console_scripts': [
            'quickjoin = quickjoin.main:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='quickjoin',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
)
