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
	# there may be more elements you don't want, such as "style", etc.
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

ch, out = epub2text('1_5225_1.epub')


#converting into a single string
stringList = ' '.join([str(item) for item in out ]).lower()


#count word in a string
# define string
"""substring = input("Enter the word: ")
count = stringList.count(substring.lower())"""
# print count
print(ch)


##book = epub.read_epub('1_5225_1.epub')
#for image in book.get_items_of_type(ebooklib.ITEM_IMAGE):
 #   print (image)*/
