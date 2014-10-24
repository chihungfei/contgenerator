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

temp = f[0]
bigramCount = string.atoi(re.findall('\d+', temp)[0])
f = f[2:]

bigramSet = {}
prefixSet = {}
suffixSet = {}

''' manipulating and calculating'''

class Bigram:
    def __init__(self, word, count):
        xx = word.split(' ')
        self.full = word
        self.prefix = xx[0]
        self.suffix = xx[1]
        self.count = string.atoi(count)
 
        
bigramList = []
       
for each in f:
    temp = each.split('\t')
    a = Bigram(temp[3], temp[1])
    bigramList.append(a)
        
        
def calcBigramSet(bigramss):
    global bigramSet, prefixSet, suffixSet
    
    for each in bigramss:
            bigramSet[each.full] = each.count
            
            if each.prefix in prefixSet:
                prefixSet[each.prefix] += each.count
            else:
                prefixSet[each.prefix] = each.count
               
            if each.suffix in suffixSet:
                suffixSet[each.suffix] += each.count
            else:
                suffixSet[each.suffix] = each.count 
                
calcBigramSet(bigramList)
                
''' Calc it'''
text = []
zoo = []
zot = []
zto = []
ztt = []

for each in bigramList:
    text.append(each.full)
    zoo.append(each.count)
    zto.append(suffixSet[each.suffix] - each.count)
    zot.append(prefixSet[each.prefix] - each.count)
    ztt.append(bigramCount - each.count - (suffixSet[each.suffix] - each.count) -(prefixSet[each.prefix] - each.count))

'''write to the file'''

t = open('out.txt', 'w')
t.write('Item\t011\t012\t021\t022\n')

k = 0
while k < len(text):
    t.write(text[k]+'\t'+str(zoo[k])+'\t'+str(zot[k])+'\t'+str(zto[k])+'\t'+str(ztt[k])+'\n')
    k += 1

t.close()
