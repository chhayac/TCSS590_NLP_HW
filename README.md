## Homework Submission # 1 
### TCSS590: Natural Language Processing 
### Winter 2018 
#### Chhaya Choudhary

Write a function, that given a sequence of three words (w1,w2,w3), would compute the probability of third word using trigram language model p(w3|w1,w2). If you're using log-probabilities, use base 2 for computing logs.

Program can be run from command line as: 

__python <trigram_model.py> <filepath> \<word1\> \<word2\> \<word3\>__
  
where filepath contains file having combined data of positive files and negative files in movie review dataset
word1, word2 and word3 are candidate tokens for the model. The output represents probability of word3 appearing after sequence of word1 and word2.

#### Test cases:

python trigram_model.py combined_file.txt hello world yahoo

Probability of [ yahoo ] appearing after [ hello ] and [ world ] is 0.00022527596305474206

python trigram_model.py HW1\combined_file.txt ruben santiago hudson

Probability of [ hudson ] appearing after [ ruben ] and [ santiago ] is 0.00041291291291291294

python trigram_model.py HW1\combined_file.txt three ten year

Probability of [ year ] appearing after [ three ] and [ ten ] is 0.00045045045045045046

python trigram_model.py HW1\combined_file.txt vincent price peter

Probability of [ peter ] appearing after [ vincent ] and [ price ] is 0.00033783783783783786

python trigram_model.py HW1\combined_file.txt albert finney tom

Probability of [ tom ] appearing after [ albert ] and [ finney ] is 0.0003153153153153153
