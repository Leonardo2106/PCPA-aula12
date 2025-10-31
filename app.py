from models import Lead
from repo import LeadRepository
from stages import DEFAULT_STAGE

lead_backend = LeadRepository()

def add_lead():
    name = input('Nome:\t')
    company = input('Empresa:\t')
    email = input('Email:\t')

    lead = Lead(name, company, email, DEFAULT_STAGE)

    modeled_lead = lead.model_lead()

    lead_backend.add_lead(modeled_lead)
    print('\nLead adicionado com sucesso!')

def list_lead():
    leads = lead_backend.list_leads()
    if not leads:
        print('Nenhum lead carregado')
        return
    
    print(f'\n## | {"Nome":<20} | {"Empresa":<20} | {"Email":<20}')
    for i, l in enumerate(leads):
        print(f'{i:<02d} | {l['name']:<20} | {l['company']:<20} | {l['email']:<20}')

def search_lead():
    input_serach = input('Buscar por:\t').strip().lower() # strip limpa espaços desnecessários

    if not input_serach:
        print('\nConsulta vázia')
        search_lead()

    leads = lead_backend.list_leads()
    results = []

    for i, l in enumerate(leads):
        lead_str = f'{l['name']} | {l['company']} | {l['email']}'.lower()

        if input_serach in lead_str:
            results.append(l)

    if not results:
        print('\nNada encontrado')
        return
    
    print(f'\n## | {"Nome":<20} | {"Empresa":<20} | {"Email":<20}')
    for i, l in enumerate(results):
        print(f'{i:<02d} | {l['name']:<20} | {l['company']:<20} | {l['email']:<20}')

def to_csv():
    path_csv = lead_backend.export_csv()
    if path_csv is None:
        print('Erro ao exportar o CSV... Feche o arquivo e tente novamente')
    else:
        print(f'Sucesso! CSV Exportado para: {path_csv}')

def main():
    while True:
        print_menu()
        op = int(input('\nEscolha:\t'))
        if op == 1:
            add_lead()
        elif op == 2:
            list_lead()
        elif op == 3:
            search_lead()
        elif op == 4:
            to_csv()
        elif op == 0:
            print('Até mais!')
            break
        else:
            print('Opção inválida')
    
def print_menu():
    print('\nMini CRM de Leads - (Adicionar/Listar)\n' \
    '\n[1] Adicionar lead' \
    '\n[2] Listar leads' \
    '\n[3] Buscar Lead' \
    '\n[4] Exportar para CSV' \
    '\n[0] Sair')

if __name__ == '__main__':
    main()