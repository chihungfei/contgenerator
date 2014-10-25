import os, nltk, re, sys, string

'''Read the file, prompt the info, cleaning the text'''
filePath = os.path.split( os.path.realpath( sys.argv[0] ) )[0]
os.chdir(filePath)

f = open('1.txt').readlines()
temp = []
for each in f:
    temp.append(each.strip('\r\n'))
    
f = temp

temp = []
for each in f:
    temp.append(each.lower())
    
f = temp

temp = f[1]
bigramCount = string.atoi(re.findall('\d+', temp)[0])
f = f[2:]

g = sorted(f)
bigramSet = {}
prefixSet = {}
suffixSet = {}
bigramList = []

for each in f:
    temp = each.split('\t')
    xx = temp[3].split(' ')
    if bigramSet.has_key(temp[3]):
        bigramSet[temp[3]] += string.atoi(temp[1])
        g.remove(each)
    else:
        bigramSet[temp[3]] = string.atoi(temp[1])
        bigramList.append(temp[3])
        
    if not prefixSet.has_key(xx[0]):
        prefixSet[xx[0]] = string.atoi(temp[1])
    else:
        prefixSet[xx[0]] += string.atoi(temp[1])
            
    if not suffixSet.has_key(xx[1]):
        suffixSet[xx[1]] = string.atoi(temp[1])
    else:
        suffixSet[xx[1]] += string.atoi(temp[1])
    
            

'''a = Bigram(temp[3], temp[1])'''


''' manipulating and calculating'''

'''class Bigram:
    def __init__(self, word, count):
        word = word.lower()
        xx = word.split(' ')
        self.full = word
        self.prefix = xx[0]
        self.suffix = xx[1]
        self.count = string.atoi(count)
 
        
bigramList = []
b = []
       
for each in f:
    temp = each.split('\t')
    a = Bigram(temp[3], temp[1])
    bigramList.append(a)
    text = temp[3]
    b.append(text)
    
c = sorted(b)
a = []
  
k = 1  
n = []
while k < len(c) - 1:
        while c[k-1] == c[k]:
            a.append(c[k])
            n.append(b.index(c[k]))
            del(c[k-1])
        else:
            k += 1
a = list(set(a))     
n = list(set(n))

repe = {}

for each in n:
    try:
        t = bigramList[each]
        del(bigramList[each])
        tName = t.full
        if not repe.has_key(tName):
            repe[tName] = t.count
        else:
            repe[tName] += t.count
    except:
        print each
        next

print repe['to the']

for each in repe:
    a = Bigram(each, str(repe[each]))
    bigramList.append(a)'''

'''print b[28309]
print b[28308]

print bigramList[28309].prefix
print bigramList[28309].suffix'''

'''for eachone in b:
    if eachone in a:
        t = bigramList[b.index(eachone)]

        for x in range(0, b.index(eachone)):
            if bigramList[x].full == eachone:
                bigramList[x].count += t.count
                
        bigramList.remove(t)'''          

            
'''def calcBigramSet(bigramss):
    global bigramSet, prefixSet, suffixSet
    
    for each in bigramss:
            if each.full in bigramSet:
                bigramSet[each.full] += each.count
            else:
                bigramSet[each.full] = each.count
            
            if each.prefix in prefixSet:
                prefixSet[each.prefix] += each.count
            else:
                prefixSet[each.prefix] = each.count
               
            if each.suffix in suffixSet:
                suffixSet[each.suffix] += each.count
            else:
                suffixSet[each.suffix] = each.count 
                
calcBigramSet(bigramList)'''
                
''' Calc it'''
text = []
zoo = []
zot = []
zto = []
ztt = []

for each in bigramList:
    xx = each.split(' ')
    bi = each
    pr = xx[0]
    su = xx[1]
    try:
        text.append(bi)
        zoo.append(bigramSet[bi])
        zto.append(suffixSet[su] - bigramSet[bi])
        zot.append(prefixSet[pr] - bigramSet[bi])
        ztt.append(bigramCount - prefixSet[pr] - suffixSet[su] + bigramSet[bi])
    except:
        next

'''write to the file'''

'''print bigramCount
print prefixSet['it']
print suffixSet['be']'''


t = open('out.txt', 'w')
t.write('Item\t011\t012\t021\t022\n')

k = 0
while k < len(text):
    t.write(text[k]+'\t'+str(zoo[k])+'\t'+str(zot[k])+'\t'+str(zto[k])+'\t'+str(ztt[k])+'\n')
    k += 1

t.close()
