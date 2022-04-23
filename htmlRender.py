import webbrowser
import os
import Novels_backend

def buildChapter(name:str, chapter:int, body):
    html = ''
    with open('kolnovels/index.html', 'r+') as kol_Template:
        html = kol_Template.read().format(name=name, chapter=chapter, body=body)

    if not os.path.exists('kolnovels/%s/chapters/'%(name)):
        os.makedirs('kolnovels/%s/chapters/'%(name))
    with open('kolnovels/%s/chapters/%s.html'%(name, chapter), 'w+') as kol_Chapter:
        kol_Chapter.write(html)

def openChapter(name:str, chapter:int):
    buildChapter(name, chapter, Novels_backend.getChapter(name, chapter))
    webbrowser.open('kolnovels/%s/chapters/%s.html'%(name,chapter))
    