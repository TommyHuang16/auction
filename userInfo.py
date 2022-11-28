#!C:\Users\tommy\AppData\Local\Programs\Python\Python310\python.exe
# -*- coding: utf-8 -*-
# 處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import control as ctrl
#連線DB
from dbConfig import conn, cur

print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>個人資訊</title>
<style type="text/css">
body {width:600px; margin:10px auto;}
#content {background-color:DarkOliveGreen; margin:20px; padding:20px; border:2px solid ivory; font-size: 14pt; color:#ff9; line-height:28px}
a {color: yellow}
</style>
</head>
<body>
<div id="content">
""")

form = cgi.FieldStorage()
uid=form.getvalue('uid')


records = ctrl.getUserInfo(uid)
for (uid,uName) in records:
	print(f"<p>User ID:{uid} 名稱:{uName}")

print("<p>歷史紀錄：</p>")
records = ctrl.getHistoryInfo(uid)
for (id,price) in records:
	print(f"<p>商品ID:{id} 競標價格:{price}")

print("<p><a href='auctionMenu.py'> 回首頁</a></p>")



print("</body></html>")



