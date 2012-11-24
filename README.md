tf-idf-emr
==========

TF*IDF algorithm for the Elastic MapReduce platform.

* Usage: `python driver.py input_file.txt output_file.txt`
* To deploy the script on Amazon EMR, add the `-emr` option.
* Look at `sentences.txt` for an example of the input format:

    "doc_id" ["sentence_1", ..., "sentence_n"]

> Specify your EMR configuration with `export MRJOB CONF=/home/you/yourpath/fileName.txt`.