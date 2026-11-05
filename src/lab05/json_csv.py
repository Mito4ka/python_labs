from pathlib import Path
import csv
import json

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте.
    """
    json_f=Path(json_path)
    csv_f=Path(csv_path)
    
    
    if not json_f.exists():
        raise FileNotFoundError("файл не найден")
    if json_f.suffix.lower() != ".json":
        raise ValueError('Входной файл должен быть JSON')
    if csv_f.suffix.lower() != ".csv":
        raise ValueError("Входной файл должен быть CSV")
    
    
    with json_f.open ("r",encoding='UTF-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON / неподдерживаемая структура")
        
    if not isinstance(data, list) or len(data) == 0:
        raise ValueError('Файл JSON пустой / имеет неправильный формат')
    if not all(isinstance(i, dict) for i in data):
        raise ValueError("Все элементы списка JSON должны быть словарями")
    
    fieldnames = {}
    for element in data:
        for key in element.keys():
            fieldnames[key] = None

    with csv_f.open('w', newline="", encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=list(fieldnames.keys()))
        w.writeheader()
        w.writerows(data)


if __name__ == '__main__':
    json_to_csv('data/lab05/samples/people1.json','data/lab05/out/people_from_json1.csv')
    json_to_csv('data/lab05/samples/cities2.json','data/lab05/out/cities_json_to2_.csv')
    json_to_csv('data/lab05/samples/my_example.json','data/lab05/out/my_example_json_to_.csv')
    
############################################################################################3
    
def csv_to_json(csv_path: str, json_path: str) -> None:
    """
    Преобразует CSV в JSON (список словарей).
    Заголовок обязателен, значения сохраняются как строки.
    json.dump(..., ensure_ascii=False, indent=2)
    """
    csv_fi=Path(csv_path)
    json_fi=Path(json_path)
    
    if not csv_fi.exists():
        raise FileNotFoundError("CSV Файл не найден")
    if csv_fi.suffix.lower() != ".csv":
            raise ValueError("Входной файл должен быть CSV")
    if json_fi.suffix.lower() != ".json":
        raise ValueError("Входной файл должен быть JSON")
    
    
    with csv_fi.open('r',encoding='UTF-8',newline='') as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("CSV не содержит заголовок")
        rows=list(reader)
        
        
        if len(rows) == 0:
            raise ValueError("В CSV не содержится данных")
        
        with json_fi.open("w", encoding="utf-8") as f:
            json.dump(rows, f, ensure_ascii=False, indent=2)
            
if __name__=='__main__':
    csv_to_json('data/lab05/samples/cities3.csv','data/lab05/out/cities3.json')
   