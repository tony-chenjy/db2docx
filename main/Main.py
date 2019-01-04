<<<<<<< HEAD
#!/usr/bin/python
# -*-coding:utf-8-*-

from pip._vendor.distlib.compat import raw_input
import logging

from db2docx import Sql2DocxSimpleFactory


def init_logger(logger):
    logger.setLevel(logging.DEBUG)

    # 创建 handler 输出到文件
    handler = logging.FileHandler("out.log", mode='w')
    handler.setLevel(logging.INFO)

    # handler 输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # 创建 logging format
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(ch)

    return logger


def tips_and_export():
    while True:
        print("choose to input 'mysql' or 'sqlServer' (eg. mysql, press enter to use mysql): ", end='')
        db_type = raw_input().strip()
        db_type = 'mysql' if db_type == '' else db_type
        db2docx = Sql2DocxSimpleFactory.produce(db_type=db_type)

        print("input ip address (eg. 127.0.0.1, press enter to use eg.): ", end='')
        db_host = raw_input().strip()
        db_host = '127.0.0.1' if db_host == '' else db_host

        print("input database name (eg. test, press enter to use eg.): ", end='')
        db_name = raw_input().strip()
        db_name = 'test' if db_name == '' else db_name

        if db_type == 'mysql':
            print("input port (eg. 3306, press enter to use eg.): ", end='')
        elif db_type == 'sqlServer':
            print("input port (eg. 1433, press enter to use eg.): ", end='')
        db_port = raw_input().strip()
        db_port = 3306 if db_port == '' else int(db_port)

        print("input user name (eg. root, press enter to use eg.): ", end='')
        db_user = raw_input().strip()
        db_user = 'root' if db_user == '' else db_user

        print("input password(eg. root, press enter to use eg.): ", end='')
        db_pwd = raw_input().strip()
        db_pwd = 'root' if db_pwd == '' else db_pwd

        print("input file name(eg. 数据字典, press enter to use eg.): ", end='')
        file_name = raw_input().strip()
        file_name = '数据字典' if file_name == '' else file_name

        print("input save path(eg. ./, press enter to use eg.): ", end='')
        file_path = raw_input().strip()
        file_path = './' if file_path == '' else file_path

        db2docx.do(db_host=db_host, db_name=db_name, db_port=db_port, db_user=db_user, db_pwd=db_pwd,
                   file_name=file_name,
                   file_path=file_path)
        # db2docx.export()

        print("press enter to continue...", end='')
        raw_input()
        print()


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    init_logger(logger)

    try:
        tips_and_export()
    except Exception as e:
        logger.error(msg=e, exc_info=True)
=======
#!/usr/bin/python
# -*-coding:utf-8-*-

from pip._vendor.distlib.compat import raw_input
import logging

from db2docx import Sql2DocxSimpleFactory


def init_logger(logger):
    logger.setLevel(logging.DEBUG)

    # 创建 handler 输出到文件
    handler = logging.FileHandler("out.log", mode='w')
    handler.setLevel(logging.INFO)

    # handler 输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.DEBUG)

    # 创建 logging format
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add the handlers to the logger
    logger.addHandler(handler)
    logger.addHandler(ch)

    return logger


def tips_and_export():
    while True:
        print("choose to input 'mysql' or 'sqlServer' (eg. mysql, press enter to use mysql): ", end='')
        db_type = raw_input().strip()
        db_type = 'mysql' if db_type == '' else db_type
        db2docx = Sql2DocxSimpleFactory.produce(db_type=db_type)

        print("input ip address (eg. 127.0.0.1, press enter to use eg.): ", end='')
        db_host = raw_input().strip()
        db_host = '127.0.0.1' if db_host == '' else db_host

        print("input database name (eg. test, press enter to use eg.): ", end='')
        db_name = raw_input().strip()
        db_name = 'test' if db_name == '' else db_name

        if db_type == 'mysql':
            print("input port (eg. 3306, press enter to use eg.): ", end='')
        elif db_type == 'sqlServer':
            print("input port (eg. 1433, press enter to use eg.): ", end='')
        db_port = raw_input().strip()
        db_port = 3306 if db_port == '' else int(db_port)

        print("input user name (eg. root, press enter to use eg.): ", end='')
        db_user = raw_input().strip()
        db_user = 'root' if db_user == '' else db_user

        print("input password(eg. root, press enter to use eg.): ", end='')
        db_pwd = raw_input().strip()
        db_pwd = 'root' if db_pwd == '' else db_pwd

        print("input file name(eg. 数据字典, press enter to use eg.): ", end='')
        file_name = raw_input().strip()
        file_name = '数据字典' if file_name == '' else file_name

        print("input save path(eg. ./, press enter to use eg.): ", end='')
        file_path = raw_input().strip()
        file_path = './' if file_path == '' else file_path

        db2docx.do(db_host=db_host, db_name=db_name, db_port=db_port, db_user=db_user, db_pwd=db_pwd,
                   file_name=file_name,
                   file_path=file_path)
        # db2docx.export()

        print("press enter to continue...", end='')
        raw_input()
        print()


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    init_logger(logger)

    try:
        tips_and_export()
    except Exception as e:
        logger.error(msg=e, exc_info=True)
>>>>>>> 1bf17071848bae1a6e563518c8bf3ba4807cb073
