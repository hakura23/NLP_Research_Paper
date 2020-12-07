import corpus_transform
import output_format
import sys
import nltk
from nltk.tag import StanfordNERTagger
from nltk.tag import pos_tag
from nltk.tokenize import word_tokenize

# this program reads in the command line argument, which is a path to the corpus, runs the stanford model on it and creates a output txt file

if len(sys.argv) != 2:
    exit('Not the right amount of arguments. Exit.')

file_path = sys.argv[1]

# call transform function to turn the file into a list of sentences
sentences = corpus_transform.transform(file_path)

print(sentences)

# initiate the tagger
model = '../stanford-ner-2020-11-17/classifiers/english.all.3class.distsim.crf.ser.gz'
jar = '../stanford-ner-2020-11-17/stanford-ner.jar'
encoding = 'utf8'

tagger = StanfordNERTagger(model, jar, encoding)

# open the output file to write
output = open('stanford_output.txt', 'w')
buf = '\n'

for sentence in sentences:
    tok_words = sentence.split(' ')
    buf += output_format.stanford_format(tagger.tag(tok_words))

output.write(buf)

output.close()