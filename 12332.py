import xlrd
import pymysql.cursors
import os



connection = pymysql.connect(host='127.0.0.1',
                                user='root',
                                password='snikers48',
                                db='maxim',
                                charset='utf8mb4',
                                cursorclass=pymysql.cursors.DictCursor)

print ("connect successful!!")

for f in os.listdir("C:/Users/wolk1612/Desktop/123/"):
    f1 = "C:/Users/wolk1612/Desktop/123/" + f
    data = xlrd.open_workbook(f1)
    sheet = data.sheet_by_index(0)

    feature = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    what = ['Identity Number', 'Date of Birth', 'Gender', 'Marital Status', 'Education', 'Children', 'Income',
            'Date appointed', 'Housing',
            'House ownership', 'Employed By']
    stroka = sheet.nrows
    stolbec = sheet.ncols

    for i in range(stroka):
        for j in range(stolbec):
            for k in range(11):
                if sheet.cell(i, j).value == what[k]:
                    feature[k] = sheet.cell(i + 1, j).value







    with connection.cursor() as cursor:

        # SQL
        sql = "insert into nasty(id,birth,gender,mrtstatus, educ, children,income, dateapp, housing, howner, empl) VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (feature[0], feature[1], feature[2], feature[3], feature[4], feature[5], feature[6], feature[7],feature[8], feature[9], feature[10]))

        sql3 = "commit"
        cursor.execute(sql3)

sql2 = "select id from nasty"
cursor.execute(sql2)

connection.close()

