#使用 Seleium 模擬"人為操控" Chrome driver 暴力爬蟲(也有其他瀏覽器ex.safari、firefox...)
#下載Seleium cmd pip install selenium
#安裝chromedriver 並放到同資料夾
from selenium.webdriver import Chrome
#引用by函式
from selenium.webdriver.common.by import By
#載入內建暫停模組
import time
#下載、導入pytube，方便下載YOUTUBE影片
import pytube
#生成資料夾的函式
import os

#選擇並開啟Chrome
driver = Chrome()
#playlist網址
driver.get("https://www.youtube.com/playlist?list=PLOGFNwZXhpfr0Ju7tw7uCj1aG0YBdwSUz")
#程式休息1s
time.sleep(1)
#尋找網址內 ID = "video-title"
list = driver.find_elements(By.ID,"video-title")

for vid in list:
    #從網址尋找href屬性，並回傳
    url = vid.get_attribute("href")
    if vid.text =="":
        continue
    print(url)
    #不分類下載，會載到低畫質得
    #pytube.YouTube(url).streams.first().download()

    #生成資料夾/檔案希望的位置
    dirname = "Use_selenium_Download_utube/youtube0602/"
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    try :
        yt = pytube.YouTube(url)
    #依照resolution排序並下載，download裡面放下載地址
        (yt.streams
        .filter(progressive=True, file_extension='mp4')
        .order_by('resolution')
        .desc()
        .first()
        .download(dirname))
        print(vid.text,"---下載成功")
    except :
        print(vid.text,"---下載失敗")

#關閉瀏覽器   
driver.close()