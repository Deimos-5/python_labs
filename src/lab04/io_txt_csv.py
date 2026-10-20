import csv
from pathlib import Path

def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    if not isinstance(path, (str, Path)) or not isinstance(encoding, str):
        raise TypeError('TypeError')
    p=Path(path)
    return p.read_text(encoding=encoding)

def write_csv(rows: list, path: str | Path, header: tuple | None = None) -> None:
    if not isinstance(rows, list) or not isinstance(path, (str, Path)):
        raise TypeError('TypeError')
    if header is not None and not isinstance(header, tuple):
        raise TypeError('TypeError')
    for row in rows:
        if not isinstance(row, (tuple, list)):
            raise TypeError('TypeError')
    p=Path(path)
    if len(rows) > 0:
        row_len=len(rows[0])
        for r in rows:
            if len(r) != row_len:
                raise ValueError('ValueError')
    with p.open("w", newline="", encoding="utf-8") as f:
        w=csv.writer(f)
        if header is not None:
            w.writerow(header)
        for r in rows:
            w.writerow(r)

if __name__ == "__main__":
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parent.parent.parent))
    
    from src.lab04.io_txt_csv import read_text, write_csv
    txt = read_text("data/input.txt")
    print(f"Результат read_text -> {repr(txt)}")
    
    write_csv([("word", "count"), ("test", 3)], "data/check.csv")


