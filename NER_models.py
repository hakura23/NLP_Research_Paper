import nltk
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

# sample text and tokenized text
text = 'Qiaotong\n Wu\n, Bruce\n Jiang\n, and\n Thomas\n Lin\n are\n students\n at\n New\n York\n University\n working\n on\n NER\n taggers\n.\n'
tok_words = word_tokenize(text)


print('\n\n\nStanford:\n\n\n')

# Stanford Core Tagger

# the stanford model takes three parameters to init, first one is the classifier (the path to a file in the classfiers directory), 
# the second is the stanford-ner.jar file in the package (the path to the stanford-ner.jar file)
# the third is the encoding info, in this case we just pass in utf8

# to run the stanfordNERTagger, init one instance, call it "tagger", tokenize the text, and run tagger.tag(the tokenized text)

from nltk.tag import StanfordNERTagger

model = 'stanford-ner-2020-11-17/classifiers/english.all.3class.distsim.crf.ser.gz'
jar = 'stanford-ner-2020-11-17/stanford-ner.jar'
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

