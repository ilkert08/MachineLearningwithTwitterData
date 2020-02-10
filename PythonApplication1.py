import tokenize
X = [[3, 6], [4,8],[0,0], [6,10], [8,12]]
y = [4, 4, 4, 7, 7]
from sklearn.neighbors import KNeighborsClassifier
from sklearn import preprocessing
from sklearn.neighbors import NearestNeighbors
import io
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import csv


dataArray =[]
labelArray = []
convertedDataArray = []
le = preprocessing.LabelEncoder()


def stopWordsRemoval():

    print("Start")
    stop_words = set(stopwords.words('english')) 
    file1 = open("C:/Users/ilkertinkir/Desktop/FilteredText/nonfiltered55.txt", "r") 
    t = 0
    for  t in range(200000): 
        line = file1.readline() 
        print(t)
        words = line.split() 
        for r in words: 
            if not r in stop_words: 
                appendFile = open('C:/Users/ilkertinkir/Desktop/lastFilter.txt','a') 
                appendFile.write(" "+ r) 
                appendFile.close()
        appendFile = open('C:/Users/ilkertinkir/Desktop/lastFilter.txt','a') 
        appendFile.write("\n")
        appendFile.close()


def wordSteaming():
    from nltk.stem import PorterStemmer 
    from nltk.tokenize import word_tokenize 
    print("giris!")
    file1 = open("C:/Users/ilkertinkir/Desktop/FilteredText/lastfilter.txt")
    ps = PorterStemmer() 
    t = 0


    for t in range(200000):

        line = file1.readline()
        words5 = line.split()
        for r in words5:
            words = word_tokenize(r) 
            for w in words: 
                featureFile = open("C:/Users/ilkertinkir/Desktop/FilteredText/features.txt","a")
                featureFile.write(ps.stem(w) + " ")
                #print(w, " : ", ps.stem(w))
        #print("ALT SATIR!")
        featureFile.write("\n")
        #featureFile.close()
    
def uniqueWords():
    file1 = open("C:/Users/ilkertinkir/Desktop/FilteredText/sonhal/highFreqList.txt")
    reader = file1.read()
    splt0 = reader.split()
    print(len(reader))
    splitted = reader.split()
    mySet = set(splitted)
    print(len(mySet))
    myList = list(mySet)
    file1.close()
    print(myList[0])
    print(len(myList))
    #60902 All Unique Word Number
    #3951 High Freq > 10 
    file1 = open("C:/Users/ilkertinkir/Desktop/FilteredText/sonhal/highFreqList.txt")
    i = 0
    k = 0
    listofSet = []


#    low = 0
#    for k in range(1):
#        for w in myList:
#            c = 0
#            for w2 in splt0:
#                if w == w2:
#                    c = c + 1
#            if c > 10:
#                file2 = open("C:/Users/ilkertinkir/Desktop/FilteredText/highFreq.txt","a")
#                print(w+":"+str(c))
#                low = low + 1
#                print("High:"+ str(low))
#                file2.write(w+" ")
#                file2.close()
#            print("I"+str(i))
#            i = i + 1              
#    print("LOW FREQ:" + str(low))   




    for i in range (60001):
        line = file1.readline()
        splitted2 = line.split()
        ss = ""
        file2 = open("C:/Users/ilkertinkir/Desktop/FilteredText/sonhal/sonsayilar.txt","a")    
        for word in splitted2:      
            ss = ss + " "+ str(myList.index(word))            
                
        listofSet.append(ss)
        file2.write(ss+"\n")          
        file2.close()
    
    file1.close()



def highFreqList():
    file1 = open('C:/Users/ilkertinkir/Desktop/FilteredText/otuzbinsozcuk.txt', 'rt')
    file2 = open('C:/Users/ilkertinkir/Desktop/FilteredText/highFreq.txt', 'rt')
    
    reader2 = file2.read()
    splt2 = reader2.split()
    
    for i in range(0, 60001):
        reader1 = file1.readline()       
        splt1 = reader1.split()
        ss = ""
        for w in splt1:
            for w2 in splt2:
                if w == w2:
                    ss = ss + " " + w
        file3 = open('C:/Users/ilkertinkir/Desktop/FilteredText/sonhal/highFreqList.txt', 'a')
        file3.write(ss)
        file3.write("\n")
        file3.close()
        
    file1.close()
    file2.close()

