#!C:\Users\tommy\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import control as ctrl
#連線DB
from dbConfig import conn, cur
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>範例1</title>
</head>
<body>
""")

#查詢


form = cgi.FieldStorage()
uid=form.getvalue('uid') 
id=form.getvalue('id') 
bidding=form.getvalue('bidding')
ctrl.bidding(uid,id,bidding)
ctrl.addAuctionInfo(uid,id,bidding)

print("競標成功!")
print("<br><a href='auctionMenu.py'>回首頁</a>")
print("</body></html>")