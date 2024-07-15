import re
from validate_docbr import CPF, CNPJ

def is_valid_cpf_or_cnpj(doc):
    # Verifica se o documento é CPF
    cpf_validator = CPF()
    if cpf_validator.validate(doc):
        return True
    
    # Verifica se o documento é CNPJ
    cnpj_validator = CNPJ()
    if cnpj_validator.validate(doc):
        return True
    
    # Se não for válido nem CPF nem CNPJ, retorna False
    return False

def is_valid_cep(cep):
    return bool(re.match(r'^\d{5}-\d{3}$', cep))

def is_valid_telefone(telefone):
    return bool(re.match(r'^\(\d{2}\) \d{5}-\d{4}$', telefone))

