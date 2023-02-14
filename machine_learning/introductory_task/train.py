import unicodedata


def change_text(text):
    text= unicodedata.normalize("NFKD", text)
    text = text.lower()
    text = text.replace('.',' ')
    text = text.replace(',',' ')
    text = text.replace('-',' ')
    text = text.replace('%','')
    text = text.replace(':',' ')
    text = text.replace('(','')
    text = text.replace(')','')
    text = text.replace('\n',' ')
    text = text.replace('[',' ')
    text = text.replace(']',' ')
    text = text.replace('"',' ')
    text = text.replace('  ',' ')
    text = text.replace('\t', ' ')
    text = text.replace('?', ' ')
    text = text.replace(u'\xa0-', u' ')
    text = text.replace(u'-\xa0', u' ')
    text = text.replace('–', ' ')
    text = text.replace('>', ' ')
    text = text.replace('<', ' ')
    text = text.replace('—', ' ')
    text = text.replace('!', ' ')
    text = text.replace(';', ' ')
    return text


def read_data(filename):
  with open(filename,'r') as f:
    data = []
    file_string = f.read()
    file_string = change_text(file_string)
    file_string = file_string.split(' ')
    data.extend(file_string)

  return data


def text(input_dir='poems.txt'):
    words = read_data(input_dir)
    words=list(filter(None, words))
    words=list(filter(lambda c:c!="с", words))
    words=words[:len(words)]
    return words


def all_combinations(word):
    data_ = []
    words=text()
    for i in range(1,len(words)):
        if words[i-1]==word:
            data_.append(words[i])
    data_head=list(set(data_))
    data_count=[0]*len(data_head)
    for i in range(len(data_head)):
        data_count[i]=data_.count(data_head[i])
    return data_count,data_head