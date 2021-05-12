import json
import pickle
import pathlib




class Stopwords(object):

    def __init__(self):
        self.multistopwords = pickle.load(open(pathlib.Path(__file__).parent.joinpath('stopwords.pkl'), 'rb'))


    def languages(self):
        return self.multistopwords.keys()

    def setlang(self, lang='chinese'):
        self.stopwords_set = self.multistopwords[lang]
        print('set language to {}'.format(lang))

    def stopwords(self):
        return self.stopwords_set


    def add(self, word):
        self.stopwords_set.add(word)

    def remove(self, word):
        if word not in self.stopwords_set:
            return
        self.stopwords_set.remove(word)

    def contains(self, word):
        return True if word in self.stopwords_set else False

    def size(self):
        return len(self.stopwords_set)


    def download(self, path):
        with open(path, mode='wt', encoding='utf8') as fout:
            for w in sorted(self.stopwords_set):
                fout.write(w + '\n')

