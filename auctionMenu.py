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
<title>競標品列表</title>
<style type="text/css">
body {width:600px; margin:10px auto;}
#content {background-color:DarkOliveGreen; margin:20px; padding:20px; border:2px solid ivory; font-size: 14pt; color:#ff9; line-height:28px}
a {color: yellow}
</style>
</head>
<body>
<div id="content">
""")

records = ctrl.getAuctionList()
for (id,name,price,uName,expireTime) in records:
	print(f"<p>ID:{id} 名稱:{name} 目前價格:{price} 目前得標者：{uName} </p> <p>競標到期時間：{expireTime}</p>")


print("<p><a href='bidding.html'> 我要競標 </a></p>")

print("<p><a href='addNewGood.html'> 我要拍賣 </a></p>")

print("<p><a href='userId.html'> 個人資料</a></p>")

print("<p><a href='addUser.html'> 新增用戶</a></p>")


print("</body></html>")



