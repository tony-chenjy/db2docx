# db2docx



## Description

using the database table information and comment to generate a data dictionary.

> A **[data dictionary](https://en.wikipedia.org/wiki/Data_dictionary)**, or [metadata repository](https://en.wikipedia.org/wiki/Metadata_repository), as defined in the *IBM Dictionary of Computing*, is a "centralized repository of information about data such as meaning, relationships to other data, origin, usage, and format".[[1\]](https://en.wikipedia.org/wiki/Data_dictionary#cite_note-1) *Oracle* defines it as a collection of tables with metadata.



## Environment & Tools

Python 3.7, python-docx, pymysql, cx_Oracle, pymssql, chardet, 



## Support

Mysql, Sqlserver, 



## Guide

### clone project to local

```
git clone https://github.com/tony-chenjy/db2docx.git
```



### install using python

```
python setup.py install
```

![step1](https://ws4.sinaimg.cn/large/006tKfTcgy1g0gdyfgclmj30r90fzweh.jpg)



### run the application & input database information

```
python Main.py
```

![step2-1](https://ws4.sinaimg.cn/large/006tKfTcgy1g0gdyt3uuqj30ra0fxt99.jpg)

![step2-2](https://ws4.sinaimg.cn/large/006tKfTcgy1g0gdzot610j30r80g0dg3.jpg)



### result

![data_dictionary](https://ws1.sinaimg.cn/large/006tKfTcgy1g0gdohoakrj30gr080dfw.jpg)



## Reference

[icecooly / Mysql2docx](https://gitee.com/icecooly/Mysql2docx)