#!/usr/bin/python
# -*-coding:utf-8-*-

import json

__author__ = 'tony.chenjy'


class Sql2Docx(object):

    # constructor
    def __init__(self, name=''):
        self.db_name = name

    # print method call tips
    @staticmethod
    def export():
        print("call method do(db_host, db_name, db_port=3306, db_user='root', db_pwd='root', file_name='数据字典')")

    def do(self, db_host, db_name, db_port=3306, db_user='root', db_pwd='root', file_name='数据字典'):
        pass

    # get tables from database connection
    def get_tables(self, db):
        pass

    # get columns from database connection and tables
    def get_columns(self, db, table_name):
        pass

    # get comment from table comment attribute
    @staticmethod
    def get_comment(comment):
        if comment is None:
            return ""
        try:
            data = json.loads(comment)
            return data[0]['value']
        except:
            return comment


if __name__ == '__main__':
    obj = Sql2Docx('sql2docx')
    print(obj)
    print(obj.db_name)
