#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


setup(
    name='jenkins-job-builder-pipeline',
    version='0.1.0',
    description="Pipeline support for jenkins-job-builder",
    author="https://github.com/rusty-dev",
    url='https://github.com/rusty-dev/jenkins-job-builder-pipeline',
    packages=['jjb_pipeline'],
    include_package_data=True,
    install_requires=[],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ],
    entry_points={
        'jenkins_jobs.projects': [
            'pipeline=jjb_pipeline.project_pipeline:Pipeline',
        ],
        'jenkins_jobs.modules': [
            'pipeline=jjb_pipeline.definition:Pipeline',
        ],
    },
)
