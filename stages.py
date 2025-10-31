from datetime import date

STAGES = ['novo']
DEFAULT_STAGE = 'novo'

def model_lead(name, company, email):
    """Cria um lead como um dicionário simples"""
    return {
        "name":name,
        "company":company,
        "email":email,
        "stage":"novo",
        "created_at":date.today().isoformat()
    }
