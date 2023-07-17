import os
import core
import random
infoCitas={"data":[]}
def LoadInfoCitas():
    global infoCitas
    if(core.CheckFile("citasmedicas.json")):
        infoCitas=core.LoadInfo("citasmedicas.json")
    else:
        core.AddInfo("citasmedicas.json",infoCitas)
def AddCitas():
    Passive=True
    while(Passive):
        Pause=True
        while(Pause):
            os.system("clear")
            try:
                id=int(input("Digite el Id del Paciente correspondiente a la Cita Medica: "))
            except ValueError:
                print("Digitos Invalidos,solo se reciben Enteros")
                input("Digite una tecla para continuar... ")
            else:
                id=str(id)
                Pause=False
        Pause=True
        while(Pause):
            os.system("clear")
            try:
                nombre=input("Digite el Nombre del Paciente correspondiente a la Cita Medica: ").upper()
                nombre=int(nombre)
            except ValueError:
                nombre=str(nombre).strip()
                if(len(nombre)>0):
                    Pause=False
                else:
                    print("Digitos Invalidos,no pueden ser caracteres vacios")
                    input("Digite una tecla para continuar... ")
            else:
                print("Digitos Invalidos,solo se aceptan Strings")
                input("Digite una tecla para continuar... ")
        Pause=True
        while(Pause):
            os.system("clear")
            try:
                motivo=input("Digite el Motivo de la Consulta: ")
                motivo=int(motivo)
            except ValueError:
                motivo=str(motivo).strip()
                if(len(motivo)>0):
                    Pause=False
                else:
                    print("Digitos Invalidos,no pueden ser caracteres Vacios")
                    input("Digite una tecla para continuar... ")
            else:
                print("Digitos Invalidos,solo se reciben Strings")
                input("Digite una tecla para continuar... ")
        cita={
            "Id-Paciente":id,
            "Nombre-Paciente":nombre,
            "Id-Cita":str(random.randint(1,999)),
            "Fecha-Cita":str(core.RandomDate()),
            "Hora-Cita":str(core.RandomTime()),
            "Motivo-Consulta":motivo
        }
        infoCitas["data"].append(cita)
        core.AddInfo("citasmedicas.json",cita) 
        Passive=bool(input("Digite un caracter AlphaNumerico para volver a Buscar Citas o Presion Enter para Volver al Menu Principal "))
        
def BuscarCita():
    Passive=True
    while(Passive):
        os.system("clear")
        print("Busqueda Cita\n 1. Buscar por Id del Paciente.\n 2. Buscar por Nombre del Paciente.")
        Pause=True
        while(Pause):
            try:
                opcion=int(input("Digite la Opcion de Busqueda de la Cita: "))
            except ValueError:
                print("Digitos Invalidos,solo se aceptan Enteros")
                input("Digite una tecla para continuar... ")
            else:
                Pause=False
        if(opcion==1):
            Pause=True
            while(Pause):
                os.system("clear")
                try:
                    id=int(input("Digite el Id del Paciente de la Cita a Buscar: "))
                except ValueError:
                    print("Digitos Invalidos,solo se aceptan Enteros")
                    input("Digite una tecla para continuar... ")
                else:
                    id=str(id)
                    Pause=False
            for i,item in enumerate (infoCitas["data"]):
                if id==item["Id-Paciente"]:
                    print(" ")
                    print(f'Id Paciente: {item["Id-Paciente"]}')
                    print(f'Nombre Paciente: {item["Nombre-Paciente"]}')
                    print(f'Id Cita: {item["Id-Cita"]}')
                    print(f'Fecha Cita: {item["Fecha-Cita"]}')
                    print(f'Hora Cita: {item["Hora-Cita"]}')
                    print(f'Motivo Consulta: {item["Motivo-Consulta"]}')
                    print(" ")
                else:
                    print("Id Paciente Inexistente")
                    input("Digite una tecla para continuar... ")
        elif(opcion==2):
            Pause=True
            while(Pause):
                os.system("clear")
                try:
                    nombre=input("Digite el Nombre del Paciente para Buscar la Cita Medica: ").upper()
                    nombre=int(nombre)
                except ValueError:
                    nombre=str(nombre).strip()
                    if(len(nombre)>0):
                        Pause=False
                    else:
                        print("Digitos Invalidos,no pueden ser caracteres Vacios")
                        input("Digite una tecla para continuar... ")
                else:
                    print("Digitos Invalidos,solo se aceptan Strings")  
                    input("Digite una tecla para continuar... ")    
            for i,item in enumerate(infoCitas["data"]):
                if nombre==item["Nombre-Paciente"]:
                    print(" ")
                    print(f'Id Paciente: {item["Id-Paciente"]}')
                    print(f'Nombre Paciente: {item["Nombre-Paciente"]}')
                    print(f'Id Cita: {item["Id-Cita"]}')
                    print(f'Fecha Cita: {item["Fecha-Cita"]}')
                    print(f'Hora Cita: {item["Hora-Cita"]}')
                    print(f'Motivo Consulta: {item["Motivo-Consulta"]}')
                    print(" ")
        else:
            print("Opcion Inexistente")
            input("Digite una tecla para continuar... ")
        Passive=bool(input("Digite un caracter AlphaNumerico para volver a Buscar Citas o Presione Enter para Volver al Menu Principal"))
