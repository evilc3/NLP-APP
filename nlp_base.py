
from nltk import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from string import punctuation
from nltk.stem import PorterStemmer,SnowballStemmer,ISRIStemmer,WordNetLemmatizer
from nltk import pos_tag
import re
import pickle
import os
from  sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
import pandas as pd


class nlp():



    def __init__(self):
       # initialise default words
       self.stop_dict = set(stopwords.words('english')).union(punctuation)
       self.vec = CountVectorizer()
       self.stemmer = PorterStemmer()
       self.lemmat = WordNetLemmatizer()
       self.stop_dict_name = 'nltk'
       self.vec_name = 'Count Vectorizer'
       self.stemmer_name = 'ProterStemmer'
       self.tokenizer_name = 'word'
       self.web_stop_words  = ["a","a's","able","about","above","according","accordingly","across","actually","after",
                                "afterwards","again","against","ain't","all","allow","allows","almost","alone","along",
                                "already","also","although","always","am","among","amongst","an","and","another","any",
                                "anybody","anyhow","anyone","anything","anyway","anyways","anywhere","apart",
                                "appear","appreciate","appropriate","are","aren't","around","as","aside",
                                "ask","asking","associated","at","available","away","awfully","b","be",
                                "became","because","become","becomes","becoming","been","before","beforehand",
                                "behind","being","believe","below","beside","besides","best","better","between","beyond",
                                "both","brief","but","by","c","c'mon","c's","came","can","can't","cannot","cant","cause","causes","certain","certainly",
                                "changes","clearly","co","com","come","comes","concerning","consequently","consider","considering","contain","containing",
                                "contains","corresponding","could","couldn't","course","currently","d","definitely","described","despite","did","didn't",
                                "different","do","does","doesn't","doing","don't","done","down","downwards","during","e","each","edu","eg","eight","either",
                                "else","elsewhere","enough","entirely","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere",
                                "ex","exactly","example","except","f","far","few","fifth","first","five","followed","following","follows","for","former",
                                "formerly","forth","four","from","further","furthermore","g","get","gets","getting","given","gives","go","goes","going",
                                "gone","got","gotten","greetings","h","had","hadn't","happens","hardly","has","hasn't","have","haven't","having","he","he's",
                                "hello","help","hence","her","here","here's","hereafter","hereby","herein","hereupon","hers","herself","hi","him","himself","his",
                                "hither","hopefully","how","howbeit","however","i","i'd","i'll","i'm","i've","ie","if","ignored","immediate","in","inasmuch","inc",
                                "indeed","indicate","indicated","indicates","inner","insofar","instead","into","inward","is","isn't","it","it'd","it'll","it's","its",
                                "itself","j","just","k","keep","keeps","kept","know","known","knows","l","last","lately","later","latter","latterly","least","less",
                                "lest","let","let's","like","liked","likely","little","look","looking","looks","ltd","m","mainly","many","may","maybe","me","mean",
                                "meanwhile","merely","might","more","moreover","most","mostly","much","must","my","myself","n","name","namely","nd","near","nearly",
                                "necessary","need","needs","neither","never","nevertheless","new","next","nine","no","nobody","non","none","noone","nor","normally",
                                "not","nothing","novel","now","nowhere","o","obviously","of","off","often","oh","ok","okay","old","on","once","one","ones","only",
                                "onto","or","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall","own","p","particular",
                                "particularly","per","perhaps","placed","please","plus","possible","presumably","probably","provides","q","que","quite","qv","r",
                                "rather","rd","re","really","reasonably","regarding","regardless","regards","relatively","respectively","right","'s","said","same",
                                "saw","say","saying","says","second","secondly","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sensible",
                                "sent","serious","seriously","seven","several","shall","she","should","shouldn't","since","six","so","some","somebody","somehow",
                                "someone","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specified","specify","specifying","still","sub",
                                "such","sup","sure","t","t's","take","taken","tell","tends","th","than","thank","thanks","thanx","that","that's","thats","the","their",
                                "theirs","them","themselves","then","thence","there","there's","thereafter","thereby","therefore","therein","theres","thereupon","these",
                                "they","they'd","they'll","they're","they've","think","third","this","thorough","thoroughly","those","though","three","through",
                                "throughout","thru","thus","to","together","too","took","toward","towards","tried","tries","truly","try","trying","twice","two","u",
                                "un","under","unfortunately","unless","unlikely","until","unto","up","upon","us","use","used","useful","uses","using","usually","uucp",
                                "v","value","various","very","via","viz","vs","w","want","wants","was","wasn't","way","we","we'd","we'll","we're","we've","welcome",
                                "well","went","were","weren't","what","what's","whatever","when","whence","whenever","where","where's","whereafter","whereas","whereby",
                                "wherein","whereupon","wherever","whether","which","while","whither","who","who's","whoever","whole","whom","whose","why","will",
                                "willing","wish","with","within","without","won't","wonder","would","wouldn't","x","y","yes","yet","you","you'd","you'll","you're",
                                "you've","your","yours","yourself","yourselves","z","zero","html","ol"]

       self.stop_web_punct = self.stop_dict.union(self.web_stop_words)                    

    

    def get_settings(self):
        return  [self.tokenizer_name,self.stop_dict_name,self.vec_name,self.stemmer_name]


    def apply_settings(self,x):

        if x == 'word':
           self.tokenizer_name = x
        elif x == 'sent':
            self.tokenizer_name = x    
        
        
        

        if x == 'nltk':
        #    self.stop_dict  = stopwords.words('english')
           self.stop_dict_name = x
        elif x == 'Extend':
            # self.stop_dict = stopwords.words('english')
            self.stop_dict_name = x


        if x == 'Count':
            self.vec  = CountVectorizer()
            self.vec_name = x
        elif x == 'TfiDf':
            # print(self.vec)
            self.vec = TfidfVectorizer() 
            self.vec_name = x
            # print(self.vec)


        if x == 'Porter':
            self.stemmer  = PorterStemmer()
            self.stemmer_name = x
        elif x == 'SnowBall':
            self.stemmer = SnowballStemmer(language = 'english',ignore_stopwords = True)    
            self.stemmer_name = x
        elif x == 'ISR':
            self.stemmer = ISRIStemmer()
            self.stemmer_name = x


    def get_tokens(self,input):
        if self.tokenizer_name == 'word':
           return str(word_tokenize(input))
        elif self.tokenizer_name == 'sent':
           return str(sent_tokenize(input))
        else: 
           print('error invaid tokenizer type')

    def get_stemmer(self,input):
        #need to add different stemmers here
        text = ''
        if self.tokenizer_name == 'word':
            for i in word_tokenize(input):
                text += self.stemmer.stem(i)+' '  
        elif self.tokenizer_name == 'sent':
            for i in sent_tokenize(input):
                text += self.stemmer.stem(i)+' '          


        return text   

    def valid_char(self,input):
        
        for j in input:
            if ord(j) <= 126 and ord(j)>=33:
                continue

            else:
                return  False

        return True
       
    def get_stopwords(self,input):

        input =  re.sub('[!@#$%^&*()\n_:><?\-.{}|+-,;""``~`—]|[0-9]|/|=|\[\]|\[\[\]\]',' ',input)
        input = re.sub('[“’\']','',input)   
        
        # print('input after regex',input)

        if self.stop_dict_name == 'nltk':
            return str(list(i for i in word_tokenize(input) if i not in self.stop_dict  and not i.split('.')[-1].isdigit() and not i.split(',')[-1].isdigit() and len(i)>1 and self.valid_char(i)))         
        elif self.stop_dict_name == 'Extend':
            # stopwords_en_punct = set(stopwords.words('english')).union(punctuation)
            
            return str(list(i for i in word_tokenize(input) if i not in self.stop_web_punct and not i.split('.')[-1].isdigit() and not i.split(',')[-1].isdigit() and len(i)>1 and self.valid_char(i)))

    def get_vec(self,input):

        # if type == 'Count':
        # print(self.vec)
        return str(self.vec.fit_transform([input]).toarray())

        # elif type == 'TfiDf':
        #     return str(TfidfVectorizer().fit_transform([input]).toarray())   

    def penn2morphy(self,penntag):
        """ Converts Penn Treebank tags to WordNet. """
        morphy_tag = {'NN':'n', 'JJ':'a',
                  'VB':'v', 'RB':'r'}
        try:
            return morphy_tag[penntag[:2]]
        except:
            return 'n' 
    
    def lemmatize_sent(self,text): 
        wnl = WordNetLemmatizer()
        # Text input is string, returns lowercased strings.
        return str([wnl.lemmatize(word.lower(), pos=self.penn2morphy(tag)) for word, tag in pos_tag(word_tokenize(text))])


    def nlp_cleaner(self,x,inf = 0):

        if type(x) != str:
            return 'invalid input , input must be string'
        
        #1 word tokenization , lowercasing
        x =  re.sub('[!@#$%^&*()\n_:><?\-.{}|+-,;""``~`—]|[0-9]|/|=|\[\]|\[\[\]\]',' ',x)
        x = re.sub('[“’\']','',x)   

        if self.tokenizer_name == 'word':
            x = list(map(str.lower,word_tokenize(x)))
        elif self.tokenizer_name == 'sent':
            x = list(map(str.lower,sent_tokenize(x)))
            print(self.tokenizer_name)    
    
        if inf:
            print('tokenizer')
            print(x[0:10])
    
    
        #2 stop words , removing punctuations
        if self.stop_dict_name == 'nltk':
            
            x = list(i for i in x if i not in self.stop_dict and not i.split('.')[-1].isdigit() and not i.split(',')[-1].isdigit() and len(i)>1 and self.valid_char(i))
        elif self.stop_dict_name == 'Extend':
            
            
            x = list(i for i in x if i not in self.stop_web_punct and not i.split('.')[-1].isdigit() and not i.split(',')[-1].isdigit()and len(i)>1 and self.valid_char(i) )
            # print(self.stop_dict_name)

        

    
    
        if inf:
            print('StopWords')
            print(x[0:10])

        
        
        #3 Stemming and Lemmatization  
    
    
        if self.stemmer_name == 'Porter':
            x = list(self.stemmer.stem(i) for i in x)
        elif self.stemmer_name == 'SnowBall':
            x = list(self.stemmer.stem(i) for i in x)    
        elif self.stemmer_name == 'ISR':
            x = list(self.stemmer.stem(i) for i in  x)    
    
        if inf:
            print('after stemming')
            print(x[0:10])        
    
    
        return x
    
        
    def create_vec(self,name,col = 'STORY',encoding = 'UTF-8'):
        ext = name.split('.')[-1]
        
        if ext == 'csv':
            data = pd.read_csv(name,encoding= encoding)
        elif ext == 'xlsx':
            data = pd.read_excel(io = name,encoding = encoding)

        data = self.vec.fit_transform(data[col])
        pickle.dump(data,open('vec_metrix_.txt','wb'))
        pickle.dump(self.vec,open(self.vec_name+'.txt','wb'))
        


        

