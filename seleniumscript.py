

# ## ════════════════════╣  SECTION Main Program  ╠════════════════════ ##

def downloadNovels(website: str, name: str, startUrl: str, chapters: int):
    if (website == 'kolnovel'):  # =============== Kolnovels Website ===============
        from . import kolnovel
        kolnovel.downloadChapters(name, startUrl, chapters)
    elif (website == 'novel4up'):
        from . import novel4up
        novel4up.downloadChapters(name, startUrl, chapters)
    elif (website == 'arnovel'):
        from . import arnovel
        arnovel.downloadChapters(name, startUrl, chapters)

#    ════════════════════╣ !SECTION Main Program  ╠════════════════════ ##


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
