from datetime import date

COMPANIES = []

def model_user(name, data_nasc, idade, tipo_sang, email='', working_on='nenhuma'):
    if hasattr(data_nasc, 'isoformat'):
        birthdate = data_nasc.isoformat()
    else:
        birthdate = data_nasc

    return {
        "name": name,
        "birthdate": birthdate,
        "age": idade,
        "email": email,
        "blood_type": tipo_sang,
        "working_on": working_on,
    }

def model_company(name, descr, nota, employees=0):
    return {
        "name": name,
        "caption": descr,
        "rate": nota,
        "employees": employees,
    }
