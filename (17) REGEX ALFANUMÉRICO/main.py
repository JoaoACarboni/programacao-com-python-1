import re
codigo = "9999"
if re.fullmatch(r"[a-z0-9]{5}", codigo):
    print("Código aceito!")
else:
    print("Código inválido!")

