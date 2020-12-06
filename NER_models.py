import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

# sample text and tokenized text
text = 'Qiaotong Wu, Bruce Jiang, and Thomas Lin are students at New York University working on NER taggers.'
tok_words = word_tokenize(text)


print('\n\n\nStanford:\n\n\n')

# Stanford Core Tagger

# download the stanford software from https://nlp.stanford.edu/software/CRF-NER.html, you'll get a package called stanfer-ner-2020-11-17
# the stanford model takes three parameters to init:
# first one is the path to classifier (the path to a file in the classfiers directory in stanford-ner-2020-11-17), 
# the second is the stanford-ner.jar file in the package (the path to the stanford-ner.jar file in stanford-ner-2020-11-17)
# the third is the encoding info, in this case we just pass in utf8

# to run the stanfordNERTagger, init one instance, call it "tagger", tokenize the text, and run tagger.tag(the tokenized text)

from nltk.tag import StanfordNERTagger

model = '../stanford-ner-2020-11-17/classifiers/english.all.3class.distsim.crf.ser.gz'
jar = '../stanford-ner-2020-11-17/stanford-ner.jar'
encoding = 'utf8'

tagger = StanfordNERTagger(model, jar, encoding)
print(tagger.tag(tok_words))

print('\n\n\nNLTK:\n\n\n')

# NLTK NE chunking

# to run NLTK Named Entity chunking, we first tokenize the text, then do POS tagging on the tokenized text with nltk.pos_tag(), then we run nltk.ne_chunk()
# on the tagged text.

# notice that what is returned is a tree-liked annotated text, so we have to handle the formatting to match with the answer key
pos_tags = pos_tag(tok_words)
print(nltk.ne_chunk(pos_tags))



print('\n\n\nFlair:\n\n\n')

# Flair

# first we need to download flair software, run the following command:
# pip3 install flair
# or pip install flair (if you are using pip instead of pip3)

# now we can use flair to do NER tagging
from flair.data import Sentence
from flair.models import SequenceTagger

# first we load the NER tagger, this should be done only once
tagger = SequenceTagger.load('ner')

# call Sentence() with the text passed in to create Sentence object
sentence = Sentence(text)

# predict NER tags
tagger.predict(sentence)

# print results
# word + \t + 
for token in sentence:
    print(str(token).split(' ')[2], end='')
    print('\t', end='')
    print(str(token.get_tag('ner')).split(' ')[0])



print('\n\n\nSpaCY\n\n\n')

#spaCy NE

# same as above, first thing to do: pip3 install spacy
# then, run: python3 -m spacy download en_core_web_sm

# import spacy
import spacy

# load the tagger
tagger = spacy.load("en_core_web_sm")

doc = tagger(text)
# we can just use the label data field to see the tag
for word in doc:
    print(word.text, word.ent_type_)

# Notice that if a word is not tagged, its tag is an empty string

