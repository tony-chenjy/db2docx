from Mysql2docx import Mysql2docx
from Mysql2docx_cm import Mysql2docx_cm

# m = Mysql2docx()
m = Mysql2docx_cm()
m.do(db_host='127.0.0.1', db_name='drklb', db_port=3306, db_user='root', db_pwd='root', file_name='深圳市大数据研究院数据字典')
