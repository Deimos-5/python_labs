import json
import csv
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    try:
        with open(json_path, 'r', encoding='utf-8') as f:
            data=json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Файл не найден")
    except json.JSONDecodeError:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    if not data or not isinstance(data,list):
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    if not isinstance(data[0],dict):
        raise ValueError("JSON должен содержать список словарей")
    keys=set()
    for row in data:
        keys.update(row.keys())
    keys=list(keys)
    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer=csv.writer(f)
        for row in data:
            row_lst=[]
            for key in keys:
                row_lst.append(row.get(key, ''))
            writer.writerow(row_lst)

def csv_to_json(csv_path: str, json_path: str) -> None:
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader=csv.reader(f)
            try:
                headers=next(reader)
            except StopIteration:
                raise ValueError('CSV пустой')
            if not headers:
                raise ValueError('CSV без заголовка')
            res=[]
            for row in reader:
                if not row:
                    continue
                row_dct=dict(zip(headers,row))
                res.append(row_dct)
    except FileNotFoundError:
        raise FileNotFoundError('Файл не найден')
    if not res:
        raise ValueError('CSV пустой')
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(res, f, ensure_ascii=False, indent=2)