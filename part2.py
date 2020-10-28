#ANN TRAN
import re
import csv
import datetime
from datetime import date

#Initiate
writeFile = open('part2.txt','w',encoding='utf8')
ageList = []
hList = []
wList = []
BMIL = []
IDL = []
#clean date
def date(data):
    #p = re.compile("(\d{1,2})\s?-?/?\|?\\\?\s?(\d{1,2})\s?-?/?\|?\\\?\s?(\d\d\d\d)")
    p = re.compile("(\d{1,2})\s?\W?[\\\]?\s?(\d{1,2})\s?\W?[\\\]?\s?(\d\d\d\d)")
    p = p.sub(r"\3-\1-\2",data)
    return p

#clean weight
def weight(data):
    #p = re.compile("(\d{1,3})\W?#s?|lbs?|;b?|pounds?|s?|weight?|wights?|:?\s?",re.I)
    p = re.compile("(\d{1,3})\W?#s?|lbs?|;b?|pounds?|s?|weight?|wights?|:?\s?",re.I)
    p = p.sub(r"\1",data)
    return p

#clean height
def height(data):
    p = re.compile("(\d{1})[\'](\d{1,2})[\”|\“]")
    p = p.sub(r"\1\2",data)
    return p

#extract weight
def calWei(data):
    w = 0
    match = re.search(r',[\'](\d{2,3})[\'|\'],',data)
    if(match!= None):
        s = match.group()
        match = re.search(r'(\d{2,3})',s)
        w = int(match.group())
    return (w)

#extract height
def calHei(data):
    h = 0
    match = re.search(r',[\"](\d\d{1,2})[\"|\"]',data)
    if(match!= None):
        s = match.group()
        match = re.search(r'(\d\d{1,2})',s)
        h = int(match.group())
    return h

#Min Height
def minHei (heiList):
    return min(heiList)

#max height
def maxHei (heiList):
    return max(heiList)

#average height
def aveHei (heiList):
    return sum(heiList)/len(heiList)

#extract timestamp
def timestamp(data):
    date = None
    match = re.search(r'\d{4}-\d{1,2}-\d{1,2}',data)
    if(match!= None):
        date = datetime.datetime.strptime(match.group(), '%Y-%m-%d').date()
    return date

#calculate Age
def calAge(birthday):
    age = 0
    if (birthday != None):
        today = datetime.datetime.today() 
        age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day)) 
    return age

#average age
def aveAge (ageList):
    return sum(ageList)/len(ageList)

#Minimum age
def minAge (ageList):
    return min(ageList)

#Max age
def maxAge (ageList):
    return max(ageList)
#BMI
def BMI (weight, height):
    bmi = int(weight/(height)**2*703)
    return bmi
#average BMI
def aveBMI (bList):
    return sum(bList)/len(bList)

#Min BMI
def minBMI(bList):
    return min(bList)
#Max BMI
def maxBMI(bList):
    return max(bList)
#ID
def ID(data):
    ID = None
    match = re.search(r'(\d{1,3})',data)
    if(match!= None):
        s = match.group()
        match = re.search(r'(\d{1,3})',s)
        ID = int(match.group())
    return ID
    

with open('regex_data.csv','r',encoding='utf8')as readFile:
    reader = csv.reader(readFile)
    for row in reader:
        row = date(str(row))
        row = weight(str(row))
        row = height(str(row))
        time = timestamp(row)
        age = calAge(time)
        w = calWei(row)
        h = calHei(row)
        i = ID(row)
        if(age != 0):
            ageList.append(age)
        if(h != 0):
            hList.append(h)
        if (w != 0):
            wList.append(w)
            if(h !=0):
                bmi = BMI(w,h)
                if(bmi!=0):
                    BMIL.append(bmi)
        if(i != None):
            IDL.append(i)
        #print(row+"\n"+"Age: "+str(age))
        writeFile.write(str(row+"\n"))

averageA = aveAge(ageList)
minA = minAge(ageList)
maxA = maxAge(ageList)

averageH = aveHei(hList)
minH = minHei(hList)
maxH = maxHei(hList)

averageB = aveBMI(BMIL)
minB = minBMI(BMIL)
maxB = maxBMI(BMIL)

html = open("part2.html",'w')


html.write("<html>\n<body>\n<h1>BMI data</h1>\n<ul>\n")
html.write("<table border='1'><tr><td><td>Age</td><td>Height</td><td>BMI</td></tr>\n")
html.write("<tr><td>Max</td><td>"+str(maxA)+"</td><td>"+str(maxH)+"</td><td>"+str(maxB)+"</td></tr>\n")
html.write("<tr><td>Min</td><td>"+str(minA)+"</td><td>"+str(minH)+"</td><td>"+str(minB)+"</td></tr>\n")
html.write("<tr><td>Mean</td><td>"+str(averageA)+"</td><td>"+str(averageH)+"</td><td>"+str(averageB)+"</td></tr>\n")
html.write("</table>")

html.write("\n<h1>BMI</h1>\n<ul>\n")
html.write("<table border='1'><tr><td>BMI</td></tr>\n")

for i in range(len(BMIL)):
    html.write('<tr><td><font color="red">'+str(IDL[i])+"</td><td>"+str(BMIL[i])+"</td></font></tr>\n")
html.write("</table>")

html.write("</body></html>")
html.close()
writeFile.close()
