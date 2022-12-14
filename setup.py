#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [ ]

test_requirements = ['pytest>=3', ]

setup(
    author="Eduardo Oliveira Menezes",
    author_email='eduardomenezes.dev@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="A Python package to access bucjet data from Google Cloud Storage",
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='google_bucket_fetcher',
    name='google_bucket_fetcher',
    packages=find_packages(include=['google_bucket_fetcher', 'google_bucket_fetcher.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/eduardo-menezes/google_bucket_fetcher',
    version='0.1.3',
    zip_safe=False,
)
