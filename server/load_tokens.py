def load_tokens(path='secrets/tokens.txt'):
    with open(path, 'r', encoding='utf-8') as tf:
        tokens = tf.readlines()
        return [t.strip('\n') for t in tokens]
    