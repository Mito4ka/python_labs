# ЛР3 — Тексты и частоты слов (словарь/множество)
# Задание A — src/lib/text.py
normalize
```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
 
    if casefold==True:
        s=text.casefold()
    else:
        s=text.lower()

    if yo2e==True:
        s=s.replace("ё","е")

    norm_s=" ".join(s.split())
    return norm_s

```
![](../../images/lab03/normalize_out.png)

tokenize
```python
import re
def tokenize(text: str) -> list[str]:

    result=normalize(text)
    return re.findall(r"\w+(?:-\w+)*",result)

print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
```
![](../../images/lab03/tokenize_out.png)

count_freq
```python
def count_freq(tokens: list[str]) -> dict[str, int]:

    freq={}
    for w in tokens:
        freq[w]=freq.get(w,0)+1
    return freq


print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["bb","aa","bb","aa","cc"]))
```
![](../../images/lab03/Count_freq.png)

top_n
```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

   
    top=sorted(freq.items(),key=lambda p: (-p[1],p[0]))[:n]
    return top

print(top_n({'a': 3, 'b': 2, 'c': 1}))
print(top_n({'bb': 2, 'aa': 2, 'cc': 1}))
```
![](../../images/lab03/top_n.png)

# Задание B — src/text_stats.py
```python
from src.lib.text import normalize, tokenize, count_freq, top_n

text=input()

norm_text=normalize(text)
token_text=tokenize(norm_text)
cnt_unik_words=count_freq(token_text)
top=top_n(cnt_unik_words)

print(f'Всего слов: {len(token_text)}')
print(f'Уникальных слов: {len(cnt_unik_words)}')
print('Топ-5:')
for kzh in top:
    print(f'{kzh[0]}: {kzh[1]}')

print('Привет, мир! Привет!!!')

```
![](../../images/lab03/text_stats_out.png)