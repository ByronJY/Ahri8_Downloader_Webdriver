import time
import os
import platform
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# Download ChromeDriver: https://chromedriver.chromium.org/


# 判斷作業系統，切換分隔符
def check_platform():
    SLASH = "/"
    if platform.system() == "Windows":
        SLASH = '\\'
    elif platform.system() == "Linux":
        SLASH = "/"
    elif platform.system() == "Darwin":
        SLASH = "/"
    else:
        print("本程式可能不支援你的作業系統")

    return SLASH

# 檢查「Downloads」路徑是否存在，若不存在則建立
def check_dir(dir, SLASH):
    try:
        os.mkdir(dir + SLASH +"Downloads")
    except FileExistsError:
        pass

# 截圖 (下載)
def download_pic(img_src, path, driver):
    strScript = 'window.open("' + img_src + '");'
    driver.execute_script(strScript)
    driver.switch_to.window(driver.window_handles[1])

    time.sleep(2)
    driver.find_element(By.TAG_NAME, "img").screenshot(path + ".png")
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

def toInt(i):
    try:
        return int(i)
    except:
        return 0


###############################           主程式           ###############################
def main():

    options = Options() 
    options.add_argument('--headless')  # 啟動Headless 無頭
    options.add_argument('--disable-gpu') #關閉GPU 避免某些系統或是網頁出錯
    options.add_argument('disable-infobars')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('window-size=3000x3000')
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_experimental_option("prefs", {"profile.password_manager_enabled": False, "credentials_enable_service": False})


    SLASH = check_platform()
    #NOW_DIR = os.path.abspath(os.getcwd())
    NOW_DIR = os.path.dirname(os.path.realpath(__file__))
    DIR = NOW_DIR + SLASH + "Downloads" + SLASH
    check_dir(NOW_DIR, SLASH) # 檢查「Downloads」路徑是否存在

    while(True):
        # manga_id = "84679" # 39 頁
        manga_id_list = list(map(toInt, input("輸入漫畫編號: ").split()))

        print("")
        
        for manga_id in manga_id_list:

            # print("漫畫佇列: " + manga_id_list + '\n')

            if manga_id < 0:
                exit()
            elif manga_id == 0:
                print("漫畫編號格式有誤！（略過）\n")
            else:
                print("【" + str(manga_id) + "】")
        
                current_page = 1

                try:
                    print(DIR + str(manga_id))
                    os.mkdir(DIR + str(manga_id))
                except FileExistsError:
                    print("存在相同檔案！\n")
                    continue
                    # pass


                driver = webdriver.Chrome(chrome_options=options)
                driver.set_window_size(3000, 3000)
                

                next_page = True
                total_imgs = 0

                while(next_page):
                    # print("Current page: " + str(current_page))

                    driver.get("https://ahri8.top/readOnline2.php?ID=" + str(manga_id) + "&host_id=1&page=" + str(current_page) + "&gallery_brightness=100&gallery_contrast=100")
                    driver.execute_script("window.scrollBy(0, document.body.scrollHeight);")
                    time.sleep(2)

                    for img_id in range(1, 11):

                        src = driver.find_element(By.XPATH, "//div[@id=\"read_online_image_" + str(img_id) + "\"]//*").get_attribute("src")
                        if src == "":
                            next_page = False
                            break

                        elif src == None:
                            # print("10th")
                            src = driver.find_element(By.XPATH, "//div[@id=\"read_online_image_" + str(img_id) + "\"]/a//*").get_attribute("src")
                            if src == "":
                                next_page = False
                                break
                        
                        print(f"第{total_imgs:>3} 頁 " + src)

                        
                        pic_path = DIR + str(manga_id) + SLASH + str(total_imgs)
                        # 呼叫下載圖片
                        download_pic(src, pic_path, driver)

                        total_imgs += 1


                    current_page += 1

                print("結束！ 【" + str(manga_id) + "】共 " + str(total_imgs) + " 頁\n")
                

                # WAIT_FOR_INPUT = input()


if __name__ == "__main__":
    main()