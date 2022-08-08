from bs4 import BeautifulSoup
import io
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import *
import pathlib
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

stop_words=set(stopwords.words("english")) 
space_gained = 0
space_input = 0

print("Welcome to Spazer\n")
for x in range(10):
    filename = str(x) + ".html"
    file = pathlib.Path('input/' + filename)
    if (file.exists()):
        print("Reading " + filename)
        f = open('input/' + filename, 'r', errors="ignore")
        contents = f.read()   
        #The code begins...
        soup = BeautifulSoup(contents,'html.parser') #Extracting the html content form the html file.  
        
        word_tokens = word_tokenize(soup.get_text()) #Tokenizing every word of the file/Splitting a sentence into list of words.
        filtered_words = [w for w in word_tokens if not w.lower() in stop_words] #Removing the stopwords from the file.
        list_to_str = " ".join(map(str,filtered_words)) #Converting list to string
        tokenizer = RegexpTokenizer(r'\w+') #Giving the regular expression
        output_1 = tokenizer.tokenize(list_to_str) #Matches all words with the regular expression
        output_2= []
        #Extracting keywords_1
        keywords_1 = ['address','Contact','contact','Address','Park','Sector','Plot','Road','Avenue','Floor','Building','Pin'] 
        for k in keywords_1:
          for l in keywords_1:
            if k in output_1 and l in output_1[(output_1.index(k)):(output_1.index(k))+60] and k != l and len(output_1[(output_1.index(k)):(output_1.index(l))+15]) > 5:
              output_2 = output_2 + (output_1[(output_1.index(k))-10:(output_1.index(l))+10])
              output_3 = ' '.join(words for words in output_2)
              
        output_4 = word_tokenize(output_3)
        output_5 = nltk.pos_tag(output_4) #Finding parts of speech of each word
        output_6 = []
        keywords_2 = ['VB','VBP','VBD','MD','VBN','TO','DT','PRP','VBZ','VBG','NNS','RB','JJ'] #Type of words to be removed from the output
        for l in output_5:
          for k in keywords_2:
            if l[1] == k:
              output_5.remove(l)
        for l in output_5:
          output_6 = output_6 + [l[0]]
        output_7 = ' '.join(words for words in output_6)

        print ("Writing reduced " + filename)
        fw = open('output/' + filename, "w")
        fw.write(output_7)
        fw.close()
        f.close()
        
        space_input = space_input + len(contents)
        space_gained = space_gained + len(contents) - len(output_7)        

print("Total Space Gained = " + str(round(space_gained*100/space_input, 2)) + "%")