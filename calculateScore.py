from mrjob.job import MRJob
from mrjob.protocol import JSONProtocol
from math import log, fabs

class calculateScore(MRJob):
 
  INPUT_PROTOCOL = JSONProtocol
  
  def mapper(self, word_doc_i, triplet):
    word, doc, i = word_doc_i
    n, N, m = [float(x) for x in triplet]
    tf, idf = n/N, log(1.0/(1.0 + m))
    yield (doc, i), fabs(tf / idf)

  def reducer(self, doc_i, tf_idfs):
    yield doc_i, sum(list(tf_idfs))

if __name__ == '__main__':
 calculateScore.run()