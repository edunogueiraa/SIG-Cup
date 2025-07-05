def validar_cpf(cpf): #Creditos Flavius

    #Deixar só numeros
    cpf = cpf.replace('.', '')
    cpf = cpf.replace('-', '')
    cpf = cpf.replace(' ', '')
    
    tam = len(cpf)
    soma = 0
    d1 = 0
    d2 = 0

    #Verificando se tudo é digito
    if not(cpf.isdigit()):
        return False

    if tam != 11:
        return False
    
    for i in range(11):
        if (cpf[i]<'0') or (cpf[i]>'9'):
            return False
        
    for i in range(9):
        soma += (int(cpf[i]) * (10 - i))

    d1 = 11 - (soma % 11)

    if (d1 == 10 or d1 == 11):
        d1 = 0
    
    if d1 != int(cpf[9]):
        return False
    
    soma = 0
    for i in range(10):
        soma += (int(cpf[i])*(11 - i))

    d2 = 11 - (soma%11)
    if (d2 == 10 or d2 == 11):
        d2 = 0
    
    if d2 != int(cpf[10]):
        return False
    
    return True


def validar_nome(nome):
  nome = nome.replace(' ', '')
  return bool(nome.isalpha())

def validar_telefone(telefone):
  telefone = telefone.replace(' ', '')
  telefone = telefone.replace('-', '')
  telefone = telefone.replace('(', '')
  telefone = telefone.replace(')', '')
  telefone = telefone.replace('+', '')
  tam = len(telefone)
  if tam < 11:
    return False
  if not(telefone.isdigit()):
    return False
  
  return True

