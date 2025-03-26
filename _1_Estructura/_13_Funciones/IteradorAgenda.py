def iterador_agenda(agenda:list):
    i: int = 0
    while i < len(agenda):
        nombre,correo,tel = agenda[i]
        i+=1
        yield nombre,correo,tel

if __name__ == '__main__':
    agenda = []

    agenda.append(("juan1","juan1@gmail.com","2225869881"))
    agenda.append(("juan2","juan2@gmail.com","2225869882"))
    agenda.append(("juan3","juan3@gmail.com","2225869883"))
    agenda.append(("juan4","juan4@gmail.com","2225869884"))
    agenda.append(("juan5","juan5@gmail.com","2225869885"))
    agenda.append(("juan6","juan6@gmail.com","2225869886"))
    agenda.append(("juan7","juan7@gmail.com","2225869887"))
    agenda.append(("juan8","juan8@gmail.com","2225869888"))
    agenda.append(("juan9","juan9@gmail.com","2225869889"))
    agenda.append(("juan0","juan0@gmail.com","2225869880"))

    for a,b,c in iterador_agenda(agenda):
        print(f"\n------------------------\nNombre: {a}\nCorreo: {b}\nNúmero: {c}\n------------------------")
