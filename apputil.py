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
        self.term_dict = defaultdict(list)

    def get_term_dict(self):

        '''Building a function to tokenize over the words and create a term dictionary'''
        
        words = self.corpus.split()

        # Build term dictionary by iteration through words
        for i in range(len(words) - 1):
            current_word = words[i]
            next_word = words[i + 1]
            self.term_dict[current_word].append(next_word)

        return self.term_dict
        

    def generate(self, seed_term=None, term_count=15):

        '''Building function for sentence generation'''

        # Confirm populated term_dict
        if not self.term_dict:
            self.get_term_dict()

        current_word = seed_term or random.choice(list(self.term_dict.keys()))
        sent = [current_word]

        # generate sentence
        for _ in range(term_count -1):
            followers = self.term_dict[current_word]
            if not followers:
                break
            current_word = random.choice(followers)
            sent.append(current_word)

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