def newList():
    x = []
    return x


def dataStabilizer():
   
     # 3951 Adet Unique Low Freq Sozcuk bulunmaktadir. Hesaplandi.
    file_input = open('C:/Users/ilkertinkir/Desktop/FilteredText/sonhal/sonsayilar.txt', 'rt')


    #CSV DOSYASININ 1,2,4 ve 5. sutunları kullanılacaktir(ID-1, DATE-2, NICKNAME-4, TWEET-5)
    #le.fit(["i am so happy today", "i am so sad today", "i am so happy and funny"])
    #print(le.transform(["i am so happy today", "i am so sad today", "i am so happy and funny"]))
    i=0
    max = 0
    tryArray = []

    print("TRICK")
    for i in range(0,10000):
        x = file_input.readline()


    for i in range(10000, 20000):
        labelArray.append(0)
        line = file_input.readline()  
        splt = line.split()
        x = newList()
        for j in range(0, 3951):
            x.append(0)
        for sp in splt:
            x[int(sp)] = 5
        convertedDataArray.append(x)
        tryArray.clear()


        if i == 15000:
            print("15000!")
          
            
    print("TRICK2")   

    for i in range(0, 20000):
        t = file_input.readline()

    for i in range(40000, 50000):          
        labelArray.append(4)
        line = file_input.readline()  
        splt = line.split()
        x = newList()
        for j in range(0, 3951):
            x.append(0)
        for sp in splt:
            x[int(sp)] = 5       
        convertedDataArray.append(x)
        
        tryArray.clear()

    print(len(labelArray))
    print(len(convertedDataArray))
    print(len(convertedDataArray[5]))
    file_input.close()    

def kNN ():
    dataStabilizer()
    print("Gecti!")
    file_input = open('C:/Users/ilkertinkir/Desktop/FilteredText/sonhal/sonsayilar.txt', 'rt')
    neigh = KNeighborsClassifier(n_neighbors=2)
    print("Training!")
    neigh.fit(convertedDataArray, labelArray)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    i = 0
    acc = 0
    akk = 0
    print("DONGU")
    dataArray.clear()
    for i in range(0, 3951):
        dataArray.append(0)
    for i in range(0, 100):
        line = file_input.readline()
        splt = line.split()
        x = newList()
        for l in range(0,3951):
             x.append(0)

        for sp in splt:              
            x[int(sp)] = 1
        if neigh.predict([x])[0] == 4:          
            acc = acc  + 1
        else:
            akk = akk + 1
            print(neigh.predict([dataArray]))       
               
        for j in range(0, 3951):
            dataArray[j] = 0    
        print("ACC:"+str(acc))
        print("AKK:"+str(akk))



    dataArray.clear()
    for i in range(0, 3951):
        dataArray.append(0)
    
    for i in range(100, 30000):
        line = file_input.readline()



    for i in range(30001, 30101):
        line = file_input.readline()
        splt = line.split()
        x = newList()
        for l in range(0,3951):
            x.append(0)
        for sp in splt:
            x[int(sp)] = 1
            
        if neigh.predict([dataArray])[0] == "0":
            acc = acc  + 1
        else:
            akk = akk + 1
            
    print("ACC:"+str(acc))
    print("AKK:"+str(akk))
              

    print("Accuracy:", 100*(200-acc) / 200 )


    text_file = open("C:/Users/ilkertinkir/Documents/NetBeansProjects/bilgiyeErisim1/info.txt", "a+")
    nn = text_file.write("Test Datasi Sayisi: "+ str(200) + "\nDogru Tahmin Sayisi:"+ str(200 - acc) + "\nYanlis Tahmin Sayisi:"+str(acc)+ "\nDogru Tahmin Orani:"+ str(100*(200-acc) / 200) )
    text_file.close()
    file_input.close()
    dataArray.clear()
    labelArray.clear()
    convertedDataArray.clear()