def ModificarCita():
    Passive=True
    while(Passive):
        os.system("clear")
        print("Modificar Cita\n 1. Modificar por Id del Paciente.\n 2. Modificar por Nombre del Paciente.")
        Pause=True
        while(Pause):
            try:
                opcion=int(input("Digite la Opcion de Modificar la Cita: "))
            except ValueError:
                print("Digitos Invalidos,solo se aceptan Enteros")
                input("Digite una tecla para continuar... ")
            else:
                Pause=False
        if(opcion==1):
            Pause=True
            while(Pause):
                os.system("clear")
                try:
                    id=int(input("Digite el Id del Paciente de la Cita a Modificar: "))
                except ValueError:
                    print("Digitos Invalidos,solo se aceptan Enteros")
                    input("Digite una tecla para continuar... ")
                else:
                    id=str(id)
                    Pause=False
            for i,item in enumerate (infoCitas["data"]):
                if id==item["Id-Paciente"]:
                    item["Motivo-Consulta"]=input("Digite el Nuevo Motivo de la Consulta o Presione Enter para Modificar: ")or item["Motivo-Consulta"]
                    core.EditarData("citasmedicas.json",infoCitas)
                else:
                    print("Id Paciente Inexistente") 
                    input("Digite una tecla para continuar... ")   
        elif(opcion==2):
            Pause=True
            while(Pause):
                os.system("clear")
                try:
                    nombre=input("Digite el Nombre del Paciente para Modificar la Cita Medica: ").upper()
                    nombre=int(nombre)
                except ValueError:
                    nombre=str(nombre).strip()
                    if(len(nombre)>0):
                        Pause=False
                    else:
                        print("Digitos Invalidos,no pueden ser caracteres Vacios")
                        input("Digite una tecla para continuar... ")
                else:
                    print("Digitos Invalidos,solo se aceptan Strings")  
                    input("Digite una tecla para continuar... ")    
            for i,item in enumerate(infoCitas["data"]):
                if nombre==item["Nombre-Paciente"]:
                    item["Motivo-Consulta"]=input("Digite el Nuevo Motivo de la Consulta o Presione Enter para Modificar: ")or item["Motivo-Consulta"]
                    core.EditarData("citasmedicas.json",infoCitas)
                else:
                    print("Nombre Paciente Inexistente")
                    input("Digite una tecla para continuar... ")
        else:
            print("Opcion Inexistente")
            input("Digite una tecla para continuar... ")
        Passive=bool(input("Digite un caracter AlphaNumerico para volver a Buscar Citas o Presione Enter para Volver al Menu Principal "))
    
def CancelarCita():
    Passive=True
    while(Passive):
        os.system("clear")
        print("Cancelar Cita\n 1. Cancelar por Id del Paciente.\n 2. Cancelar por Nombre del Paciente.")
        Pause=True
        while(Pause):
            try:
                opcion=int(input("Digite la Opcion de Cancelar la Cita: "))
            except ValueError:
                print("Digitos Invalidos,solo se aceptan Enteros")
                input("Digite una tecla para continuar... ")
            else:
                Pause=False
        if(opcion==1):
            Pause=True
            while(Pause):
                os.system("clear")
                try:
                    id=int(input("Digite el Id del Paciente de la Cita a Cancelar: "))
                except ValueError:
                    print("Digitos Invalidos,solo se aceptan Enteros")
                    input("Digite una tecla para continuar... ")
                else:
                    id=str(id)
                    Pause=False
            for i,item in enumerate (infoCitas["data"]):
                if id==item["Id-Paciente"]:
                    infoCitas["data"].pop(i)
                    core.EditarData("citasmedicas.json",infoCitas)
                else:
                    print("Id Paciente Inexistente") 
                    input("Digite una tecla para continuar... ")  
        elif(opcion==2):
            Pause=True
            while(Pause):
                os.system("clear")
                try:
                    nombre=input("Digite el Nombre del Paciente para Cancelar la Cita Medica: ").upper()
                    nombre=int(nombre)
                except ValueError:
                    nombre=str(nombre).strip()
                    if(len(nombre)>0):
                        Pause=False
                    else:
                        print("Digitos Invalidos,no pueden ser caracteres Vacios")
                        input("Digite una tecla para continuar... ")

                else:
                    print("Digitos Invalidos,solo se aceptan Strings")
                    input("Digite una tecla para continuar... ")
      
            for i,item in enumerate(infoCitas["data"]):
                if nombre==item["Nombre-Paciente"]:
                    infoCitas["data"].pop(i)
                    core.EditarData("citasmedicas.json",infoCitas)
                else:
                    print("Nombre Paciente Inexistente")
                    input("Digite una tecla para continuar... ")
        else:
            print("Opcion Inexistente")
            input("Digite una tecla para continuar... ")
        Passive=bool(input("Digite un caracter AlphaNumerico para volver a Buscar Citas o Presione Enter para Volver al Menu Principal "))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    
    
"""1. El programa debe tener un menú que permita al usuario seleccionar diferentes opciones:
agregar cita, buscar cita, modificar cita, cancelar cita y salir del programa.
2. Cada cita médica debe tener los siguientes datos: nombre del paciente, fecha de la cita,
hora de la cita y motivo de la consulta.
3. Al agregar una cita, el programa debe solicitar al usuario que ingrese los datos
correspondientes y luego guardar la cita en un archivo JSON.
4. Al buscar una cita, el programa debe solicitar al usuario un criterio de búsqueda (por
ejemplo, nombre del paciente o fecha de la cita) y mostrar todas las citas que coincidan
con ese criterio.
5. Al modificar una cita, el programa debe permitir al usuario seleccionar una cita de la lista
de citas y solicitar los nuevos datos para actualizarla en el archivo JSON.
6. Al cancelar una cita, el programa debe permitir al usuario seleccionar una cita de la lista
de citas y eliminarla del archivo JSON.
7. Al salir del programa, se deben guardar todos los cambios realizados en el archivo JSON
y mostrar un mensaje de despedida."""