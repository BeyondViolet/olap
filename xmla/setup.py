#-*- coding:utf-8 -*-

from setuptools import setup

long_description = open("README.md").read()

install_requires=[
    'olap >= 0.3',
    'zeep',
    'requests',
    'lxml',
    'httpx[http2]'
    ]

setup(
    name='bv_xmla',
    version='0.8.0',
    url="https://github.com/BeyondViolet/bv_xmla",
    license='Apache Software License 2.0',
    classifiers = [
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules"
        ],
    description='Access olap data sources through xmla',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Norman Krämer, Alexey Gornostaev',
    author_email='kreopt@gmail.com',
    packages=['bv_xmla'],
    package_dir={'bv_xmla':'bv_xmla'},
    install_requires=install_requires,
    tests_require = [
        'nose',
        'requests_mock',
    ],

    test_suite = 'nose.collector',

    include_package_data=True,
    zip_safe=False,
)
