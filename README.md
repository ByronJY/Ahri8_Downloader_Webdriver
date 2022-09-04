###### Ahri8_Downloader_Webdriver
# 松鼠症倉庫下載器

[影片說明](https://youtu.be/tLdMTop1fyA)

## 前置作業
該程式會用到 **Selenium** 函式庫，需要額外安裝
##### Python 3 使用 pip 安裝
`python3 -m pip install selenium`

該程式還需要使用 **ChromeDriver** ，所以裝置上必須先有 Google Chrome

[然後下載與裝置上 Chrome 同版本之 ChromeDriver](https://chromedriver.chromium.org/)

將 ChromeDriver 與本程式置於同一路徑下

## 使用
輸入「**漫畫編號**」即可，輸入任意 **負數** 結束程式

可使用 **空格** 將多個參數隔開，程式會依序執行

例如輸入 `48723 27774 -1` 程式會下載完 48723、27774 後結束

###### 會在此 py 檔執行的路徑產生一個「**Downloads**」資料夾，並在其內生成「**漫畫編號**」之資料夾，下載的圖片會在此資料夾中
