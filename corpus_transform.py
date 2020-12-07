# this program reads in the corpus and returns a list of sentences (list of strings)

# assuming each sentence starts and ends with a new line

def transform(file_name):
    file = open(file_name, 'r')

    output = []
    buf = ''
    line = file.readline()
    while line:
        if line == '\n':
            output.append(buf.strip())
            buf = ''
        else:
            buf += line[:-1] + ' '

        line = file.readline()

    return output[1:-2]