from models import Usuario, Company
from repo import UserRepository, CompanyRepository
from stages import COMPANIES
from datetime import datetime

user_backend = UserRepository('users.json')
company_backend = CompanyRepository('companies.json')

def add_user():
    nome = input('\nNome completo:\t')
    data_str = input('Data de nascimento (DD/MM/AAAA):\t')
    tipo_sang = input('Tipo sanguíneo (ex: O+, A-, B+)::\t')
    email = input('E-mail:\t')

    company_input = input('Empresa que trabalha (nenhuma/procurando):\t').strip().lower()

    if company_input in ('nenhuma', 'procurando'):
        working_on = company_input
    else:
        if company_input not in COMPANIES:
            print(f'\nNenhuma empresa com o nome: "{company_input}" encontrada. Mesmo assim vou salvar esse nome.')
        working_on = company_input

    try:
        data_nasc = datetime.strptime(data_str, '%d/%m/%Y').date()
    except ValueError:
        print('\nData inválida. Use o formato DD/MM/AAAA.')
        return

    user = Usuario(nome, data_nasc, tipo_sang, email=email, working_on=working_on)
    modeled_user = user.model_user()

    user_backend._add_item(modeled_user)
    print('\nUsuário adicionado com sucesso')

def add_company():
    nome = input('\nNome da empresa:\t')
    descr = input('Breve descrição:\t')
    try:
        nota_input = int(input('Avaliação (0-5):\t'))
    except ValueError:
        print('\nAvaliação inválida. Use um número inteiro entre 0 e 5.')
        return

    company = Company(nome, descr)
    company._dar_nota(nota_input)

    modeled_company = company.model_company()

    company_backend._add_item(modeled_company)
    if nome.lower() not in COMPANIES:
        COMPANIES.append(nome.lower())
    print('\nEmpresa adicionada com sucesso')

def list_user():
    users = user_backend._list()
    if not users:
        print('Nenhum usuário carregado')
        return

    print(f'\n## | {"Name":<20} | {"Age":<5} | {"Email":<30} | {"Working on":<20}')
    for i, l in enumerate(users):
        name = l.get("name", "")
        age = l.get("age", "")
        email = l.get("email", "")
        working_on = l.get("working_on", "")
        print(f'{i:02d} | {name:<20} | {str(age):<5} | {email:<30} | {working_on:<20}')

def list_company():
    companies = company_backend._list()
    if not companies:
        print('Nenhuma empresa carregada')
        return

    print(f'\n## | {"Name":<20} | {"Caption":<30} | {"Rate":<5} | {"Employees":<10}')
    for i, l in enumerate(companies):
        name = l.get("name", "")
        caption = l.get("caption", "")
        rate = l.get("rate", "")
        employees = l.get("employees", "")
        print(f'{i:02d} | {name:<20} | {caption:<30} | {str(rate):<5} | {str(employees):<10}')

def search_company():
    input_search = input('Buscar por:\t').strip().lower()

    if not input_search:
        print('\nConsulta vazia')
        return

    companies = company_backend._list()
    results = []

    for l in companies:
        company_str = f"{l.get('name', '')} | {l.get('caption', '')} | {l.get('rate', '')} | {l.get('employees', '')}".lower()

        if input_search in company_str:
            results.append(l)

    if not results:
        print('\nNada encontrado')
        return

    print(f'\n## | {"Name":<20} | {"Caption":<30} | {"Rate":<5} | {"Employees":<10}')
    for i, l in enumerate(results):
        name = l.get("name", "")
        caption = l.get("caption", "")
        rate = l.get("rate", "")
        employees = l.get("employees", "")
        print(f'{i:02d} | {name:<20} | {caption:<30} | {str(rate):<5} | {str(employees):<10}')

def search_user():
    input_search = input('Buscar por:\t').strip().lower()

    if not input_search:
        print('\nConsulta vazia')
        return

    users = user_backend._list()
    results = []

    for l in users:
        user_str = f"{l.get('name', '')} | {l.get('age', '')} | {l.get('email', '')} | {l.get('working_on', '')}".lower()

        if input_search in user_str:
            results.append(l)

    if not results:
        print('\nNada encontrado')
        return

    print(f'\n## | {"Name":<20} | {"Age":<5} | {"Email":<30} | {"Working on":<20}')
    for i, l in enumerate(results):
        name = l.get("name", "")
        age = l.get("age", "")
        email = l.get("email", "")
        working_on = l.get("working_on", "")
        print(f'{i:02d} | {name:<20} | {str(age):<5} | {email:<30} | {working_on:<20}')

def to_csv(backend, file_name, field_names=None):
    if field_names is None:
        field_names = []
    path_csv = backend._export_csv(file_name, field_names)
    if path_csv is None:
        print('Erro ao exportar o CSV... Feche o arquivo e tente novamente')
    else:
        print(f'Sucesso! CSV Exportado para: {path_csv}')

def main():
    while True:
        _main_menu()
        try:
            op = int(input('\nEscolha:\t'))
        except ValueError:
            print('\nDigite um número válido')
            continue

        if op == 1:
            main_users()
        elif op == 2:
            main_companies()
        elif op == 3:
            print('\nAté mais!')
            break
        else:
            print('Opção inválida')

def main_users():
    while True:
        _users_menu()

        try:
            op = int(input('\nEscolha:\t'))
        except ValueError:
            print('\nDigite um número válido')
            continue

        if op == 1:
            add_user()
        elif op == 2:
            list_user()
        elif op == 3:
            search_user()
        elif op == 4:
            to_csv(
                backend=user_backend,
                file_name='users.csv',
                field_names=[
                    'name',
                    'birthdate',
                    'age',
                    'email',
                    'blood_type',
                    'working_on'
                ]
            )
        elif op == 5:
            break
        else:
            print('\nDigite uma opção válida')

def main_companies():
    while True:
        _companies_menu()

        try:
            op = int(input('\nEscolha:\t'))
        except ValueError:
            print('\nDigite um número válido')
            continue

        if op == 1:
            add_company()
        elif op == 2:
            list_company()
        elif op == 3:
            search_company()
        elif op == 4:
            to_csv(
                backend=company_backend,
                file_name='companies.csv',
                field_names=[
                    'name',
                    'caption',
                    'rate',
                    'employees'
                ]
            )
        elif op == 5:
            break
        else:
            print('\nDigite uma opção válida')

def _users_menu():
    print('\n[1] Add user')
    print('[2] List users')
    print('[3] Search user')
    print('[4] Export to `.csv`')

    print('\n[5] Back')

def _companies_menu():
    print('\n[1] Add company')
    print('[2] List companies')
    print('[3] Search company')
    print('[4] Export to `.csv`')

    print('\n[5] Back')

def _main_menu():
    print('\nMINI CRM - Adicionar/Listar com OO')

    print('\n[1] Users')
    print('[2] Companies')

    print('\n[3] Sair')


if __name__ == '__main__':
    main()
