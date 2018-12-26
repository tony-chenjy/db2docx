# db2docx forked from Mysql2docx
[CM / db2docx](https://gitee.com/chenjunyu/Mysql2docx) & [yu578707139/db2docx](https://github.com/yu578707139/db2docx) is forked from [icecooly / Mysql2docx](https://gitee.com/icecooly/Mysql2docx)

    what to used for:
        used to generate data_dictionary.docx from database comments, with self-defined styles
    
    develop environment:
        python3.7
    
    required packages: 
        python-docx, pymysql, cx_Oracle, pymssql, chardet

#### step1: install db2docx  
    (windows cmd) /Mysql2docx > python setup.py install
![step1](https://gitee.com/chenjunyu/Mysql2docx/attach_files/download?i=195880&u=http%3A%2F%2Ffiles.git.oschina.net%2Fgroup1%2FM00%2F06%2F10%2FPaAvDFwi-FeAXfnnAAAn_rb5nmU186.PNG%3Ftoken%3Dad549b229bb7c7d333d5a868debe0ea9%26ts%3D1545795712%26attname%3Dstep1.PNG "在这里输入图片标题")

#### step2: run Main.py
    (windows cmd) /Mysql2docx/main > python Main.py



#### step3: input database information and generate data_dictionary.docx happily.
   
#### more ways: generate data_dictionary.docx originally
#### part1: Mysql2Docx 
    how to use (python command)
    >>> from db2docx import Mysql2Docx
    >>> m=Mysql2Docx()
    >>> m.export()
    [output] call method do(db_host, db_name, db_port, db_user='root', db_pwd='root', file_name='数据字典', file_path='./')
    >>> m.do(db_host='127.0.0.1', db_name='database_name', db_port=3306, db_user='root', db_pwd='root', file_name='数据字典', file_path='./')

#### part2: SqlServer2Docx 
    how to use (python command)
    >>> from db2docx import SqlServer2Docx
    >>> m=SqlServer2Docx()
    >>> m.export()
    [output] call method do(db_host, db_name, db_port, db_user='root', db_pwd='root', file_name='数据字典', file_path='./')
    >>> m.do(db_host='127.0.0.1', db_name='database_name', db_port=1433, db_user='root', db_pwd='root', file_name='数据字典', file_path='./')

#### part3: Oracle2Docx 
    (to be continued...)

#### part4: export example
![export example](https://gitee.com/chenjunyu/Mysql2docx/attach_files/download?i=193628&u=http%3A%2F%2Ffiles.git.oschina.net%2Fgroup1%2FM00%2F05%2FF8%2FPaAvDFwZ7MaAYnaNAAAxuZWEu6Y223.PNG%3Ftoken%3D6065ac12dfaae701cac3fe9315028ecc%26ts%3D1545203075%26attname%3Ddata_dictionary.PNG "export example")
