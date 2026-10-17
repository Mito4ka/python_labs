def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
   
    if casefold==True:
        s=text.casefold()
    else:
        s=text.lower()

    if yo2e==True:
        s=s.replace("ё","е")

    norm_s=" ".join(s.split())
    return norm_s

print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
#print(normalize("Hello\r\nWorld"))
#print(normalize("  двойные   пробелы  "))


import re
def tokenize(text: str) -> list[str]:

    result=normalize(text)
    return re.findall(r"\w+(?:-\w+)*",result)

#print(tokenize("привет мир"))
#print(tokenize("hello,world!!!"))
#print(tokenize("по-настоящему круто"))
#print(tokenize("2025 год"))
#print(tokenize("emoji 😀 не слово"))

def count_freq(tokens: list[str]) -> dict[str, int]:

    freq={}
    for w in tokens:
        freq[w]=freq.get(w,0)+1
    return freq


#print(count_freq(["a","b","a","c","b","a"]))
#print(count_freq(["bb","aa","bb","aa","cc"]))

#Б

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

   
    top=sorted(freq.items(),key=lambda p: (-p[1],p[0]))[:n]
    return top

#print(top_n({'a': 3, 'b': 2, 'c': 1}))
#print(top_n({'bb': 2, 'aa': 2, 'cc': 1}))