import pymysql.cursors
db = pymysql.connect(host='localhost',
                     user='root',
                     password='admin2',
                     database='neelu',
                     cursorclass=pymysql.cursors.DictCursor)
with db.cursor() as cursor:
    sql = "SELECT * FROM student"
    cursor.execute(sql)
    result = cursor.fetchone()
    print(result)