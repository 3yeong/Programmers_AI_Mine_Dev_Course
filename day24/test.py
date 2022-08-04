import pymysql

conn = pymysql.connect(host='localhost', user='root',db='mysql', password='130526',  charset='utf8')
cursor = conn.cursor()

sql = '''CREATE TABLE WEAPON ( 
id int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY, 
name varchar(255), 
stock int(10) 
) 
'''

cursor.execute(sql)

conn.commit()
conn.close()