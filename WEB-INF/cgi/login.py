#!C:/Python/Python27/python.exe
# -*- coding:UTF-8 -*-

import sys
import MySQLdb as mydb
import cgi

print "ContentType:html/text\n"
print "<html>"
print "<head>"
print "</head>"
print "<body>"


form = cgi.FieldStorage()

username = form.getvalue("username")
password = form.getvalue("password")


if username == None or password == None: # 参数为空校验
	print '<p>Please input username and password</p>'
	print '<a href="http://127.0.0.1:8080/my_project_stuent_info_sys/">GoBack</a>'
	print "</body>"
	print "</html>"
	sys.eixt()

conn =  mydb.connect(db='testdb', host='127.0.0.1', user='root')
# print '<p>connect success</p>'
# print "</body>"
# print "</html>"
cur = conn.cursor()
sql_find = 'select * from student where username="%s"' % username
cur.execute(sql_find)
row = cur.fetchall()
if len(row) == 0: # 用户名未查到
	print '<p>Can\'t Find Your Infomation.Please Signup First!</p>'
	print '<a href="http://127.0.0.1:8080/my_project_stuent_info_sys/">GoBack</a>'
	print "</body>"
	print "</html>"
	sys.eixt()

if len(row) > 0: # 密码错误
		if password != row[0][3]:
			print '<p>Have A Wrong Password!</p>'
			print '<a href="http://127.0.0.1:8080/my_project_stuent_info_sys/">GoBack</a>'
			print "</body>"
			print "</html>"
			sys.eixt()
		else:
			print '<p>Login Success!</p>'
			print '''
			<h3>UserInfo</h3>
			<br>
			<p>UserID:%s</p><br>
			<p>UserName:%s</p><br>
			<p>UserSex:%s</p><br>
			<p>UserPhone:%s</p><br>
			<p>UserAddress:%s</p><br>
			</body>
			</html>			
			''' % (row[0][1], row[0][2], row[0][4], row[0][5], row[0][6])