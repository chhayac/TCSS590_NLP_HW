## Homework Submission # 1 
### TCSS590: Natural Language Processing 
### Winter 2018 
#### Chhaya Choudhary

Write a function, that given a sequence of three words (w1,w2,w3), would compute the probability of third word using trigram language model p(w3|w1,w2). If you're using log-probabilities, use base 2 for computing logs.

The program implements tri-gram language model with add-one smoothing.

Program can be run from command line as: 

__python <trigram_model.py> <dataset_path> \<word1\> \<word2\> \<word3\>__
  
where dataset_path contains folders Pos and Neg having positive review files and negative review files.
word1, word2 and word3 are candidate tokens for the model. The output represents probability of word3 appearing after sequence of word1 and word2.

#### Test cases:

python trigram_model.py ..\HW1 hello world yahoo

Probability of [ yahoo ] appearing after [ hello ] and [ world ] is 0.00022517451024544022

python trigram_model.py ..\HW1 ruben santiago hudson

Probability of [ hudson ] appearing after [ ruben ] and [ santiago ] is 0.0013492241960872497

python trigram_model.py ..\HW1 three ten year

Probability of [ year ] appearing after [ three ] and [ ten ] is 0.0006752194463200541

python trigram_model.py ..\HW1 vincent price peter

Probability of [ peter ] appearing after [ vincent ] and [ price ] is 0.0006749156355455568

python trigram_model.py ..\HW1 albert finney tom

Probability of [ tom ] appearing after [ albert ] and [ finney ] is 0.0011233430689732643