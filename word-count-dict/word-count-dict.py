def word_count_dict(sentences):
    """
    Returns: dict[str, int] - global word frequency across all sentences
    """
    # Your code here
    hashmap = {}
    for sentence in sentences:
        for word in sentence:
            if word not in hashmap:
                hashmap[word] = 1
            else:
                hashmap[word] = hashmap[word] + 1
    return hashmap