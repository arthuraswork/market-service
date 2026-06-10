def get_list(path = 'data/data.jsonl'):
    with open(path, 'r') as f:
        for j in f:
            yield j