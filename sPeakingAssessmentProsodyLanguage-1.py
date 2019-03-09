from __future__ import print_function
import sys
def my_except_hook(exctype, value, traceback):
        print('There has been an error in the system')
sys.excepthook = my_except_hook
import warnings
if not sys.warnoptions:
    warnings.simplefilter("ignore")
import parselmouth
from parselmouth.praat import call, run_file
import glob
import operator
import speech_recognition as sr
from langdetect import detect
from langdetect import detect_langs
import numpy as np # linear algebra
from nltk.sentiment import SentimentAnalyzer
from aylienapiclient import textapi
client = textapi.Client("6c626cb8", "7933378b9f0590bc6f1f9f00b5049a8a")
import nltk, re, pprint
from nltk import word_tokenize
from nltk.tokenize import sent_tokenize
from nltk.probability import FreqDist
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
nltk.download('punkt')
import random
import time
import errno
import csv,sys
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
from subprocess import check_output
from sklearn import preprocessing
from sklearn.metrics import cohen_kappa_score
import queue
import sounddevice as sd
import soundfile as sf
import _thread  
import pickle
from scipy.stats import binom
from scipy.stats import ks_2samp
from scipy.stats import ttest_ind
from pandas import read_csv
from textblob import TextBlob
from collections import defaultdict
from nltk.classify.util import apply_features, accuracy as eval_accuracy
from nltk.collocations import BigramCollocationFinder
from nltk.metrics import (
    BigramAssocMeasures,
    precision as eval_precision,
    recall as eval_recall,
    f_measure as eval_f_measure,
)
from textblob import Word
from textblob.wordnet import VERB
from nltk.probability import FreqDist
from nltk.sentiment.util import save_file, timer

pathy = input("Enter the path to the Auto-Speech_Rater directory: ")
name = input("what is your name?    ")
t0 = int(input("Your desired Recording time in seconds:    "))
ran = input("jp for Japanese, ln for Like-Native, n for Native:    ")
smr = int(input("sampling rate; 16000 or 42000 or 48000 or 96000 Hz:    "))
bt=int(input("bit depth; 8 or 16 or 24 or 32 bit:    "))


pa00=pathy+"/"+"dataset"+"/"+"audioFiles"+"/"
pa0=pathy+"/"+"dataset"+"/"+"audioFiles"+"/"+name+".wav"
pa1=pathy+"/"+"dataset"+"/"+"datanewchi22.csv"
pa2=pathy+"/"+"dataset"+"/"+"stats.csv"
pa3=pathy+"/"+"dataset"+"/"+"datacorrP.csv"
pa4=pathy+"/"+"dataset"+"/"+"datanewchi.csv"
pa5=pathy+"/"+"dataset"+"/"+"datanewchi33.csv"
pa6=pathy+"/"+"dataset"+"/"+"datanewchi33.csv"
pa7=pathy+"/"+"dataset"+"/"+"datanewchi44.csv"
pa8=pathy+"/"+"dataset"+"/"+"essen"+"/"+"MLTRNL.praat"
pa9=pathy+"/"+"dataset"+"/"+"essen"+"/"+"myspsolution.praat"

rere=pa0

RECORD_TIME = t0

def countdown(p,q,w):
    i=p
    j=q
    z=w
    k=0
    while True:
        if(j==-1):
            j=59
            i -=1
        if(j > 9):  
            print(str(k)+str(i)+ " : " +str(j), "\t", end="\r")
        else:
            print(str(k)+str(i)+" : " + str(k)+str(j), "\t", end="\r")
        time.sleep(1)
        j -= 1
        if(i==0 and j==-1):
            break
    if(i==0 and j==-1):
        if z==0:
            huf="Go ahead!"
            print(huf)
        if z==1:
            huf="Time up!"
        # time.sleep(1)

print("===========================================")
print("HOLD ON!! get ready, 5 seconds to go!")
print("===========================================")
countdown(0,5,0) #countdown(min,sec)	


q = queue.Queue()
rec_start = int(time.time())

