# The parameter model is:
# nlp = spacy.load("en_core_web_sm")
# model = nlp(*SENTENCE WE WANT TO TAG*)


def SpaCy_Format(model):
    out_str = '\n'
    for ent in model.dents:
        if ent.label_ == 'PERSON':
            out_str = out_str + ent.text + '\tPER\n'
        elif ent.label_ == 'ORG':
            out_str = out_str + ent.text + '\tORG\n'
        elif ent.label_ == 'GPE':
            out_str = out_str + ent.text + '\tLOC\n'
        elif ent.label_ == 'LOC':
            out_str = out_str + ent.text + '\tLOC\n'
    out_str = out_str + '\n'
    return out_str