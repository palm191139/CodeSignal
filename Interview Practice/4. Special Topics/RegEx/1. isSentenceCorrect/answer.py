def isSentenceCorrect(sentence):
    pattern = r"^[A-Z][^.?!]*[.?!]$"
    return re.match(pattern, sentence) is not None
