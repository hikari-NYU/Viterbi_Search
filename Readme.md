###Viterbi Search Experiment
####Weicheng Ma
-----

######Overview 
* This is a part-of-speech tagger based on Brown Corpus. 
* Hidden Markov Model generated by another program used. 
* For here just viterbi algorithm part. 
* @Input:String; Raw input from the user, a sentence. 
* @Output:String; A string of taggs coherent with the words in place. 


######Usage 
 0. Python 2.7 with NLTK and JSON required. 
 1. Put the dictionary files under the same folder as viterbi.py. 
 2. Run 'python viterbi.py'. 
 3. Input the sentence to tag when asked. 
 4. See the result string. 


######Methods 

FORWARD:
---------------------------------------------------------------------------
 The transition and emition probabilities used here are based on Brown corpus. 
 The process of finding the optimistic path is as follows: 
 1. Build up an empty map with the rows corresponding to tags and columns to words. 
 2. Initialize the first column, fill only the start symbol with probability 1.0. 
 3. For the next row, calculate the probabilities for each pair of values by adding 
 up the former probability and transitionemission probabilities. 
 4. Record the index of tags also. 
 5. Repeat 3-4 till the end of sentence. 
 6. Fill the end symbol in the last column only. 
 
BACKWARD:
--------------------------------------------------------------------------
 6. Start from the end symbol, trace back using the recorded indexes. 
 7. Collect and return. 