if __name__ == "__main__":

    n =  nlp()
    # print(n.get_stopwords('how are u doing my friend its been a long time'))
    # # print(n.get_stemmer(input = 'how are u doing my friend its been a long time'))
    # print(n.get_vec('how are u doing my friend its been a long time'))
    # # print(n.get_vec('how are u doing my friend its been a long time'))
    # # print(n.lemmatize_sent(text = 'how are u doing my friend its been a long time'))
    # # print(n.get_tokens(input = 'how are u doing my friend its been a long time'))
    # n.apply_settings(x = 'TfiDf')
    # print(n.get_vec('how are u doing my friend its been a long time'))

    # print(n.nlp_cleaner(['how are u doing my friend its been a long time ,,,,.......2930203??{}P:=-"0:OOIUYTRRE@!'' \""[][[]] \'   <p> </p>   🎉  ₹ ////  1,2322 1.22 ******s '][0]))

    string = "do..  ............................................................................................................\
    Mumbai: India Inc's external commercial borrowings (ECBs) fell by 45% to $2.42 billion in January 2019 as compared \
    to the year-ago period, data from the Reserve Bank of India (RBI) has showed.\n\n\nDomestic firms had raised $5.40 billion \
    from overseas sources during January 2018. Of the total borrowings during the month, $2.27 billion was raised through the automatic \
    route of external commercial borrowings (ECBs). The remaining $150 million was taken through the approval route, according to RBI data on ECB for January 2019.\
    <p> </p>   🎉  ₹ ////  1,2322 1.22 <html> <html> <li> </li> ol> //hat !@#$%^&*!@#$%^&*()$%^&*()"

    # print(n.nlp_cleaner(string))
  
    # print(punctuation)
    n.stop_dict_name  = 'Extend'
    print(len(n.stop_web_punct),len(n.stop_dict))

    print(n.nlp_cleaner(string))
    # print(n.get_stopwords('input are u doing my friend its been a long time experiment today went well ,,,,.......2930203??{}P:=-"0:OOIUYTRRE@!'' \""[][[]] \'   <p> </p>   🎉  ₹ ////  1,2322 1.22'))
    






           