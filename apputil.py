from collections import defaultdict
import numpy as np
import random

class MarkovText(object):
    '''Building a class MarkovText that includes functions to generate a dictionary containing key value pairs,
      where the keys represent tokens (words) and the values represent their possible subsequent states within a corpus.
    '''
    def __init__(self, corpus):

        '''Creating a function that assigns a corpus and ensures that each key 
           in the resulting dictionary is automatically initialized with a list as its value.
        '''
        self.corpus = corpus
        self.term_dict = None

    def get_term_dict(self):

        '''Building a function to tokenize over the words and create a term dictionary'''
        
        corpus = self.corpus if isinstance(self.corpus, str) else ""
        # white space tokenization
        tokens = corpus.split()

        # Build token and list next tokens
        d = defaultdict(list)
        for i in range(len(tokens) - 1):
            d[tokens[i]].append(tokens[i + 1])

        if tokens:
            _ = d[tokens[-1]]  

        self.term_dict = dict(d)

        return self.term_dict
        

    def generate(self, seed_term=None, term_count=15):

        '''Building function for sentence generation'''

        # Confirm populated term_dict
        if not self.term_dict:
            self.get_term_dict()

        # if term_dic is empty
        if not self.term_dict:
            raise ValueError("Corpus is empty or could not generate term dictionary.")

        if seed_term is not None:
            if seed_term not in self.term_dict:
                raise ValueError(f"Seed term '{seed_term}' not found in corpus.")
            current_word = seed_term
        else:
             current_word = random.choice(list(self.term_dict.keys()))
    
        sent = [current_word]

        # generate sentence
        for _ in range(term_count -1):
            followers = self.term_dict.get(current_word, [])
            if not followers:
                
                current_word = np.random.choice(list(self.term_dict.keys()))
                sent.append(cur)
                continue
            nxt = np.random.choice(followers)
            sent.append(nxt)
            current_word = nxt

        return ' '.join(sent)
    
# set corpus 
corpus = (
"Healing comes from taking responsibility: to realize that it is you - and no one else - "
"that creates your thoughts, your feelings, and your actions."
)

# create Markov object and term dictionary
text_gen = MarkovText(corpus)
term_dic = text_gen.get_term_dict()
text_gen.generate(term_count = 12)




