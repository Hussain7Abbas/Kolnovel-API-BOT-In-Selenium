from click import getchar
from seleniumscript import *
from htmlRender import *

def inputNovelName():
    message = '\n    ========== Novels ==========\n'
    novels = getNovelsNames()
    for i in range(len(novels)):
        message += '    %s   %s\n' %(i, novels[i])
    print(message)
    
    return novels[int(input("Enter Novel Number: "))]

def inputChapterNumeber():
    message = '\n    ========== Chapters ==========\n'
    chapters = getNovelChapters(novel_name)
    for chapter in chapters:
        message += '    %s' %(chapter)
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
        # ====== Download Novel Chapters ======
        params = ['kolnovel']
        if (input('is novel exist? y/n:') == 'y'):
            novel = inputNovelName()
        else:
            novel = input("Enter Novel Name: ")
        
        params.append(novel)
        chapter_start = int(input("Enter Novel Start Chapter: "))
        chapter_end = int(input("Enter Novel Start Chapter: "))
        params.append((chapter_start, chapter_end+1))
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