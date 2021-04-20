import binascii
from collections import defaultdict
from typing import Sequence
from collections import Counter
import sys

v = '11122112141311112123131222211121621211124112213221112162112113114163113211421121132221622222411321311331611221121413111121231312222111216322121412123312222111122141624112123212416214122231631132114221112162321321242113531132142162321211424112123212322111121322231221111322216222232122141212112163113211422111216231224113221211211232216231224113113232121151124162312311111311416311321142211113212221112162411321222111216212111214132122211121623212114241121232123221111213222312211113222162411211422111124112214113316121421413132163131211211212321241642112141311112162222241132122211121624112231241121121121323221311416311321142141322122111216121212163131214121322213221111321311331615113114162411213242121632122411311322111211241631312211112123212416221321412132221112162411213222141621142211113212221112162112113222164211214131111132131622222123241122323113161421142111111341211212111151322122111122111111512213221111241122131151232121121135211422111132123221115124112123212311513113211422111111513113211211212111221111511'


def xorc(list):
    xord = []
    if(len(list) %2 != 0):
        list.append('0')
    for i in list:
        xord.append(int(i[0])^int(i[1]))
    print(xord)

    for h in xord:
        z = (h if h==0 else 1)
        print(str(h), end ="")

def xorList(list):
    xored=[]
    if(len(list) %2 != 0):
        list.append('0')
    for idx in range(0,len(list)):
        if (idx > 0):
           xored.append((int(list[idx-1])^int(list[idx])))
    return xored

def unique(list):
 
    ulist = []
  
    for x in list:
        if x not in ulist:
            ulist.append(x)
    return ulist
   
def divideSeq(list):
    seq = []
    aux = str(list[0])
    for idx in range(0,len(list)):
        if (idx > 0):
            if ( list[idx-1] > list[idx] ):
                seq.append(str(aux))
                aux = ''.join(str(list[idx]))
            else: 
                aux += str(list[idx])
    return seq

def maxOccor(list):
    L = list
    d = defaultdict(int)
    for i in L:
        d[i] += 1
    result = max(d.items(), key=lambda x: x[1])
    return result

def sepEachNchar(list,n):
    strs = []
    for idx in range(0, len(list), n):
        strs.append(list[idx : idx + n])
    return strs

def occorUniqueVal(list):
    return dict(sorted(Counter(list).items(), key=lambda item: item[1], reverse = True))

def sumEachIdx(list):
    sumList=[]
    for i in list:
        sumInt=0
        for idx in range(0,len(i)):
            sumInt += int(i[idx])
        sumList.append(str(sumInt))
    return sumList

def isPrime(list):
    primelist = []
    for i in range(0,len(list)):
        num = int(list[i])
        if num > 1:
            for i in range(2, int(num/2)+1):
                if (num % i) == 0:
                    primelist.append('0')
                    break
            else:
                primelist.append('1')
        else:
            primelist.append('0')
    return primelist

def getReplace(searchKey,orderedDict,listToReplace):
    
    temp = list(orderedDict.items()) 

    if(len(listToReplace)<len(temp)):
        sys.exit("\n\n\n\n[ ! Error !] Replace list has not enough chars to replace\n\n\n\n")

    res = [idx for idx, key in enumerate(temp) if key[0] == searchKey]
    
    return str(listToReplace[res[0]])

def replaceByRank(list,replaceList):
    orderedFreq = occorUniqueVal(list)
    for s in unique(list):
        repl=getReplace(s,orderedFreq,replaceList)
        for n, i in enumerate(list):
            if list[n] == s:
                list[n] = repl
    return list

def listToString(list):
    return ''.join(list)

#bytes_object=bytes.fromhex(v)
#ascii_string = bytes_object.decode("ASCII")

#print(ascii_string)


originalvalue = sepEachNchar(v,1)
pairs = sepEachNchar(v,2)
dv = divideSeq(v)
sumList = sumEachIdx(dv)

###### Change Settings 

commonEnglishLower = "etaoinsrhldcumfpgwybvkxjqz"
commonEnglishUpper = commonEnglishLower.upper()
alphabetUpper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabetLower = alphabetUpper.lower()
digits = "0123456789"
hexValues = "0123456789ABCDEF"

replaceVector = commonEnglishLower+commonEnglishUpper

#testString = sepEachNchar( listToString(replaceByRank(originalvalue,replaceVector)) ,1)

testString = pairs

print( "---------------------")
print( "[+] Input\n")
print( testString )
print("\n[i] Number of Unique values\n{}".format(str(len(unique(testString)))))
print("\n[i] Top character \n" + "Value {} appears {} time(s).".format(str(maxOccor(testString)[0]),str(maxOccor(testString)[1])))
print("\n[i] Frequency of Unique Values\n{}".format(str(occorUniqueVal(testString))))
print( "\n[-] Result: \n\n{}".format(listToString( replaceByRank(testString,replaceVector))))
print( "---------------------")
