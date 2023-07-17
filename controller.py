import os
import citasmedicas
import core
Activate=True
dataCitas={"data":[]}
if __name__=="__main__":
    while(Activate):
        os.system("clear")
        print("GESTION CITAS MEDICAS\n 1. Agregar Citas Medicas.\n 2. Buscar Citas Medicas.\n 3. Modificar Citas Medicas.\n 4. Cancelar Citas Medicas.\n 5. Salir del Programa")
        Passive=True
        while(Passive):
            try:
                opcion=int(input(("Digite la Opcion: ")))
            except ValueError:
                print("Digitos Invalidos")
            else:
                Passive=False  
        if(opcion==1):
            citasmedicas.LoadInfoCitas()
            citasmedicas.AddCitas()
        elif(opcion==2):
            citasmedicas.LoadInfoCitas()
            citasmedicas.BuscarCita()
        elif(opcion==3):
            citasmedicas.LoadInfoCitas()
            citasmedicas.ModificarCita()
        elif(opcion==4):
            citasmedicas.LoadInfoCitas()
            citasmedicas.CancelarCita()
        elif(opcion==5):
            print("CERRANDO PROGRAMA HASTA PRONTO...")
            input("Digite una tecla para continuar... ")
            Activate=False
        else:
            print("Opcion Inexistente")
            input("Digite una tecla para continuar... ")
        