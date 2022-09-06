
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


def _locate_element(driver, by: By, value: str, wait: int = 20):
    return WebDriverWait(driver, wait).until(EC.presence_of_element_located((by, value)))


def _locate_elements(driver, by: By, value: str, wait: int = 20):
    return WebDriverWait(driver, wait).until(EC.presence_of_all_elements_located((by, value)))


options = Options()
options.page_load_strategy = 'eager'

# from webdriver_manager.chrome import ChromeDriverManager
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def downloadChapters(name: str, startUrl: str, chapters: int):
    chapterNo = 0
    driver = webdriver.Chrome(service=Service("/home/hussain7abbas/Projects/selenium_chrome/Kol Novel API/drivers/chromedriver"), options=options)
    err = []
    print('\n********* Fetching Chapters ... *********')
    for i in range(chapters):
        # try:

            driver.get(startUrl)
            print('got it')

            chapterNo = _locate_element(driver, By.ID, 'chapter-heading').get_attribute('innerHTML')
            chapterNo = int(chapterNo.replace('-', ' ').strip().split(' ')[-1])

            print(chapterNo)

            startUrl = _locate_element(driver, By.XPATH, "//div[@class='nav-next ']/a").get_attribute('href')

            print(startUrl)

            body = _locate_element( driver, By.XPATH, "//div[@class='reading-content']").get_attribute('innerHTML')

            print('** Chapter ', chapterNo, ' Fetched')
            saveNovel(name, chapterNo, str(body).replace('"', '\''))
            buildChapter(name, chapterNo, str(body).replace('"', '\''))
        # except:
        #     err.append(chapterNo)

    if (err != []):
        print('\n\n\nError with Loading Chapters: ')
        for i in err:
            print(i, end=' ')
        print()
    else:
        print('\n********* Fetching Done Successfully *********')

    driver.quit()


# ## ════════════════════╣  SECTION Test Area  ╠════════════════════ ##
# ─── NOTE test webdriver ────────────────
# downloadChapters('your-talent-is-mine', 'https://novel4up.com/novel/i-copy-talents/12/', 50)


# ─── NOTE test webdriver ────────────────

# driver = webdriver.Chrome(service=Service(
#     "./drivers/chromedriver"), options=options)

# driver.get('https://kolnovel.com/desolate-era-103635/')

#    ════════════════════╣ !SECTION Test Area  ╠════════════════════ ##
