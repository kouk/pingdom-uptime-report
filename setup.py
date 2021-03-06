#!/usr/bin/env python
# -*- coding: utf-8 -*-
import setuptools

import versioneer

setuptools.setup(
    name="pingdom-uptime-report",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    url="https://github.com/kouk/pingdom-uptime-report",

    author="Konstantinos Koukopoulos",
    author_email="koukopoulos@gmail.com",

    description="Generate uptime reports using the Pingdom API.",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(where='src'),
    zip_safe=True,
    package_dir={"": "src"},

    install_requires=[
        'clize>=4.0.0',
        'PingdomLib>=2.0.0',
        'enum-compat>=0.0.2',
        'arrow>=0.10.0',
        'configobj>=5.0.6',
        'lazy-object-proxy>=1.3.1',
    ],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    license='MIT',
    entry_points={
        'console_scripts': [
            'uptimereport = uptime_report.cli:main',
        ]
    },
    extras_require={
        'gsheet': [
            'pygsheets',
        ]
    },
    keywords="pingdom uptime sla api"
)
