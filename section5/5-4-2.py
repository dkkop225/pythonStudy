import pymysql

#MySQL Connection
conn = pymysql.connect(host='localhost',user = 'dkk',password='1111',
                        db='python_app1',charset='utf8')


try:
    with conn.cursor(pymysql.cursors.DictCursor) as c:  #conn.cursor(pymysql.cursors.DictCursor) 딕셔너리 형태#
        c.execute("SELECT * FROM users")
        #1개로우
        #print(c.fetchone())
        #선택지정
        #print(c.fetchmany(3))
        #전체로우
        #print(c.fetchall())

        #순회1
        c.execute("SELECT * FROM users ORDER BY id ASC")
        rows = c.fetchall()
        for row in rows:
            print('usage1 >', row)

        #순회2
        c.execute("SELECT * FROM users ORDER BY id DESC")
        for row in rows:
            print('usage2 >', row)

        #조건조희
        param1 = (1,)
        c.execute("SELECT * FROM users WHERE id=%s",param1)
        print('param1',c.fetchall())

        #조건조희2
        param2 = 1
        c.execute("SELECT * FROM users WHERE id='%d'" %param1)
        print('param2',c.fetchall())


        #조건조희2
        param3 = (4,5)
        c.execute("SELECT * FROM users WHERE id IN('%d','%d')" % (4,5))
        print('param3',c.fetchall())
finally:
    conn.close();
