from pathlib import Path
import json
import csv

class Repository:
    def __init__(self, file_name: str):
        self.DATA_DIR = Path(__file__).resolve().parent / 'data'
        self.DATA_DIR.mkdir(exist_ok=True)
        self.DB_PATH = self.DATA_DIR / file_name

    def _load(self):
        if not self.DB_PATH.exists():
            return []
        try:
            return json.loads(self.DB_PATH.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            return []

    def _save(self, items):
        self.DB_PATH.write_text(
            json.dumps(items, ensure_ascii=False, indent=2),
            encoding="utf-8"
        )

    def _list(self):
        return self._load()

    def _add_item(self, item_dict):
        items = self._load()
        items.append(item_dict)
        self._save(items)

    def _export_csv(self, file_name: str, field_names=None):
        if field_names is None:
            field_names = []
        path_csv = self.DATA_DIR / file_name
        items = self._load()
        try:
            with path_csv.open('w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=field_names)
                writer.writeheader()
                for item in items:
                    writer.writerow(item)

            return path_csv

        except PermissionError as e:
            print(f'Erro maldito: {e}')
            return None

class UserRepository(Repository):
    def __init__(self, file_name: str = 'users.json'):
        super().__init__(file_name)

class CompanyRepository(Repository):
    def __init__(self, file_name: str = 'companies.json'):
        super().__init__(file_name)
