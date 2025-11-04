from datetime import date

class Company:
    def __init__(self, nome: str, descr: str):
        self.nome = nome
        self.descr = descr
        self.notas = []
        self.employees = []

    def _dar_nota(self, nota: int) -> int:
        if nota < 0 or nota > 5:
            print('\nDefina uma nota entre 0-5')
            return 0

        self.notas.append(nota)
        return nota

    def _media_notas(self) -> float:
        if not self.notas:
            return 0.0
        media = sum(self.notas) / len(self.notas)
        return media

    def _get_employees(self) -> int:
        return len(self.employees)

    def model_company(self):
        return {
            "name": self.nome,
            "caption": self.descr,
            "rate": self._media_notas(),
            "employees": self._get_employees(),
        }

class Usuario:
    def __init__(self, nome: str, data_nasc: date, tipo_sang: str, email: str, working_on: str):
        self.nome = nome
        self.data_nasc = data_nasc
        self.idade = self._calcular_idade()
        self.email = email
        self.tipo_sang = tipo_sang
        self.working_on = working_on

    def _calcular_idade(self) -> int:
        hoje = date.today()
        idade = hoje.year - self.data_nasc.year

        if (hoje.month, hoje.day) < (self.data_nasc.month, self.data_nasc.day):
            idade -= 1

        return idade

    def model_user(self):
        return {
            "name": self.nome,
            "birthdate": self.data_nasc.isoformat(),
            "age": self.idade,
            "email": self.email,
            "blood_type": self.tipo_sang,
            "working_on": self.working_on,
        }
