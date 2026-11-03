
import csv
import json
from pathlib import Path
from src.lab04.io_txt_csv import ensure_parent_dir

def json_to_csv(json_path: str, csv_path: str) -> None:
#Записывает значения
#
 #   Args:
 #       json_path: Путь к json файлу из которого читаем
  #      csv_path: Путь к csv файлу куда пишем

   # Returns: 
    #    None

    #Raises:
     #   FileNotFoundError: 
      #      Указанный JSON файл не найден
       # ValueError:
        #    Указанный файл не формата JSON
         #   Пустой JSON или неподдерживаемая структура
          #  Файл JSON пустой или имеет неправильный формат
           # Все элементы списка JSON должны быть словарями

    j_p = Path(json_path)
    c_p = Path(csv_path)
    
    if not j_p.exists():
        raise FileNotFoundError(f"файл не найден: {j_p}")
    if j_p.suffix.lower() != '.json':
        raise ValueError(f"Указанный файл не формата JSON: {j_p}")
    

    with j_p.open('r', encoding='utf-8') as j_f:
        try:
            data = json.load(j_f)
        except json.JSONDecodeError as e:
            raise ValueError(f"Файл содержит некорректный JSON: {e.lineno}, {e.msg}")
        if not isinstance(data,list) or len(data) == 0:
            raise ValueError("Файл JSON пустой или имеет неправильный формат")
        if not all(isinstance(x, dict) for x in data):
            raise ValueError("Все элементы списка JSON должны быть словарями")
        
    ensure_parent_dir(c_p)
    # порядок колонок определяется их первым появлением в JSON
    headers = []
    seen = set()
    for item in data:
        for key in item.keys():
            if key not in seen:
                seen.add(key)
                headers.append(key)
            
    with open(c_p, 'w', newline="", encoding="utf-8") as c_f:
            #restval - заполняет отсутствующие поля пустыми строками
            writer = csv.DictWriter(c_f, fieldnames=headers, restval="")
            writer.writeheader()
            writer.writerows(data)
'''
import csv
from pathlib import Path
from openpyxl import Workbook
from openpyxl.utils import get_column_letter
from src.lab04.io_txt_csv import ensure_parent_dir

def csv_to_xlsx(csv_path: str, xlsx_path: str) -> None:
    """Преобразует CSV в XLSX с авто-шириной колонок."""
    csv_file = Path(csv_path)
    xlsx_file = Path(xlsx_path)

    if not csv_file.exists():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")
    if csv_file.stat().st_size == 0:
        raise ValueError(f"Файл {csv_path} пуст")

    wb = Workbook()
    ws = wb.active
    ws.title = "Data"

    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row_idx, row in enumerate(reader, 1):
            for col_idx, value in enumerate(row, 1):
                ws.cell(row=row_idx, column=col_idx, value=value)

    # Авто-ширина колонок
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter # Получаем букву колонки (A, B, C...)
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 2)
        ws.column_dimensions[column].width = adjusted_width

    ensure_parent_dir(str(xlsx_file))
    wb.save(xlsx_file)
'''