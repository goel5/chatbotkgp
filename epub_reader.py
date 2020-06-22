import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup


def epub2thtml(epub_path):
    book = epub.read_epub(epub_path)
    chapters = []
    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            chapters.append(item.get_content())
    return chapters


blacklist = [
	'[document]',
	'noscript',
	'header',
	'html',
	'meta',
	'head', 
	'input',
	'script',
	
]
def chap2text(chap):
    output = ''
    soup = BeautifulSoup(chap, 'html.parser')
    text = soup.find_all(text=True)
    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    return output

def thtml2ttext(thtml):
    Output = []
    for html in thtml:
        text =  chap2text(html)
        Output.append(text)
    return Output

def epub2text(epub_path):
    chapters = epub2thtml(epub_path)
    ttext = thtml2ttext(chapters)
    return chapters,ttext

#getting html output file
ch, out = epub2text('1_5225_1.epub')
out=out[2]
f=open("out.html", "w")
f.write(str(ch[2])) #observed ch[2] was returning full chapter in out.html
f.close()

#make a list of all the paragraphs in the chapter
u= [line for line in out.split('\n') if line.strip() != '']

#removing escape characters between paragraphs and getting new output
new_out = '\n'.join([str(item) for item in u ])
f=open("new_out.html", "w",encoding="utf-8")
f.write(str(new_out)) #observed ch[2] was returning full chapter in out.html
f.close()

#taking input from user
word = input("Enter the word: ")
#count word in a string
""""count = stringList.count(substring.lower())"""



#Returning list of paragraph containig the word asked by user
final_out = list(x.lower() for x in u)
final_out = list(i.strip() for i in final_out)#removing spaces at begining and end
import re
def searchWordinSentence(word,final_out):
    pattern = re.compile(word)
    if re.search(pattern,final_out):
        return True
para=list((t for t in final_out if searchWordinSentence(word,t)))


##book = epub.read_epub('1_5225_1.epub')
#for image in book.get_items_of_type(ebooklib.ITEM_IMAGE):
 # print (image)
