words = ['cat', 'window', 'defenstrate']
for w in words:
    print(w, len(w))

for w in words[:]:
    if len(w) > 6:
        words.insert(0, w)
        print(w, words)
