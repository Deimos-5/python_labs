import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if not isinstance(text, str):
        raise TypeError('TypeError')
    if not isinstance(casefold, bool) or not isinstance(yo2e, bool):
        raise TypeError('TypeError')
    if casefold:
        text = text.casefold()
    else:
        text = text.lower()
    if yo2e:
        text = text.replace('ё', 'е')
        text = text.replace('Ё', 'Е')
    text = re.sub(r'[\s\t\r\n]+', ' ', text)
    text = text.strip()
    return text

def tokenize(text: str) -> list[str]:
    if not isinstance(text, str):
        raise TypeError('TypeError')
    pattern = r'\w+(?:-\w+)*'
    res = []
    for match in re.finditer(pattern, text):
        res.append(match.group())
    return res

def count_freq(tokens: list[str]) -> dict[str, int]:
    if not isinstance(tokens, (list, tuple)):
        raise TypeError('TypeError')
    for token in tokens:
        if not isinstance(token, str):
            raise TypeError('TypeError')
    res = {}
    for token in tokens:
        if token in res:
            res[token] += 1
        else:
            res[token] = 1
    return res

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    if not isinstance(freq, dict) or not isinstance(n, int) or isinstance(n, bool):
        raise TypeError('TypeError')
    for key in freq:
        if not isinstance(key, str) or not isinstance(freq[key], int) or isinstance(freq[key], bool):
            raise TypeError('TypeError')
    items = []
    for key in freq:
        items.append((key, freq[key]))
    for i in range(len(items)):
        for j in range(0, len(items) - i - 1):
            change = False
            if items[j][1] < items[j+1][1]:
                change = True
            elif items[j][1] == items[j+1][1]:
                if items[j][0] > items[j+1][0]:
                    change = True
            if change:
                tmp = items[j]
                items[j] = items[j+1]
                items[j+1] = tmp
    res = []
    counter = 0
    for item in items:
        if counter < n:
            res.append(item)
            counter += 1
        else:
            break
    return res

if __name__ == "__main__":
    print("normalize")
    cases_normalize = [("ПрИвЕт\nМИр\t", True, True), ("ёжик, Ёлка", True, True), ("Hello\r\nWorld", False, False), ("  двойные   пробелы  ", True, True)]
    for text, cf, yo in cases_normalize:
        try:
            res = normalize(text, casefold=cf, yo2e=yo)
            print(f"{repr(text)} -> '{res}'")
        except Exception as e:
            print(f"{repr(text)} -> {type(e).__name__}")

    print("\ntokenize")
    cases_tokenize = ["привет мир", "hello,world!!!", "по-настоящему круто", "2025 год", "emoji 😀 не слово"]
    for text in cases_tokenize:
        try:
            res = tokenize(text)
            print(f"{text} -> {res}")
        except Exception as e:
            print(f"'{text}' -> {type(e).__name__}")

    print("\ncount_freq")
    cases_freq = [["a","b","a","c","b","a"], ["bb","aa","bb","aa","cc"]]
    for case in cases_freq:
        try:
            res = count_freq(case)
            print(f"{case} -> {res}")
        except Exception as e:
            print(f"{case} -> {type(e).__name__}")

    print("\ntop_n")
    cases_top = [({'a':3, 'b':2, 'c':1}, 2), ({'bb':2, 'aa':2, 'cc':1}, 2)]
    for freq, n in cases_top:
        try:
            res = top_n(freq, n)
            print(f"({freq}, n={n}) -> {res}")
        except Exception as e:
            print(f"({freq}, n={n}) -> {type(e).__name__}")