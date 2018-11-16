# Mysql2docx_cm forked from Mysql2docx
生成mysql数据字典文档（带样式）

## install（安装）[需要python3.0以上]
```shell/cmd
进入项目目录（setup.py同级目录）
python setup.py install
```

## how to use（使用）
```python
>>> from Mysql2docx_cm import Mysql2docx_cm
>>> m=Mysql2docx_cm()
>>> m.export()
# expect output（export tips 输出导出提示）:call method do(db_host, db_name, db_port=3306, db_user='root', db_pwd='root', file_name='数据字典')
>>> m.do(db_host='127.0.0.1', db_name='database_name', db_port=3306, db_user='root', db_pwd='root', file_name='数据字典')
```
如果参数正确会成功生成>>file_name.docx（默认：数据字典.docx）

## 截图
![](https://gitee.com/icecooly/Mysql2docx/attach_files/download?i=92257&u=http%3A%2F%2Ffiles.git.oschina.net%2Fgroup1%2FM00%2F01%2FC2%2FPaAvDFmfDX2AbSPhAAH-JDNEN-o933.png%3Ftoken%3D314a024565ec3e8df4ec6964413aacba%26ts%3D1503595901%26attname%3Dlizi.png)
