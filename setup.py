# -*- encoding: UTF-8 -*-

from setuptools import setup, find_packages

"""
See https://gitee.com/icecooly/Mysql2docx
See https://gitee.com/chenjunyu/Mysql2docx
"""

VERSION = '1.0'

DESCRIPTION = (
    'generate data_dictionary.docx from database comments, with self-defined styles'
)

setup(
    name='db2docx',
    version=VERSION,
    description="generate data_dictionary.docx from database comments, with self-defined styles",
    long_description=DESCRIPTION,
    classifiers=[],
    keywords='',
    include_package_data=True,
    author='tony.chenjy',
    author_email='tony.chenjy@foxmail.com',
    url='https://gitee.com/chenjunyu/Mysql2docx',
    license='MIT',
    packages=find_packages(),
    install_requires=['python-docx', 'pymysql', 'cx_Oracle', 'pymssql', 'chardet'],
    extras_require={}
)
