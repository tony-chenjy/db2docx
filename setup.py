#-*- encoding: UTF-8 -*-
from setuptools import setup, find_packages
import sys, os
from os import path
import Mysql2docx

"""
See https://github.com/icecooly/Mysql2docx
"""

VERSION = '1.0.0'

with open('README.md') as f:
    long_description = f.read()

setup(
        name='Mysql2docx', 
        version=VERSION, 
        description="mysql自动生成数据库设计文档",
        long_description=long_description, # 放README.md文件,方便在Pypi页展示
        classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        keywords='自动数据库设计文档', # 关键字
        author='skydu', # 用户名
        author_email='icecooly.du@qq.com', 
        url='https://github.com/icecooly/Mysql2docx',
        license='MIT',
        packages=find_packages(),
        install_requires=['python-docx'],
        extras_require={}
)
