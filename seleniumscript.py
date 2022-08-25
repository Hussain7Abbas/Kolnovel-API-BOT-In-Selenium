from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from Novels_backend import *
from htmlRender import *


def _locate_element(driver, by: By, value: str, wait: int = 10):
    return WebDriverWait(driver, wait).until(EC.presence_of_element_located((by, value)))


def _locate_elements(driver, by: By, value: str, wait: int = 10):
    return WebDriverWait(driver, wait).until(EC.presence_of_all_elements_located((by, value)))


options = Options()
options.page_load_strategy = 'eager'


def downloadNovels(website: str, name: str, startUrl: str, chapters: int):
    chapterNo = 0
    driver = webdriver.Chrome(service=Service(
        "./drivers/chromedriver"), options=options)
    if (website == 'kolnovel'):  # =============== Kolnovels Website ===============
        err = []
        print('\n********* Fetching Chapters ... *********')
        for i in range(chapters):
            try:

                driver.get(startUrl)

                # ─── NOTE pass robot check ────────────────
                if driver.find_element_by_id('recaptcha_for_all_button'):
                    robotButton = _locate_element(
                        driver, By.ID, "recaptcha_for_all_button")

                    print(robotButton.get_attribute('innerHTML'))
                    robotButton.click()
                    sleep(3)

                # ─── NOTE Wait for page Load after robot check ────────────────
                while(not driver.find_element_by_class_name('entry-title')):
                    sleep(1)

                chapterNo = _locate_element(
                    driver, By.XPATH, "//h1[@class='entry-title']").get_attribute('innerHTML')
                chapterNo = int(chapterNo.replace('-', ' ').split(' ')[-1])

                startUrl = _locate_element(
                    driver, By.XPATH, "//div[@class='nvs']/a").get_attribute('href')

                print(startUrl)

                body = _locate_element(
                    driver, By.XPATH, "//div[@class='epwrapper']")

                driver.execute_script("""
                var childNodesToRemove =document.getElementsByClassName("code-block");
                for(var i=childNodesToRemove.length-1;i >= 0;i--){
                    var childNode = childNodesToRemove[i];
                    childNode.parentNode.removeChild(childNode);
                }

                var childNodesToRemove1 =document.getElementsByClassName("navimedia");
                for(var j=childNodesToRemove1.length-1;j >= 0;j--){
                    var childNode1 = childNodesToRemove1[j];
                    childNode1.parentNode.removeChild(childNode1);
                }

                """, body)

                print('** Chapter ', chapterNo, ' Fetched')
                saveNovel(name, chapterNo, str(body.get_attribute('innerHTML')).replace(
                    '<p>&nbsp;</p>', '').replace('"', '\''))
                buildChapter(name, chapterNo, str(body.get_attribute('innerHTML')).replace(
                    '<p>&nbsp;</p>', '').replace('"', '\''))
            except:
                err.append(chapterNo)

        if (err != []):
            print('\n\n\nError with Loading Chapters: ')
            for i in err:
                print(i, end=' ')
            print()
        else:
            print('\n********* Fetching Done Successfully *********')

        driver.quit()


# downloadNovels('kolnovel', 'deslate-era',
#                'https://kolnovel.com/desolate-era-103635/', 10)

# ## ════════════════════╣  SECTION Test Area  ╠════════════════════ ##

driver = webdriver.Chrome(service=Service(
    "./drivers/chromedriver"), options=options)

driver.get('https://kolnovel.com/desolate-era-103635/')

#    ════════════════════╣ !SECTION Test Area  ╠════════════════════ ##


# # try:
# #     messages=[]
# #     for i in range(10):
# #         driver.get("https://rewayat.club/novel/the-lord-is-empire/"+str(i))
# #         messages.append(driver.title)
# #         body = [t.text for t in _locate_elements(By.XPATH,"//div[@class='v-card__text unselectable pre-formatted font-cairo text-right font-weight-medium opacity-high']")]
# #         messages.extend(body)
# # finally:
# #     telegram_send.send(messages=body)
# #     driver.quit()
