def Reversed_sentence(sentence):
    words=sentence.split(' ')
    rev_words=reversed(words)
    rev_sentence=' '.join(rev_words)
    return rev_sentence

sentence=input('enter the sentence: ')
print(Reversed_sentence(sentence))