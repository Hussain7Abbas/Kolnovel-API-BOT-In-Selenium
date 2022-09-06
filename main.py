from seleniumscript import *
from htmlRender import *
from Novels_backend import *

sites = ['kolnovel', 'novel4up', 'arnovel']


def inputSiteName():
    message = '\n    ========== Sites ==========\n'
    for i in range(len(sites)):
        message += '    %s   %s\n' % (i, sites[i])
    print(message)

    return sites[int(input("Enter Site Number: "))]


def inputNovelName():
    message = '\n    ========== Novels ==========\n'
    novels = getNovelsNames()
    for i in range(len(novels)):
        message += '    %s   %s\n' % (i, novels[i])
    print(message)

    return novels[int(input("Enter Novel Number: "))]


def inputChapterNumeber():
    message = '\n    ========== Chapters ==========\n'
    chapters = getNovelChapters(novel_name)
    for chapter in chapters:
        message += '    %s' % (chapter)
    print(message)

    return input("Enter Chapter Number: ")


while True:
    print('''
    ========== Actions ==========
    1   Download Novel Chapters
    2   Open Novel
    3   Rebuild Novel

    Type any key to quit ...
    ''')
    action = input("Enter Action Number: ")

    if action == '1':
        params = []
        # ====== Download Novel Chapters ======
        params.append(inputSiteName())

        if (input('is novel exist? y/n:') == 'y'):
            novel = inputNovelName()
        else:
            novel = input("Enter Novel Name: ")

        params.append(novel)
        chapter_start_url = input("Enter Novel Start Chapter URL: ")
        params.append(chapter_start_url)
        chapter_end = int(
            input("How many chapters would you want to download?: "))
        params.append(chapter_end)
        downloadNovels(*params)
    elif action == '2':
        # ====== Open Novel ======
        novel_name = inputNovelName()
        chapter_no = inputChapterNumeber()
        openChapter(novel_name, chapter_no)
    elif action == '3':
        # ====== Open Novel ======
        novel_name = inputNovelName()
        chapters = getNovelChapters(novel_name)
        print('\n********* Rebuilding Chapters ... *********')
        for chapter in chapters:
            buildChapter(novel_name, chapter, getChapter(novel_name, chapter))
            print('** Chapter ', chapter, ' Rebuilt')
        print('\n********* Rebuild Done Successfully *********')
    else:
        break
