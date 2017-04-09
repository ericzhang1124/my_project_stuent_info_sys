# !C:/Python/Python27/python.exe
# coding:UTF8

import sys
import MySQLdb as mydb

import cgi

print "ContentType:html/text\n"
print "<html>"
print "<head>"
print '<meta charset="utf-8">'
print "</head>"
print "<body>"

form = cgi.FieldStorage()

userInfo =  []

username = form.getvalue("username")
password = form.getvalue("password")
age = form.getvalue("age")
phone = form.getvalue("phone")
address = form.getvalue("address")
sex = form.getvalue("sex")
stu_id = form.getvalue("stu_id")

userInfo.append(stu_id)
userInfo.append(username)
userInfo.append(password)
userInfo.append(sex)
userInfo.append(phone)
userInfo.append(address)
userInfo.append(age)


if None in userInfo:
	print '<p>Please input all info in the form!</p>'
	print '<a href="http://127.0.0.1:8080/my_project_stuent_info_sys/signup.html">GoBack</a>'
	print "</body>"
	print "</html>"
	sys.eixt()


conn =  mydb.connect(db='testdb', host='127.0.0.1', user='root')
curs = conn.cursor()

sql_find = 'select * from student where username="%s"' % username

curs.execute(sql_find)
row = curs.fetchall()
if len(row) != 0: # 用户已经注册过了，根据username判断
	print '<p>This User already signup!</p>'
	print '<a href="http://127.0.0.1:8080/my_project_stuent_info_sys/signup.html">GoBack</a>'
	print "</body>"
	print "</html>"
	sys.eixt()


sql_insert = 'insert into student values (default, "%s", "%s", "%s", "%s", "%s", "%s", "%s")'  % (userInfo[0], userInfo[1], userInfo[2], userInfo[3], userInfo[4], userInfo[5], userInfo[6])
curs.execute(sql_insert)
conn.commit()

curs.execute(sql_find)
row = curs.fetchall()
if len(row) != 0: # 插入成功后如果根据username能够查询到该用户信息即确认信息注册成功
	print '<p>Sign Up Success!</p>'
	print '<a href="http://127.0.0.1:8080/my_project_stuent_info_sys/">Go To Login</a>'
	print "</body>"
	print "</html>"


