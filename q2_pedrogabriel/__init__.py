alugueis = {}

with open("users.txt", "r") as file:
    # Leia as linhas do arquivo e crie um dicionário
    file_contents = file.readlines()

users = {}

for line in file_contents:
    parts = line.strip().split(":")
    if len(parts) == 2:
        username, password = parts[0], parts[1]
        users[username] = password



with open("users.txt", "w") as file:
    for username, password in users.items():
        file.write(f"{username}:{password}\n")

gravar_dicionario = lambda users, filename: (
  open(filename, "w").writelines(
    f"{user}:{passwd}\n" for user, passwd in users.items()
  )
)




print(users)

getuser = lambda : input("What is your e-mail address? ")
getpassword = lambda : input("What is your password? ")
blocked = lambda : print("Access blocked. Non-existent user or user name and password do not match...")
allowed = lambda : print("Access allowed")

cond2 = lambda user : not user in users.keys()
cond = lambda user, gpassword : not users[user] == gpassword

cadastro = lambda user , guser, gpassword : user.update({guser:gpassword}) and cadastrado() #and gravar_dicionario(user, "users.txt")
cadastrado = lambda : print("cadastrado com sucesso!!!!",users)

login = lambda user, guser, gpassword : blocked() if cond2(guser) else (cond(guser, gpassword) and blocked()) or ((not cond(guser, gpassword)) and (allowed()  ))
interacao = lambda resposta, notas ,guser: resposta == 1 and login() or resposta == 2 and cadastro()
login(users, getuser(), getpassword())
cadastro(users, getuser(), getpassword())
gravar_dicionario(users, "users.txt")
print(users)