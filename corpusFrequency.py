from mrjob.job import MRJob
from mrjob.protocol import JSONProtocol
import itertools

class corpusFrequency(MRJob):
 
  INPUT_PROTOCOL = JSONProtocol
  
  def mapper(self, word_doc_i, n_N):
    word, doc, i, n, N = word_doc_i + n_N
    yield word, (doc, i, n, N, 1)
  
  def reducer(self, word, info):
    info = list(info)
    m = len(info)
    for element in info:
      doc, i, n, N = element[:4]
      yield (word, doc, i), (n, N, m)

if __name__ == '__main__':
 corpusFrequency.run()