from mrjob.job import MRJob
from mrjob.protocol import JSONProtocol
import nltk
import re

class wordFrequency(MRJob):
 
 INPUT_PROTOCOL = JSONProtocol

 def __init__(self, *args, **kwargs):
   super(wordFrequency, self).__init__(*args, **kwargs)
   self.freqs = {}
   self.stop = nltk.corpus.stopwords.words('english')
   
 def mapper(self, doc, sentences):
   for i, sentence in enumerate(sentences):
     words = self.tokenize(sentence)
     for j, word in enumerate(words):
       if word in self.stop: continue
       k = (word, doc, str(i))
       try: self.freqs[k] += 1
       except: self.freqs[k] = 1

 def tokenize(self, txt):
   p = re.compile(r"\d+|[-'a-z]+|[ ]+|\s+|[.,]+|\S+", re.I)
   slice_starts = [m.start() for m in p.finditer(txt)] + [None]
   r = [txt[s:e] for s, e in zip(slice_starts, slice_starts[1:])]
   return r

 def mapper_final(self):
   for key in self.freqs.iterkeys():
     yield key, int(self.freqs[key])

 def reducer(self, key, counts):
   total = 0
   for count in list(counts):
     total += count
   yield key, total


if __name__ == '__main__':
 wordFrequency.run()
