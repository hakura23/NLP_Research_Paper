import corpus_transform
import output_format
import sys
import flair
from flair.data import Sentence
from flair.models import SequenceTagger

corpus = sys.argv[1]
source = corpus_transform.transform(corpus)
print(source)
tagger = SequenceTagger.load('ner')
# target file for write
f = open("flair-output.txt", "w")
buf = '\n'

for text in source:
    sentence = Sentence(text)
    tagger.predict(sentence)
    lst = []
    for token in sentence:
        lst.append([str(token).split(' ')[2], str(token.get_tag('ner')).split(' ')[0]])
    model_result = output_format.flair_format(lst)
    buf = buf + model_result

f.write(buf)
f.close()