import sys
import lib.text

def main():
    text=sys.stdin.read()
    
    normalized=lib.text.normalize(text)
    tokens=lib.text.tokenize(normalized)
    freq=lib.text.count_freq(tokens)
    top=lib.text.top_n(freq, 5)
    
    total_words=len(tokens)
    unique_words=len(freq)
    
    print(f"Всего слов: {total_words}")
    print(f"Уникальных слов: {unique_words}")
    print("Топ-5:")
    
    for word, count in top:
        print(f"{word}:{count}")

main()