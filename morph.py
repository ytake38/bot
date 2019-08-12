from sudachipy import tokenizer
from sudachipy import dictionary



def analize(text):
    tokenizer_obj = dictionary.Dictionary().create()
    tokens = tokenizer_obj.tokenize(tokenizer.Tokenizer.SplitMpde.C, text)
    return tokens
