from collections import defaultdict


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

        # your code here ...

        self.term_dict = {}

        return None


    def generate(self, seed_term=None, term_count=15):

        # your code here ...

        return None