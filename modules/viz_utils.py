def char_length_distr(df):
    w_len = []
    for v_list in df.vocab:
        for w in v_list:
            w_len.append(len(w))
        
    return w_len


def remove_large_words(df, max_word_size = 15):
    _ = df.copy()
    for i,document in enumerate(_['vocab']):
        for word in document:
            if len(word) > max_word_size:
                _['vocab'][i].remove(word)
    return _