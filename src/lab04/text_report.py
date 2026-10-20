import argparse
import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from src.lab04.io_txt_csv import read_text, write_csv
import src.lib.text

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument("--in", dest="input_path", required=True)
    parser.add_argument("--out", dest="output_path", required=True)
    args=parser.parse_args()
    
    txt=read_text(args.input_path)
    normalized=src.lib.text.normalize(txt)
    tokens=src.lib.text.tokenize(normalized)
    freq=src.lib.text.count_freq(tokens)
    top=src.lib.text.top_n(freq, 5)
    
    header=("word", "count")
    write_csv(top, args.output_path, header=header)

if __name__ == "__main__":
    main()
