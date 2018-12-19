#!/usr/bin/python
# -*-coding:utf-8-*-

import pymysql as connection
from entity import Table
from entity import Column
from entity import DocxGenerator
from db2docx import Sql2Docx

__author__ = 'tony.chenjy'


class Mysql2Docx(Sql2Docx):

    def do(self, db_host, db_name, db_port=3306, db_user='root', db_pwd='root', file_name='数据字典', file_path='./'):
        print("jdbc_url=%s:%d/%s" % (db_host, db_port, db_name))
        print("db_user=%s" % db_user)
        print("db_pwd=%s" % db_pwd)
        print()

        self.db_name = db_name
        db = connection.connect(db_host, db_user, db_pwd, db_name, db_port, charset="utf8")
        tables = self.get_tables(db)
        for table in tables:
            table_name = table.name
            table.columns = self.get_columns(db, table_name)

        # generate docx
        DocxGenerator.generate_docx(file_path=file_path, file_name=file_name, tables=tables)

    # get tables from database connection
    def get_tables(self, db):
        sql = "SELECT TABLE_NAME, TABLE_COMMENT FROM INFORMATION_SCHEMA.TABLES " \
              "WHERE TABLE_SCHEMA = '%s' AND TABLE_TYPE = 'BASE TABLE'" % self.db_name
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        tables = list()
        for table in data:
            t = Table(table[0], self.get_comment(table[1]))
            tables.append(t)
        cursor.close()
        return tables

    # get columns from database connection and tables
    def get_columns(self, db, table_name):
        sql = "SELECT  " \
              "COLUMN_NAME 列名,  " \
              "COLUMN_TYPE 数据类型,  " \
              "IS_NULLABLE 是否为空,    " \
              "COLUMN_DEFAULT 默认值,    " \
              "COLUMN_COMMENT 备注   " \
              "FROM INFORMATION_SCHEMA.COLUMNS  " \
              "WHERE TABLE_SCHEMA ='%s' AND TABLE_NAME  = '%s';" % (self.db_name, table_name)
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        columns = list()
        for column in data:
            c = Column(column[0], column[1], self.is_nullable(column[2]), column[3], self.get_comment(column[4]))
            columns.append(c)
        cursor.close()
        return columns

    def is_nullable(self, flag):
        if flag == "YES":
            return ""
        else:
            return "NO"


if __name__ == '__main__':
    obj = Mysql2Docx('mysql2docx')
    print(obj)
    print(obj.db_name)
    obj.do(db_host='127.0.0.1', db_name='drklb', db_port=3307, db_user='root', db_pwd='root', file_name='数据字典_mysql',
           file_path='/')
