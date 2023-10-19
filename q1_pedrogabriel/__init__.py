notas = {
"100" : 1000,
"50" : 1500,
"20" : 800
}
alugueis = {}
users = {
"as" : "senha",
"asclepiades_braz" : "senhamuitofraca"
}
printcarlist = lambda : print("Lista de notas disponiveis: ")
sacaroudepositar = lambda : int(input("Sacar digite 1; Depositar digite 2;"))
depositar = lambda : print("deposito concluido!")

interacao = lambda resposta, notas ,guser: resposta == 1 and carstorent(notas,guser) or resposta == 2 and depositar()

allnotas = lambda notas : print([k + " Reais, qtd disponivel:" + str(notas[k]) for k in notas.keys()])
cin = lambda : input("Qual o valor do saque? ")
msg = lambda c, notas ,guser: (c in notas.keys() and print("Operação concluidam ;") and (notas.update({guser: notas[guser] - c}))) or (not c in notas.keys() and print("nota indisponivel..."))

carstorent = lambda notas, guser : printcarlist() or allnotas(notas) or msg(cin(), notas, guser)
getuser = lambda : input("What is your e-mail address? ")
getpassword = lambda : input("What is your password? ")
blocked = lambda : print("Access blocked. Non-existent user or user name and password do not match...")
allowed = lambda : print("Access allowed")
cond2 = lambda user : not user in users.keys()
cond = lambda user, gpassword : not users[user] == gpassword
login = lambda users, guser, gpassword, notas : blocked() if cond2(guser) else (cond(guser, gpassword) and blocked()) or ((not cond(guser, gpassword)) and (allowed() or interacao(sacaroudepositar(),notas,guser) ))
login(users, getuser(), getpassword(), notas)