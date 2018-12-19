#!/usr/bin/python
# -*-coding:utf-8-*-

import pymssql as connection
from entity import Table
from entity import Column
from entity import DocxGenerator
from db2docx import Sql2Docx
import chardet

__author__ = 'tony.chenjy'


class SqlServer2Docx(Sql2Docx):

    def do(self, db_host, db_name, db_port=1433, db_user='root', db_pwd='root', file_name='数据字典', file_path='./'):
        print("jdbc_url=%s:%d/%s" % (db_host, db_port, db_name))
        print("db_user=%s" % db_user)
        print("db_pwd=%s" % db_pwd)
        print()

        self.db_name = db_name
        db = connection.connect(server=db_host, user=db_user, password=db_pwd, database=db_name, charset="utf8")
        tables = self.get_tables(db)
        for table in tables:
            table_name = table.name
            table.columns = self.get_columns(db, table_name)

        # generate docx
        DocxGenerator.generate_docx(file_path=file_path, file_name=file_name, tables=tables)

    # get tables from database connection
    def get_tables(self, db):
        # sql = "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES " \
        #       "WHERE TABLE_CATALOG = '%s' AND TABLE_TYPE = 'BASE TABLE'" % self.db_name

        sql = "SELECT OBJ.NAME, EXT.VALUE FROM " \
              "(SELECT NAME, ID FROM SYSOBJECTS WHERE XTYPE='U') OBJ " \
              "LEFT JOIN " \
              "(SELECT MAJOR_ID AS ID, VALUE FROM SYS.EXTENDED_PROPERTIES WHERE MINOR_ID=0) EXT " \
              "ON OBJ.ID=EXT.ID " \
              "ORDER BY OBJ.NAME; "
        cursor = db.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()

        tables = list()
        for table in data:
            t = Table(table[0], self.get_comment(self.byte_to_str(table[1])))
            if t.name == 'sysdiagrams':
                continue
            tables.append(t)
        return tables

    # get columns from database connection and tables
    def get_columns(self, db, table_name):
        # sql = "SELECT  " \
        #       "COLUMN_NAME 列名,  " \
        #       "COLUMN_TYPE 数据类型,  " \
        #       "IS_NULLABLE 是否为空,    " \
        #       "COLUMN_DEFAULT 默认值,    " \
        #       "COLUMN_COMMENT 备注   " \
        #       "FROM INFORMATION_SCHEMA.COLUMNS  " \
        #       "WHERE TABLE_SCHEMA ='%s' AND TABLE_NAME  = '%s';" % (self.db_name, table_name)

        cursor = db.cursor()
        sql = "SELECT TOP 1 ID FROM SYSOBJECTS WHERE XTYPE='U' AND NAME='%s'" % (table_name)
        cursor.execute(sql)
        table_ids = cursor.fetchall()
        table_id = table_ids[0][0]

        sql = "SELECT COL.NAME, TYPE.NAME AS TYPENAME, COL.ISNULLABLE, COL.CDEFAULT, EXT.VALUE FROM (SELECT NAME, CDEFAULT, ISNULLABLE, COLID, XTYPE FROM SYSCOLUMNS WHERE ID='%s') COL " \
              "LEFT JOIN " \
              "(SELECT * FROM SYSTYPES WHERE NAME!='sysname') TYPE " \
              "ON COL.XTYPE=TYPE.XTYPE " \
              "LEFT JOIN " \
              "(SELECT MINOR_ID, VALUE FROM SYS.EXTENDED_PROPERTIES WHERE CLASS_DESC='OBJECT_OR_COLUMN' AND MINOR_ID>0 AND MAJOR_ID='%s') EXT " \
              "ON EXT.MINOR_ID=COL.COLID " \
              "ORDER BY COL.COLID ASC;" % (table_id, table_id)
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()

        columns = list()
        for column in data:
            c = Column(column[0], column[1], self.is_nullable(column[2]), self.get_default_value(column[3]),
                       self.get_comment(self.byte_to_str(column[4])))
            columns.append(c)
        return columns

    def byte_to_str(self, comment):
        if comment is None:
            return ""

        if chardet.detect(comment).get('encoding') == 'utf-8':
            result = comment.decode("utf-8")
        elif chardet.detect(comment).get('encoding') == 'ascii':
            result = comment.decode('ascii')
        else:
            result = ""
        return result

    def is_nullable(self, flag):
        if flag:
            return ""
        else:
            return "NO"

    def get_default_value(self, flag):
        if flag:
            return str(flag)
        else:
            return None


if __name__ == '__main__':
    obj = SqlServer2Docx('sqlServer2docx')
    print(obj)
    print(obj.db_name)
    obj.do(db_host='192.168.0.74', db_name='jtms', db_port=1433, db_user='sa', db_pwd='root',
           file_name='数据字典_sqlServer', file_path='/')
