#!/usr/bin/python
# -*-coding:utf-8-*-

from db2docx import Mysql2Docx
from db2docx import SqlServer2Docx


class Sql2DocxSimpleFactory:

    # produce Sql2Docx
    @staticmethod
    def produce(db_type):
        if db_type == 'mysql':
            db = Mysql2Docx()
        elif db_type == 'sqlServer':
            db = SqlServer2Docx()
        else:
            db = Mysql2Docx()
        return db
