import pymysql.cursors
db = pymysql.connect(host='localhost',
                     user='root',
                     password='admin2',
                     database='neelu',
                     cursorclass=pymysql.cursors.DictCursor)
cursor=db.cursor()
query= 'update student set fname= "pallavi" where age=23'
try:
     cursor.execute(query)
     db.commit()
except:
     db.rollback()

db.close()