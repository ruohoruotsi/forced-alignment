import gzip
import os
import pickle

CORPUS_DIR = "D:/code/ip8/corpora"


def save_corpus(corpus_entries, filename, gzip=False):
    corpus_file = os.path.join(CORPUS_DIR, filename)
    corpus_dir = os.path.dirname(corpus_file)
    if not os.path.exists(corpus_dir):
        os.makedirs(corpus_dir)

    if gzip:
        corpus_file += '.gz'
        with gzip.open(corpus_file, 'wb') as corpus:
            corpus.write(pickle.dumps(corpus_entries))
    else:
        with open(corpus_file, 'wb') as corpus:
            pickle.dump(corpus_entries, corpus)


def load_corpus(filename):
    corpus_file = os.path.join(CORPUS_DIR, filename);
    if filename.endswith('.gz'):
        with gzip.open(corpus_file, 'rb') as corpus:
            corpus_entries = pickle.loads(corpus.read())
    else:
        with open(corpus_file, 'rb') as corpus:
            corpus_entries = pickle.load(corpus)
    return corpus_entries