dev_info = sd.query_devices(2, 'input')
# samplerate = int(dev_info['default_samplerate'])
samplerate = smr

def data_callback(input_data, frames, time, status):
    if status:
        print(status, file=sys.stderr)
    q.put(input_data.copy())

with sf.SoundFile(rere, mode='x', samplerate=samplerate, channels=2) as file:
    with sd.InputStream(samplerate=samplerate, device=2, channels=2, callback=data_callback,blocksize=20500):
        rec_time = int(time.time()) - rec_start
        _thread.start_new_thread(countdown,(0,t0,1))
        while rec_time <= RECORD_TIME:
            file.write(q.get())
            rec_time = int(time.time()) - rec_start
                            
result_array = np.empty((0, 100))
path = pa0
files = glob.glob(path)
result_array = np.empty((0, 27))

try:
	def mysppron(m,p,q):
		sound=m
		sourcerun=p 
		path=q
		objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
		print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
		z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
		z2=z1.strip().split()
		z3=int(z2[13]) # will be the integer number 10
		z4=float(z2[14]) # will be the floating point number 8.3
		db= binom.rvs(n=10,p=z4,size=10000)
		a=np.array(db)
		b=np.mean(a)*100/10
		print ("Pronunciation_posteriori_probability_score_percentage= :%.2f" % (b))
		return;
	
	def myspp(m,p,q):
		sound=m
		sourcerun=p 
		path=q
		objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
		print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
		z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
		z2=z1.strip().split()
		z3=int(z2[13]) # will be the integer number 10
		z4=float(z2[14]) # will be the floating point number 8.3
		db= binom.rvs(n=10,p=z4,size=10000)
		a=np.array(db)
		b=np.mean(a)*100/10
		return b
	
	def myspgend(m,p,q):
		sound=m
		sourcerun=p 
		path=q
		objects= run_file(sourcerun, -20, 2, 0.3, "yes",sound,path, 80, 400, 0.01, capture_output=True)
		print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
		z1=str( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
		z2=z1.strip().split()
		z3=float(z2[8]) # will be the integer number 10
		z4=float(z2[7]) # will be the floating point number 8.3 
		
		if z4<=114:
			g=101
			j=3.4
		elif z4>114 and z4<=135:
			g=128
			j=4.35
		elif z4>135 and z4<=163:
			g=142
			j=4.85
		elif z4>163 and z4<=197:
			g=182
			j=2.7
		elif z4>197 and z4<=226:
			g=213
			j=4.5
		elif z4>226:
			g=239
			j=5.3
		else:
			print("Voice not recognized")
			exit()
		def teset(a,b,c,d):
			d1=np.random.wald(a, 1, 1000)
			d2=np.random.wald(b,1,1000)
			d3=ks_2samp(d1, d2)
			c1=np.random.normal(a,c,1000)
			c2=np.random.normal(b,d,1000)
			c3=ttest_ind(c1,c2)
			y=([d3[0],d3[1],abs(c3[0]),c3[1]])
			return y
		nn=0
		mm=teset(g,j,z4,z3)
		while (mm[3]>0.05 and mm[0]>0.04 or nn<5):
		   mm=teset(g,j,z4,z3)
		   nn=nn+1
		nnn=nn
		if mm[3]<=0.09:
			mmm=mm[3]
		else:
			mmm=0.35
		if z4>97 and z4<=114:
			print("a Male, mood of speech: Showing no emotion, normal, p-value/sample size= :%.2f" % (mmm), (nnn)) 
		elif z4>114 and z4<=135:
			print("a Male, mood of speech: Reading, p-value/sample size= :%.2f" % (mmm), (nnn))
		elif z4>135 and z4<=163:
			print("a Male, mood of speech: speaking passionately, p-value/sample size= :%.2f" % (mmm), (nnn))
		elif z4>163 and z4<=197:
			print("a female, mood of speech: Showing no emotion, normal, p-value/sample size= :%.2f" % (mmm), (nnn))
		elif z4>197 and z4<=226:
			print("a female, mood of speech: Reading, p-value/sample size= :%.2f" % (mmm), (nnn))
		elif z4>226 and z4<=245:
			print("a female, mood of speech: speaking passionately, p-value/sample size= :%.2f" % (mmm), (nnn))
		else:
			print("Voice not recognized")

	AUDIO_FILE = (pa0)
	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
		audio = r.record(source,duration=15) # read the entire audio file
	try:
		trans=r.recognize_google(audio,language = "en-US")
		#trans=r.recognize_sphinx(audio, language="en-US")
		#print("The audio file contains: " + a)
	except sr.UnknownValueError:
		print("Machine could not understand the audio")
	except sr.RequestError as e:
		print("Not good internet connection; {0}".format(e))

	b=detect_langs(trans)
	c=detect(trans)
	now=len(trans.split())
	
	if not c=='en'or now<10:
		input("No further result, did you speak in English or the machine heard unnatural-sounding speech Try again,Press any key to exit.")
		exit()
	

	for soundi in files:
		objects= run_file(pa8, -20, 2, 0.3, "yes", soundi, pa00, 80, 400, 0.01, capture_output=True)
		#print (objects[0]) # This will print the info from the sound object, and objects[0] is a parselmouth.Sound object
		z1=( objects[1]) # This will print the info from the textgrid object, and objects[1] is a parselmouth.Data object with a TextGrid inside
		z3=z1.strip().split()
		z2=np.array([z3])
		result_array=np.append(result_array,[z3], axis=0)
		
	np.savetxt(pa1,result_array, fmt='%s',delimiter=',')

	#Data and features analysis 
	df = pd.read_csv(pa1,
						 names = ['avepauseduratin','avelongpause','speakingtot','avenumberofwords','articulationrate','inpro','f1norm','mr','q25',
								  'q50','q75','std','fmax','fmin','vowelinx1','vowelinx2','formantmean','formantstd','nuofwrds','npause','ins',
								  'fillerratio','xx','xxx','totsco','xxban','speakingrate'],na_values='?')

	scoreMLdataset=df.drop(['xxx','xxban'], axis=1)
	scoreMLdataset.to_csv(pa7, header=False,index = False)
	newMLdataset=df.drop(['avenumberofwords','f1norm','inpro','q25','q75','vowelinx1','nuofwrds','npause','xx','totsco','xxban','speakingrate','fillerratio'], axis=1)
	newMLdataset.to_csv(pa5, header=False,index = False)
	namess=nms = ['avepauseduratin','avelongpause','speakingtot','articulationrate','mr',
								  'q50','std','fmax','fmin','vowelinx2','formantmean','formantstd','ins',
								  'xxx']
	df1 = pd.read_csv(pa5,
							names = namess)
	df33=df1.drop(['xxx'], axis=1)
	array = df33.values
	array=np.log(array)
	x = array[:,0:13]

	print(" ")
	print(" ")
	print("===========================================")
	if ran=="jp":
		levv=45
	elif ran=="ln":
		levv=65
	else:
		levv=80
	p=pa0
	c=pa9
	a=pa00
	bi=myspp(p,c,a)
	if bi<levv:
		mysppron(p,c,a)
		input("Try again, unnatural-sounding speech detected. No further result. Press any key to exit.")
		exit()
	
	mysppron(p,c,a)
	myspgend(p,c,a)
	
	print(" ")
	print(" ")
	print("====================================================================================================")
	print("HERE ARE THE RESULTS, your spoken language level (speaking skills).")
	print("a: just started, a1: beginner, a2: elementary, b1: intermediate, b2: upper intermediate, c: master") 
	print("====================================================================================================")

	def resulti(m,n):
		jj=m
		ii=n
		if jj=="a":
				ascore=ii
		else:
				ascore=ii/5
		if jj=="a1":
				a1score=ii
		else:
				a1score=ii/5
		if jj=="a2":
				a2score=ii
		else:
				a2score=ii/5
		if jj=="b1":
				b1score=ii
		else:
				b1score=ii/5
		if jj=="b2":
				b2score=ii
		else:
				b2score=ii/5
		if jj=="c":
				cscore=ii
		else:
				cscore=ii/5
		matx=np.array([ascore, a1score,a2score,b1score,b2score,cscore])
		scovec=np.power(matx, 2)
		return scovec

	filename=pathy+"/"+"dataset"+"/"+"essen"+"/"+"CART_model.sav"

	model = pickle.load(open(filename, 'rb'))
	predictionsCA = model.predict(x)
	ca=resulti(predictionsCA,0.7)
	print("Judge 70    ",predictionsCA)

	#filename=pathy+"/"+"essen"+"/"+"ETC_model.sav"

	#model = pickle.load(open(filename, 'rb'))
	#predictions = model.predict(x)
	#print("70% accuracy    ",predictions)

	filename=pathy+"/"+"dataset"+"/"+"essen"+"/"+"KNN_model.sav"

	model = pickle.load(open(filename, 'rb'))
	predictionsKN = model.predict(x)
	kn=resulti(predictionsKN,0.67)
	print("Judge 67    ",predictionsKN)

	filename=pathy+"/"+"dataset"+"/"+"essen"+"/"+"LDA_model.sav"

	model = pickle.load(open(filename, 'rb'))
	predictionsLD = model.predict(x)
	ld=resulti(predictionsLD,0.6)
	print("Judge 60    ",predictionsLD)

	filename=pathy+"/"+"dataset"+"/"+"essen"+"/"+"LR_model.sav"

	model = pickle.load(open(filename, 'rb'))
	predictionsLR = model.predict(x)
	lr=resulti(predictionsLR,0.68)
	print("Judge 68    ",predictionsLR)

	filename=pathy+"/"+"dataset"+"/"+"essen"+"/"+"NB_model.sav"

	model = pickle.load(open(filename, 'rb'))
	predictionsNB = model.predict(x)
	nb=resulti(predictionsNB,0.61)
	print("Judge 61    ",predictionsNB)

	#filename=pathy+"/"+"essen"+"/"+"PCA_model.sav"

	#model = pickle.load(open(filename, 'rb'))
	#predictions = model.predict(x)
	#print("70% accuracy    ",predictions)

	#filename=pathy+"/"+"essen"+"/"+"RFE_model.sav"

	#model = pickle.load(open(filename, 'rb'))
	#predictions = model.predict(x)
	#print("70% accuracy    ",predictions)

	filename=pathy+"/"+"dataset"+"/"+"essen"+"/"+"SVN_model.sav"

	model = pickle.load(open(filename, 'rb'))
	predictionsSV = model.predict(x)
	sv=resulti(predictionsSV,0.72)
	print("Judge 72    ",predictionsSV)

	resAlt1=ca+kn+ld+lr+nb+sv
	resAlt2=np.power(resAlt1,0.5)
	#vall=np.amax(resAlt2)
	resAlt2=np.array(resAlt2)
	vall=np.amax(resAlt2)
	inx = np.where(resAlt2==vall)
	if vall>1:
		vall=2-vall
	else:
		vall=vall

	mom=np.array(["a","a1","a2","b1","b2","c"])
	resA=mom[inx]
	momm=np.where(mom==inx)
	print(" ")
	print(" ")
	print("===========================================")
	print("Your sprosodic fluency level could be at  ",resA," with a confidence level of   ", "%.2f" % vall)
	print(" ")
	print("===========================================")
		
except:
	print(" ")
	print(" ")
	print("===========================================")
	print("Try again, noisy background or unnatural-sounding speech detected. No result.")
	exit()
def percentage1(count, total):
   return 100 * count / total 
def percentage2(xxx):
   return 100 * xxx 

class SentimentAnalyzer(object):
    """
    A Sentiment Analysis tool based on machine learning approaches.
    """

    def __init__(self, classifier=None):
        self.feat_extractors = defaultdict(list)
        self.classifier = classifier

    def all_words(self, documents, labeled=None):
       """
        Return all words/tokens from the documents (with duplicates).
        :param documents: a list of (words, label) tuples.
        :param labeled: if `True`, assume that each document is represented by a
            (words, label) tuple: (list(str), str). If `False`, each document is
            considered as being a simple list of strings: list(str).
        :rtype: list(str)
        :return: A list of all words/tokens in `documents`.
        """
       all_words = []
       if labeled is None:
           labeled = documents and isinstance(documents[0], tuple)
       if labeled == True:
           for words, sentiment in documents:
               all_words.extend(words)
       elif labeled == False:
           for words in documents:
               all_words.extend(words)
       return all_words


    def apply_features(self, documents, labeled=None):
        """
        Apply all feature extractor functions to the documents. This is a wrapper
        around `nltk.classify.util.apply_features`.

        If `labeled=False`, return featuresets as:
            [feature_func(doc) for doc in documents]
        If `labeled=True`, return featuresets as:
            [(feature_func(tok), label) for (tok, label) in toks]

        :param documents: a list of documents. `If labeled=True`, the method expects
            a list of (words, label) tuples.
        :rtype: LazyMap
        """
        return apply_features(self.extract_features, documents, labeled)


    def unigram_word_feats(self, words, top_n=None, min_freq=0):
        """
        Return most common top_n word features.

        :param words: a list of words/tokens.
        :param top_n: number of best words/tokens to use, sorted by frequency.
        :rtype: list(str)
        :return: A list of `top_n` words/tokens (with no duplicates) sorted by
            frequency.
        """
        # Stopwords are not removed
        unigram_feats_freqs = FreqDist(word for word in words)
        return [
            w
            for w, f in unigram_feats_freqs.most_common(top_n)
            if unigram_feats_freqs[w] > min_freq
        ]


    def bigram_collocation_feats(
        self, documents, top_n=None, min_freq=3, assoc_measure=BigramAssocMeasures.pmi
    ):
        """
        Return `top_n` bigram features (using `assoc_measure`).
        Note that this method is based on bigram collocations measures, and not
        on simple bigram frequency.

        :param documents: a list (or iterable) of tokens.
        :param top_n: number of best words/tokens to use, sorted by association
            measure.
        :param assoc_measure: bigram association measure to use as score function.
        :param min_freq: the minimum number of occurrencies of bigrams to take
            into consideration.

        :return: `top_n` ngrams scored by the given association measure.
        """
        finder = BigramCollocationFinder.from_documents(documents)
        finder.apply_freq_filter(min_freq)
        return finder.nbest(assoc_measure, top_n)


    def classify(self, instance):
        """
        Classify a single instance applying the features that have already been
        stored in the SentimentAnalyzer.

        :param instance: a list (or iterable) of tokens.
        :return: the classification result given by applying the classifier.
        """
        instance_feats = self.apply_features([instance], labeled=False)
        return self.classifier.classify(instance_feats[0])


    def add_feat_extractor(self, function, **kwargs):
        """
        Add a new function to extract features from a document. This function will
        be used in extract_features().
        Important: in this step our kwargs are only representing additional parameters,
        and NOT the document we have to parse. The document will always be the first
        parameter in the parameter list, and it will be added in the extract_features()
        function.

        :param function: the extractor function to add to the list of feature extractors.
        :param kwargs: additional parameters required by the `function` function.
        """
        self.feat_extractors[function].append(kwargs)


    def extract_features(self, document):
        """
        Apply extractor functions (and their parameters) to the present document.
        We pass `document` as the first parameter of the extractor functions.
        If we want to use the same extractor function multiple times, we have to
        add it to the extractors with `add_feat_extractor` using multiple sets of
        parameters (one for each call of the extractor function).

        :param document: the document that will be passed as argument to the
            feature extractor functions.
        :return: A dictionary of populated features extracted from the document.
        :rtype: dict
        """
        all_features = {}
        for extractor in self.feat_extractors:
            for param_set in self.feat_extractors[extractor]:
                feats = extractor(document, **param_set)
            all_features.update(feats)
        return all_features


    def train(self, trainer, training_set, save_classifier=None, **kwargs):
        """
        Train classifier on the training set, optionally saving the output in the
        file specified by `save_classifier`.
        Additional arguments depend on the specific trainer used. For example,
        a MaxentClassifier can use `max_iter` parameter to specify the number
        of iterations, while a NaiveBayesClassifier cannot.

        :param trainer: `train` method of a classifier.
            E.g.: NaiveBayesClassifier.train
        :param training_set: the training set to be passed as argument to the
            classifier `train` method.
        :param save_classifier: the filename of the file where the classifier
            will be stored (optional).
        :param kwargs: additional parameters that will be passed as arguments to
            the classifier `train` function.
        :return: A classifier instance trained on the training set.
        :rtype:
        """
        print("Training classifier")
        self.classifier = trainer(training_set, **kwargs)
        if save_classifier:
            save_file(self.classifier, save_classifier)

        return self.classifier


    def evaluate(
        self,
        test_set,
        classifier=None,
        accuracy=True,
        f_measure=True,
        precision=True,
        recall=True,
        verbose=False,
    ):
        """
        Evaluate and print classifier performance on the test set.

        :param test_set: A list of (tokens, label) tuples to use as gold set.
        :param classifier: a classifier instance (previously trained).
        :param accuracy: if `True`, evaluate classifier accuracy.
        :param f_measure: if `True`, evaluate classifier f_measure.
        :param precision: if `True`, evaluate classifier precision.
        :param recall: if `True`, evaluate classifier recall.
        :return: evaluation results.
        :rtype: dict(str): float
        """
        if classifier is None:
            classifier = self.classifier
        print("Evaluating {0} results...".format(type(classifier).__name__))
        metrics_results = {}
        if accuracy == True:
            accuracy_score = eval_accuracy(classifier, test_set)
            metrics_results['Accuracy'] = accuracy_score

        gold_results = defaultdict(set)
        test_results = defaultdict(set)
        labels = set()
        for i, (feats, label) in enumerate(test_set):
            labels.add(label)
            gold_results[label].add(i)
            observed = classifier.classify(feats)
            test_results[observed].add(i)

        for label in labels:
            if precision == True:
                precision_score = eval_precision(
                    gold_results[label], test_results[label]
                )
                metrics_results['Precision [{0}]'.format(label)] = precision_score
            if recall == True:
                recall_score = eval_recall(gold_results[label], test_results[label])
                metrics_results['Recall [{0}]'.format(label)] = recall_score
            if f_measure == True:
                f_measure_score = eval_f_measure(
                    gold_results[label], test_results[label]
                )
                metrics_results['F-measure [{0}]'.format(label)] = f_measure_score

        # Print evaluation results (in alphabetical order)
        if verbose == True:
            for result in sorted(metrics_results):
                print('{0}: {1}'.format(result, metrics_results[result]))

        return metrics_results


	
text = trans
txt=trans.split()
lent=len(word_tokenize(trans))
SentimentAnalyzer(text)
fe=pathy+"/"+"dataset"+"/"+"essen"+"/"+"my_classifier.pickle"
f = open(fe, 'rb')
classifier = pickle.load(f)
qualityy=TextBlob(text)
obsub=qualityy.sentiment
if obsub[1]>0.5:
        print("Your speech sounds less logically structured by %:   ", "%.2f" % ((obsub[1]-0.5)*100))
else:
        print("Your speech sounds more logically structured by %:   ", "%.2f" % ((1-obsub[1])*100))
f.close()
quaa=qualityy.words
def lexical_diversity(a):
    return len(set(trans))/len(trans)
v=percentage2(lexical_diversity(trans))
if v>=0.145*100 and v<0.231*100 :
        langscore="b2"
elif v>=0.231*100:
        langscore="c"
elif v>=0.121*100 and v<0.145*100:
        langscore="b1"
elif v<0.121*100 and v>=0.09*100:
        langscore="a2"
else:
        langscore="a1"  

tokenized_text=word_tokenize(text)
#print(tokenized_text)
tokenized_sent=sent_tokenize(text)
stop_words=set(stopwords.words("english"))
filtered_sent=[]
for w in tokenized_text:
        if w not in stop_words:
                filtered_sent.append(w)
#print("Filterd Sentence:",filtered_sent)
filtered_sent=filtered_sent
ps = PorterStemmer()
stemmed_words=[]
for w in filtered_sent:
        stemmed_words.append(ps.stem(w))
#print("Stemmed Sentence:",stemmed_words)
def lexical_diversity(a):
        return len(set(a))/len(a)
def lexical_richness(a,b):
        return len(a)/len(b)
vio=percentage2(lexical_diversity(tokenized_text))
vocano=lexical_richness(filtered_sent,tokenized_text)
if vocano>=0.4 and vocano<0.5:
        langscoree="b2"
elif vocano>=0.5:
        langscoree="c"
elif vocano>=0.3 and vocano<0.4:
        langscoree="b1"
elif vocano<0.3 and vocano>=0.2:
        langscoree="a2"
else:
        langscoree="a1" 

vvv=percentage2(vocano)
#print(len(set(filtered_sent)))
#print(len(trans))
#print(len(tokenized_text))
vocab = filtered_sent
long_words = [w for w in vocab if len(w) >10]
soso=sorted(long_words)
mesu=len(soso)/len(vocab)
if mesu>0.01:
        sayy="you used sofisticated words"
else:
        sayy=" "

if resA=="c":
        if langscore=="c" or langscore=="b2":
                ai="c"
        elif langscore=="b1" or langscore=="a2":
                ai="b2"
        elif langscore=="a1":
                ai="b1"
        else:
                ai="b1"

if resA=="b2":
        if langscore=="c" or langscore=="b2":
                ai="b2"
        elif langscore=="b1" or langscore=="a2":
                ai="b2"
        elif langscore=="a1":
                ai="b1"
        else:
                ai="b1"
if resA=="b1":
        if langscore=="c" or langscore=="b2":
                ai="b2"
        elif langscore=="b1" or langscore=="a2":
                ai="b1"
        elif langscore=="a1":
                ai="b1"
        else:
               ai="a2" 
if resA=="a2":
        if langscore=="c" or langscore=="b2":
                ai="b1"
        elif langscore=="b1" or langscore=="a2":
                ai="a2"
        elif langscore=="a1":
                ai="a2"
        else:
                ai="a1"                                 
if resA=="a1" or resA=="a":
        if langscore=="c" or langscore=="b2":
                ai="a1"
        elif langscore=="b1" or langscore=="a2":
                ai="a"
        elif langscore=="a1":
                ai="a"
        else:
                ai="a" 
if ai=="c":
        iBT="26-30"
if ai=="b2":
        iBT="18-25"
if ai=="b1":
        iBT="10-17"
if ai=="a2":
        iBT="less than 9"

print(" ")
print("===========================================")
print("the lexical richness in specific contexts; confidence level %:",round(v,1))
print("the lexical richness in in ordinary conversation contexts; confidence level %:",round(vio,1))
print("the lexical diversity; confidence level %:  ",round(vvv,1))
print(sayy)
print(" ")
print("your use of academic language skill could be at   ", langscore)
print("your use of general language skill could be at   ", langscoree)
print(" ")
print("===========================================")
print("your TOEFL iBT score could be in this range   ", iBT)
print("===========================================")
fini=input("The general assessment is DONE, press f to continue for a specific assessment or any other key to terminate the programe:   ")

if fini=='f':
        s1 = input("Enter key word-1: ")
        s2 = input("Enter key word-2: ")
        s3 = input("Enter key word-3: ")
        v1=a.count(s1)
        v2=a.count(s2)
        v3=a.count(s3)
        ran=[v1,v2,v3]
        def totscore(numList):
                totscore=0
                for i in numList:
                        if i==0:
                                score=-1
                        else:
                                score=i
                        totscore=totscore+score
                return totscore
        print(totscore(ran))
        print(v1)
        print(v2)
        print(v3)
        input("Done,press any key to terminate the program")
else:
        exit()
