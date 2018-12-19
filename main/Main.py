from db2docx import Mysql2Docx
from db2docx import Oracle2Docx
from db2docx import SqlServer2Docx

# m = Mysql2Docx()
# m.do(db_host='127.0.0.1', db_name='drklb', db_port=3307, db_user='root', db_pwd='root', file_name='数据字典_mysql',
#      file_path='/')

# o = Oracle2Docx()
# o.do(db_host='192.168.0.71', db_name='drklb', db_port=3307, db_user='root', db_pwd='root', file_name='数据字典_oracle')

# m = SqlServer2Docx()
# m.do(db_host='192.168.0.66', db_name='jtms', db_port=1433, db_user='sa', db_pwd='root',
#      file_name='数据字典_sqlServer', file_path='/')

ms = SqlServer2Docx()
ms.do(db_host='192.168.0.74', db_name='jtms', db_port=1433, db_user='sa', db_pwd='root',
     file_name='东莞市交投集团办公自动化系统数据字典', file_path='/')
