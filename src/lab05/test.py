import argparse
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent.parent))

from src.lab05.json_csv import json_to_csv, csv_to_json 
from src.lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="Конвертер форматов данных (JSON, CSV, XLSX)")
    subparsers = parser.add_subparsers(dest="command", help="Доступные команды")

    parser_j2c = subparsers.add_parser("json2csv", help="Конвертировать JSON в CSV")
    parser_j2c.add_argument("--in", dest="input_path", required=True, help="Путь к входному JSON")
    parser_j2c.add_argument("--out", dest="output_path", required=True, help="Путь к выходному CSV")

    parser_c2j = subparsers.add_parser("csv2json", help="Конвертировать CSV в JSON")
    parser_c2j.add_argument("--in", dest="input_path", required=True, help="Путь к входному CSV")
    parser_c2j.add_argument("--out", dest="output_path", required=True, help="Путь к выходному JSON")

    parser_c2x = subparsers.add_parser("csv2xlsx", help="Конвертировать CSV в Excel (XLSX)")
    parser_c2x.add_argument("--in", dest="input_path", required=True, help="Путь к входному CSV")
    parser_c2x.add_argument("--out", dest="output_path", required=True, help="Путь к выходному XLSX")
    
    args = parser.parse_args()
    try:
        if args.command == "json2csv":
            json_to_csv(args.input_path, args.output_path)
            print(f"Успешно: {args.input_path} -> {args.output_path}")   
        elif args.command == "csv2json":
            csv_to_json(args.input_path, args.output_path)
            print(f"Успешно: {args.input_path} -> {args.output_path}")     
        elif args.command == "csv2xlsx":
            csv_to_xlsx(args.input_path, args.output_path)
            print(f"Успешно: {args.input_path} -> {args.output_path}")  
        else:
            parser.print_help()
            
    except (FileNotFoundError, ValueError) as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()