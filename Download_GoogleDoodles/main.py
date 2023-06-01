#網頁處裡
from urllib.request import urlopen,urlretrieve
#文字格式處理
import json
#檢查資料夾是否存在的內建資料庫
import os
#下載202X年
for years in range(4):
    for n in range(12):
        url="https://www.google.com/doodles/json/202"+str(years)+"/"+str(n+1)+"?hl=zh-TW"
        doodles = json.load(urlopen(url))
        for d in doodles:
            url = "https:" + d["url"]
            print(d["title"],url)
            #img_name = "doodles/" +url.split("/")[-1]
            dir_name1 = "doodles/"
            dir_name2 = dir_name1 +"/202"+str(years)+"年/"
            dir_name3 = dir_name2 +str(n+1)+"月/"

            #產生多重資料夾
            if not os.path.exists(dir_name1):
                os.mkdir(dir_name1)
            if not os.path.exists(dir_name2):
                os.mkdir(dir_name2)
            if not os.path.exists(dir_name3):
                os.mkdir(dir_name3)
            # #處裡圖片
            # response = urlopen(url)
            # img = response.read()
            # #創建資料夾
            # with open(img_name,mode="wb") as f:
            #     f.write(img)
            img_name = dir_name3 + url.split("/")[-1]
            #等同於上面的讀取網站到寫入、創建資料
            urlretrieve(url,img_name)
    