def decisionTree():
    from sklearn import tree
    #X = [[0, 0], [1, 1]]
    #Y = [0, 1]
    dataStabilizer()
    print("Gecti!")
    file_input = open('C:/Users/ilkertinkir/Desktop/train_edit33.csv', 'rt')
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(convertedDataArray, labelArray)
    i = 0
    acc = 0
    for row in csv.reader(file_input):
        if i<5000:
            le.fit([ row[2], row[4], row[5]])   
            #print(le.transform([  row[1], row[2], row[4], row[5]  ])[1])
            if clf.predict([[
                          le.transform([   row[2], row[4], row[5]  ])[0],
                          le.transform([   row[2], row[4], row[5]  ])[1],
                          le.transform([   row[2], row[4], row[5]  ])[2] ]])[0] == "4":
                acc = acc  + 1
            ss0 = row[2] + row[4] + row[5] + "\nTahmin:" + clf.predict([[
                          le.transform([   row[2], row[4], row[5]  ])[0],
                          le.transform([   row[2], row[4], row[5]  ])[1],
                          le.transform([   row[2], row[4], row[5]  ])[2] ]])[0] +" " + "Asil Sonuc:" + row[0] +"\n\n"

            
            
  #          print("Tahmin:",clf.predict([[
  #                        le.transform([  row[1], row[2], row[4], row[5]  ])[0],
  #                        le.transform([  row[1], row[2], row[4], row[5]  ])[1],
  #                        le.transform([  row[1], row[2], row[4], row[5]  ])[2],
  #                        le.transform([  row[1], row[2], row[4], row[5]  ])[3] ]]))
  #          print("Asil Sonuc:", row[0])
        
        if i == 99999:
            print("Ara!")
        if i>100000 and i<105000:
            le.fit([row[1], row[2], row[4], row[5]])   
            #print(le.transform([  row[1], row[2], row[4], row[5]  ])[1])
            if clf.predict([[
                          le.transform([   row[2], row[4], row[5]  ])[0],
                          le.transform([   row[2], row[4], row[5]  ])[1],
                          le.transform([   row[2], row[4], row[5]  ])[2] ]])[0] == "0":
                acc = acc  + 1
            ss0 = row[2] + row[4] + row[5] + "\nTahmin:" + clf.predict([[
                          le.transform([   row[2], row[4], row[5]  ])[0],
                          le.transform([   row[2], row[4], row[5]  ])[1],
                          le.transform([   row[2], row[4], row[5]  ])[2] ]])[0] +" " + "Asil Sonuc:" + row[0] +"\n\n"

           


     #       print("Tahmin:",clf.predict([[
     #                     le.transform([  row[1], row[2], row[4], row[5]  ])[0],
     #                     le.transform([  row[1], row[2], row[4], row[5]  ])[1],
     #                     le.transform([  row[1], row[2], row[4], row[5]  ])[2],
     #                     le.transform([  row[1], row[2], row[4], row[5]  ])[3] ]]))
     #       print("Asil Sonuc:", row[0])
        
        i = i + 1

    print("Accuracy:", 100 * (10000-acc)/10000)
    number = 100 * (1000-acc)/1000
    text_file = open("C:/Users/ilkertinkir/Documents/NetBeansProjects/bilgiyeErisim1/info.txt", "a+")
    nn = text_file.write("Test Datasi Sayisi: "+ str(10000) + "\nDogru Tahmin Sayisi:"+ str(10000 - acc) + "\nYanlis Tahmin Sayisi:"+str(acc)+ "\nDogru Tahmin Orani:"+ str(100*(10000-acc) / 10000) )    
    file_input.close()
    dataArray.clear()
    labelArray.clear()
    convertedDataArray.clear()



#wordSteaming()
#stopWordsRemoval()
#uniqueWords()
    #le.fit(["i am so happy today", "i am so sad today", "i am so happy and funny"])
    #print(le.transform(["i am so happy today", "i am so sad today", "i am so happy and funny"]))
file00 = open('C:/Users/ilkertinkir/Documents/NetBeansProjects/bilgiyeErisim1/pythonVariables.txt', 'rt')
ss = file00.readline()
if ss == "firstAlgorithm":
    print("Decision Tree:")
    decisionTree()
elif ss == "secondAlgorithm":
    print("kNN:")
    kNN()

