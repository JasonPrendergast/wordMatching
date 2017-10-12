import nltk
from nltk.tokenize import word_tokenize
import numpy as np
import random
import pickle
from collections import Counter
from nltk.stem import WordNetLemmatizer
#from collections import Counter


        
        
def lexicon_play():
    lexicon =[]

    with open('Towns_List.csv','r') as f:
        towns = f.readlines()
    with open('towns.csv','r') as f:
        towns2 = f.readlines()
           
    
    with open('lexicon_jt.pickle','rb') as f:
        print('label')
        labellexicon = pickle.load(f)
        print(len(labellexicon))
    #print(labellexicon)
    for i in range(len(labellexicon)):
        #print(str(labellexicon[i]))
        all_words = word_tokenize(str(labellexicon[i]))
        lexicon += list(all_words)

    
    count = 0
    for t in range(len(towns)):
        towns[t]=str(towns[t]).lower()
        
    for t in range(len(towns2)):
        towns2[t]=str(towns2[t]).lower()

    all_towns = towns+towns2

    all_towns = Counter(all_towns)

    #for t in all_towns:
    # #   print(t)
     #   print(all_towns[t])
        
        

       # print(t)
    #for t in towns:
    #    print(t)
    

        
   # for w in lexicon:
        #print(count)
    #    for t in all_towns:
   #         if t == w:
    #            print(w)
    #            print(all_towns[w])
    #    count+=1
    w_counts = Counter(lexicon)

    for w in w_counts:
        #print(w)
        for t in all_towns:
           # print(t)
            if t.strip() == w:
                print(w)
                print(w_counts[w])
            
lexicon_play()
