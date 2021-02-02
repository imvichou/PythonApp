#抓取 Medium.com 的文章資料
import urllib.request as req

url = "http://medium.com/_/api/home-feed"

#建立一個Requset物件，附加Requset headers的資訊
request=req.Request(
    url,
    headers={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.88 Safari/537.36"}
    )

with req.urlopen(request) as response:
    data=response.read().decode("utf-8") #回傳資料格式為json

#解析json格式的資料，取得每篇文章的標題
import json
data=data.replace("])}while(1);</x>","")
data=json.loads(data)

#取得json資料中的文章標題
posts=data["payload"]["references"]["Post"]
for key in posts:
    post=posts[key]
    print(post["title"])