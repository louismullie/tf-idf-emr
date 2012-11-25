tf-idf-emr
==========

**Usage**

TF*IDF algorithm for the Elastic MapReduce platform.

* Usage: `python driver.py input_file.txt output_file.txt`
* To deploy the script on Amazon EMR, add the `-emr` option.
* Look at `sentences.txt` for an example of the input format:

   `"doc_id" ["sentence_1", ..., "sentence_n"]`

> Specify your EMR configuration with `export MRJOB_CONF=/home/you/yourpath/fileName.txt`.

**Reference**

Wan J, Yu W, Xu X. Design and Implementation of Distributed Document  
Clustering Based on MapReduce. Proceedings of the ISCSCT 2009, pp. 278-280. ([PDF](http://www.academypublisher.com/proc/iscsct09/papers/iscsct09p278.pdf))

