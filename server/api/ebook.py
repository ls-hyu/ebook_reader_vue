#from app import app
import ebooklib
from ebooklib import epub
from html.parser import HTMLParser
#from gtts import gTTS
import pyttsx3

def read():
    class MyHTMLParser(HTMLParser):
        def handle_starttag(self, tag, attrs):
            #print("Encountered a start tag:", tag)
            pass

        def handle_endtag(self, tag):
            #print("Encountered an end tag :", tag)
            pass

        def handle_data(self, data):
            #print("Encountered some data  :", data)
            print(data)
            engine.say(data)
            engine.runAndWait()

    engine = pyttsx3.init()
    en_voice_id = "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0"
    engine.setProperty('voice', en_voice_id)

    parser = MyHTMLParser()
    #parser.feed('<html><head><title>Test</title></head>'
    #            '<body><h1>Parse me!</h1></body></html>')

    book = epub.read_epub('test.epub')

    page = 0
    for doc in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
        page += 1
        if page < 2:
            continue
        print(doc)
        print("_________________________")
        print(parser.feed(doc.get_body_content().decode()))
        #for line in str(doc.get_body_content()):
        #    print(str(line))
        print("")
        if page == 2:
            break