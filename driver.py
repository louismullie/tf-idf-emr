from mrjob.job import MRJob
from wordFrequency import wordFrequency
from wordCount import wordCount
from corpusFrequency import corpusFrequency
from calculateScore import calculateScore
import re, json; from sys import argv, stdout

# Helper method to run a job and stream output.
def run_job(klass, input_file, output_file):
  args = [input_file]
  if not LOCAL: args += ['-r', 'emr']
  inst = klass(args=args)
  with inst.make_runner() as runner:
    runner.run()
    file = open(output_file, 'w+')
    for line in runner.stream_output():
      file.write(line)
    file.close()

# Make sure we got proper arguments.
if len(argv) < 3 or len(argv) > 5:
  exit("Usage: python driver.py " + \
  "[input file] [output file] [options]")

# Determine if we're running locally or on EMR.
LOCAL = not (len(argv) > 3 and argv[3] == '-emr')

# Output all logging information to STDOUT.
MRJob.set_up_logging(verbose=True, stream=stdout)

# Run all the MapReduce workers sequentially.
run_job(wordFrequency, argv[1], 'frequencies.txt')
run_job(wordCount, 'frequencies.txt', 'counts.txt')
run_job(corpusFrequency, 'counts.txt', 'corpus.txt')
run_job(calculateScore, 'corpus.txt', argv[2])