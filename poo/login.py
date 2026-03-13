import json

class Usuario:
    def __init__(self, email, password):
       self.email = email
       self.password = password

arquivo_json = "usuarios.json"

def validador_usuario(email):
    try:
        with open(arquivo_json, "r") as file:
            usuarios = json.load(file)
    except FileNotFoundError:
        return False

    for usuario in usuarios:
        if usuario["email"] == email:
            print("You have a email in my login")
            return True
    return False 


entrada_email = input("Input your email: ")
if validador_usuario(entrada_email) == True:
    entrada_senha = input("Input your password: ")


user = [{
    "email" : entrada_email,
    "password" : entrada_senha 
}]
with open(arquivo_json, "w") as file:
    json.dump(user, file, ensure_ascii=False, indent=2)

usuarios_recebidos = []
with open(arquivo_json, "r") as file:
    for login in json.load(file):
        usuario_recebido = Usuario(**login)
        usuarios_recebidos.append(usuario_receblido)

for usuario in usuarios_recebidos:
    print(f"Email: {usuario.email} \nSenha: {usuario.password}")