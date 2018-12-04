from db2docx import Mysql2Docx
from db2docx import Oracle2Docx

m = Mysql2Docx()
m.do(db_host='127.0.0.1', db_name='drklb', db_port=3307, db_user='root', db_pwd='root', file_name='数据字典_mysql')

o = Oracle2Docx()
o.do(db_host='192.168.0.71', db_name='drklb', db_port=3307, db_user='root', db_pwd='root', file_name='数据字典_oracle')
