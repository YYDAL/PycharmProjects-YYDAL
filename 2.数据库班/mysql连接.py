import pymysql
pymysql_config = {
    'user': 'root',
    'password': 'qwe123',
    'db': 'hhh',
    'charset': 'utf8'
}

conn = pymysql.Connect(**pymysql_config)    #连接数据库
cur = conn.cursor()                          #启用游标

cur.execute('select * from student')       #执行命令

cur.close()                                #关闭游标
conn.close()                               #关闭数据库


