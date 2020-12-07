import corpus_transform
import output_format
import nltk
from nltk.tag import pos_tag
import sys

if len(sys.argv) != 2:
    exit('Not the right amount of arguments. Exit.')

file_path = sys.argv[1]

# call transform function to turn the file into a list of sentences
sentences = corpus_transform.transform(file_path)

# open the output file to write
output = open('nltk_output.txt', 'w')
buf = '\n'

for sentence in sentences:
    tok_words = sentence.split(' ')
    buf += output_format.nltk_format(nltk.ne_chunk(pos_tag(tok_words)))

output.write(buf)

output.close()
