from sudachipy import tokenizer
from sudachipy import dictionary



def analize(text):
    tokenizer_obj = dictionary.Dictionary().create()
    mode = tokenizer.Tokenizer.SplitMode.A
    tokens = tokenizer_obj.tokenize(text, mode)
    #tokens = tokenizer_obj.tokenize(tokenizer.Tokenizer.SplitMode.C, text)
    return tokens

if __name__ == "__main__":
    text = "私は昨日東京に行きました。"
    tokenizer_obj = dictionary.Dictionary().create()
    #tokens = tokenizer_obj.tokenize(tokenizer.Tokenizer.SplitMode.C, text)
    mode = tokenizer.Tokenizer.SplitMode.A
    tokens = tokenizer_obj.tokenize(text, mode)
    for t in tokens:
        print(t.surface(), t.part_of_speech(), t.reading_form(), t.normalized_form())
