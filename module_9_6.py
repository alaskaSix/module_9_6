def all_variants(text):
    result = len(text)
    for s in range(result):
        for n in range(s + 1, result + 1):
            yield text[s:n]


a = all_variants("abc")
for i in a:
    print(i)
