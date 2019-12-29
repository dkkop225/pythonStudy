import urllib.request as req
import simplejson as json
import os.path

#url

url = "https://api.github.com/repositories"

#경로,파일명
savename = '/Users/dkkim/Documents/section4/reop.json'

if not os.path.exists(url):
    req.urlretrieve(url,savename)

items = json.load(open(savename, 'r',encoding="utf-8"))
#item = json.loads(open(savename, 'r',encoding="utf-8").read())

#출력
for item in items:
    print(item["full_name"]+"-"+item["owner"]["url"])
