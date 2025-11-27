def booktext(x):
    with open(x) as l:
         file_content = l.read()
    return(file_content)
def num_words(text):
    h = text.split()
    return(len(h))
def characters(text):
    n_characters = {}
    for tq in text:
        pq = tq.lower()
        if pq not in n_characters:
           n_characters[pq] = 1
        else:
           n_characters[pq] += 1
    return(n_characters)
def sorting1(text3):
    lista = []
    for char in text3:
        m = text3[char]
        h = {"char": char, "num": m}
        lista.append(h)
    def sort_on(item):
        return item["num"]
    lista.sort(reverse=True, key=sort_on)
    return(lista)

