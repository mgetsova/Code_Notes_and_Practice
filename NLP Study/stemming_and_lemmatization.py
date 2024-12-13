# Stemming 

'''
- eliminates prefixes and suffixes from words
- most common alg for stemmign English words: Porter's Alg
    5 phases of word reductions applied sequentially
    each phase has conventions for how to select rules
    Limitation: morphological variants produced are not always real words
- use language specific rules but require less knowledge than a lemmatizer
- stemmed form does not matter, only the equivalence classes it forms
- stemming tends to increase recall while harming precision

There are many other algorithms for stemming, like an N-Gram stemmer.\

Disadvantages / Challenges:
- over-stemming : when stemmer produces incorrect root forms or non-valid words
(ex: "arguing" stemmed to "argu") ...can be addressed by choosing right stemmer,
testing on sample text, using lemmatization

- under-stemming: stemmer fails to produce accurate root forms or reduce words
to their base form (same way to address as above)
'''

# Porter stemmer in NLTK
from nltk.stem import PorterStemmer
 
# Create a Porter Stemmer instance
porter_stemmer = PorterStemmer()
 
# Example words for stemming
words = ["running", "jumps", "happily", "running", "happily"]
 
# Apply stemming to each word
stemmed_words = [porter_stemmer.stem(word) for word in words]
 
# Print the results
print("Original words:", words)
print("Stemmed words:", stemmed_words)


# Lemmatization
'''
- more powerful than stemming
- "doing things properly with the use of a vocabulary and morphological analysis
of words, aiming to remove inflectional endings only and return the base or 
dictionary form of the word (the lemma)"
ie. considers context, usually use positional arguments (verb, adj, or noun) as 
input as well
- typially, lemmatizers preferred to stemmers, or nice to do both but in 
search engines, stemming alone is sufficient
(both stemming and lemamtization also useful in building knowledge graphs)

In NLTK, WordNet lemamtizer can be used with or without part of speech (POS) tagging
'''


import nltk
nltk.download('wordnet')
from nltk.stem import WordNetLemmatizer
 
# Create WordNetLemmatizer object
wnl = WordNetLemmatizer()
 
# single word lemmatization examples
list1 = ['kites', 'babies', 'dogs', 'flying', 'smiling', 
         'driving', 'died', 'tried', 'feet']
for words in list1:
    print(words + " ---> " + wnl.lemmatize(words))






# sentence lemmatization examples
string = 'the cat is sitting with the bats on the striped mat under many flying geese'
 
# Converting String into tokens
list2 = nltk.word_tokenize(string)
print(list2)
#> ['the', 'cat', 'is', 'sitting', 'with', 'the', 'bats', 'on',
#   'the', 'striped', 'mat', 'under', 'many', 'flying', 'geese']
 
lemmatized_string = ' '.join([wnl.lemmatize(words) for words in list2])
 
print(lemmatized_string)   
#> the cat is sitting with the bat on the striped mat under many flying goose



'''
WordNet lemmatizer with POS tagging:
'''
# WORDNET LEMMATIZER (with appropriate pos tags)
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import wordnet
 
lemmatizer = WordNetLemmatizer()
 
# Define function to lemmatize each word with its POS tag
 
# POS_TAGGER_FUNCTION : TYPE 1
def pos_tagger(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:          
        return None
 
sentence = 'the cat is sitting with the bats on the striped mat under many badly flying geese'
 
# tokenize the sentence and find the POS tag for each token
pos_tagged = nltk.pos_tag(nltk.word_tokenize(sentence))  
 
print(pos_tagged)
#>[('the', 'DT'), ('cat', 'NN'), ('is', 'VBZ'), ('sitting', 'VBG'), ('with', 'IN'), 
# ('the', 'DT'), ('bats', 'NNS'), ('on', 'IN'), ('the', 'DT'), ('striped', 'JJ'), 
# ('mat', 'NN'), ('under', 'IN'), ('many', 'JJ'), ('flying', 'VBG'), ('geese', 'JJ')]
 
# As you may have noticed, the above pos tags are a little confusing.
 
# we use our own pos_tagger function to make things simpler to understand.
wordnet_tagged = list(map(lambda x: (x[0], pos_tagger(x[1])), pos_tagged))
print(wordnet_tagged)
#>[('the', None), ('cat', 'n'), ('is', 'v'), ('sitting', 'v'), ('with', None), 
# ('the', None), ('bats', 'n'), ('on', None), ('the', None), ('striped', 'a'), 
# ('mat', 'n'), ('under', None), ('many', 'a'), ('flying', 'v'), ('geese', 'a')]
 
lemmatized_sentence = []
for word, tag in wordnet_tagged:
    if tag is None:
        # if there is no available tag, append the token as is
        lemmatized_sentence.append(word)
    else:        
        # else use the tag to lemmatize the token
        lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
lemmatized_sentence = " ".join(lemmatized_sentence)
 
print(lemmatized_sentence)
#> the cat can be sit with the bat on the striped mat under many fly geese


# extra: POS tagging in NLTK
from nltk.tokenize import word_tokenize
from nltk import pos_tag
 
# Sample text
text = "NLTK is a powerful library for natural language processing."
 
# Performing PoS tagging
pos_tags = pos_tag(word_tokenize(text))
 
# Displaying the PoS tagged result in separate lines
print("Original Text:")
print(text)
 
print("\nPoS Tagging Result:")
for word, pos_tag in pos_tags:
    print(f"{word}: {pos_tag}")