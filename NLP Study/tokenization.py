from nltk.tokenize import sent_tokenize, word_tokenize 
  
text = "Natural language processing (NLP) is a field of computer science, artificial intelligence and computational linguistics concerned with the interactions between computers and human (natural) languages, and, in particular, concerned with programming computers to fruitfully process large natural language corpora. Challenges in natural language processing frequently involve natural language understanding, natural language generation (frequently from formal, machine-readable logical forms), connecting language and machine perception, managing human-computer dialog systems, or some combination thereof."
  
print(sent_tokenize(text)) 
print(word_tokenize(text))


# Tokenization

'''
sentence tokenization using sent_tokenize

The sent_tokenize function uses an instance of PunktSentenceTokenizer from 
the nltk.tokenize.punkt module, which is already been trained and thus very 
well knows to mark the end and beginning of sentence at what characters and 
punctuation.  
'''
from nltk.tokenize import sent_tokenize
text = "Hello everyone. Welcome to GeeksforGeeks. You are studying NLP article."
sent_tokenize(text)

'''
Sentence tokenization using PunktSentenceTokenizer
'''
# Loading PunktSentenceTokenizer using English pickle file
import nltk
tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')
tokenizer.tokenize(text) # should be the same as above

'''
Word tokenization using word_tokenize

word_tokenize() function is a wrapper function that calls tokenize() on an 
instance of the TreebankWordTokenizer class. 
'''
from nltk.tokenize import word_tokenize
text = "Hello everyone. Welcome to GeeksforGeeks."
word_tokenize(text)

'''
Word tokenization using TreebankWordTokenizer

You'll notice that output is not same as above, punctuation is handled weird.
You should decide what to do with punctuation in preprocessing/ text normalization
before tokenization. 
'''
from nltk.tokenize import TreebankWordTokenizer
tokenizer = TreebankWordTokenizer()
tokenizer.tokenize(text)

'''
Word tokenization using WordPunctTokenizer 

Splits words based on punctuation boundaries. Each punctuation is marked as a
separate token.
'''
from nltk.tokenize import WordPunctTokenizer
tokenizer = WordPunctTokenizer()
tokenizer.tokenize("Let's see how it's working.")

'''
Word tokenization using regular expression
'''




from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
text = "Let's see how it's working."
tokenizer.tokenize(text)

'''
More libraries for tokenization:

SpaCy - robust tokenization capabilities 
BERT Tokenizer - uses WordPiece tokenizer (a type of subword tokenizer), allows use of regex for further customization
Byte-Pair Encoding - a subword tokenization scheme that iteratively merges the most frequent pairs of consecutive bytes/chars in a given corpus
Sentence Piecen- subword tokenization alg, iteratively merges frequent sequences of chars or subwords in a given corpus, language agnostic
'''

'''
Limitations of tokenization:
- text may include more than one word/just words...can have email addresses, URLs, special symbols
'''


# from HuggingFace Tutorial :
'''
Loading the BERT tokenizer trained with the same checkpoint as BERT is done the same way as loading the model, except we use the BertTokenizer class:
'''
from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-cased")
'''
Similar to AutoModel, the AutoTokenizer class will grab the proper tokenizer class in the library based on the checkpoint name, and can be used directly with any checkpoint:
'''
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("bert-base-cased")
tokenizer("Using a Transformer network is simple")
print(tokenizer)