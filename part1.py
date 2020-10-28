#AnnTran
import codecs
import re
import string

#INITIATE
readFile=codecs.open('Henry V Entire Play.html',"rb")
readFile=readFile.read()
readFile=str(readFile)
writeFile = open('HenryV.txt','w')
acts = dict()

#REMOVE HTTP TAG
def striphtml(data):
    p = re.compile(r'\<[^>]+\>', re.I)
    return p.sub('', data)


text = striphtml(readFile)
text = text.replace('\\n','\n')
text = text.replace('\\','')

#DIFFERENT PART
#r'(\bACT\s?[A-Z]\b)'
def act(data):
    p = re.compile(r'(\bACT\s?[A-Z]\b)',re.DOTALL)
    return p.sub("==ACT \1==", data)
def scene(data):
    p = re.compile(r'(\bSCENE\s?[A-Z]\b)',re.DOTALL)
    return p.sub("=SCENE \1=", data)
def direct(data):
    p = re.compile('Exit',re.I)
    return p.sub('[Exit]', data)
def enter(data):
    p = re.compile('Enter',re.I)
    return p.sub('[Enter]',data)

text = act(text)
text = scene(text)
text = direct(text)
text = enter(text)
print(text)
writeFile.write(text)
writeFile.close()

    

