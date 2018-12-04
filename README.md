# db2docx forked from Mysql2docx


#### part1: Mysql2docx_cm 
    generate data_dictionary.docx from mysql comments, with self-defined styles
    根据mysql注释生成数据字典（带自定义样式）

- required packages
> PyMySQL、python-docx

- how to use (python command)
> from Mysql2docx_cm import Mysql2docx_cm
> 
> m=Mysql2docx_cm()
> 
> m.export()
> 
    expect output（export tips 输出导出提示）:call method do(db_host, db_name, db_port=3306, db_user='root', db_pwd='root', file_name='数据字典')
> m.do(db_host='127.0.0.1', db_name='database_name', db_port=3306, db_user='root', db_pwd='root', file_name='数据字典')
> 
    file_name.docx（default：数据字典.docx）


#### part2: Oracle2docx_cm (to be continued...)

#### 截图
![](https://gitee.com/icecooly/Mysql2docx/attach_files/download?i=92257&u=http%3A%2F%2Ffiles.git.oschina.net%2Fgroup1%2FM00%2F01%2FC2%2FPaAvDFmfDX2AbSPhAAH-JDNEN-o933.png%3Ftoken%3D314a024565ec3e8df4ec6964413aacba%26ts%3D1503595901%26attname%3Dlizi.png)


