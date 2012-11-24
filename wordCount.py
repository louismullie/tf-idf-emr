from mrjob.job import MRJob
from mrjob.protocol import JSONProtocol

class wordCount(MRJob):
 
  INPUT_PROTOCOL = JSONProtocol

  def mapper(self, word_doc_i, n):
    word, doc, i = word_doc_i
    yield doc, (i, word, n)

  def reducer(self, doc, i_word_ns):
    N, S, i_word_ns = 0, {}, list(i_word_ns)
    for i_word_n in i_word_ns:
      i, word, n = i_word_n
      N += n
      for i_word_n2 in i_word_ns:
        i2, word2, n2 = i_word_n2
        if n == n2 and word2 == word:
          try: S[i2] += 1
          except: S[i2] = 1
    for i_word_n in i_word_ns:
      i, word, n = i_word_n
      yield (word, doc, i), (n, N)

if __name__ == '__main__':
 wordCount.run()