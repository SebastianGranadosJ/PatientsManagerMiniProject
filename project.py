# **********************
# * VARIABLES GLOBALES *
# **********************
patients = {"Juan Sebastian":{"name": "Juan Sebastian", "age":18, "history": "Gastritis"},"Maria Jose":{"name": "Maria Jose", "age":20, "history": "Riñon malo"} }
running = True

# **********************
# *      FUNCIONES     *
# **********************

def enter_patient():
    print("*******************")
    print("Ingrese el nuevo paciente")
    print("*******************")
    print("")
    name = input("Ingrese el nombre del paciente: ")
    age = int(input("Ingrese la edad el paciente: "))
    history = input("Ingrese el historial clinico del paciente: ")
        
    patients[name] =  {"name": name, "age":age, "history":history}
    print("Usuario: " + name + " registrado exitosamente")

def list_patients():
    print("*******************")
    print("Lista de pacientes")
    print("*******************")
    for kpatient, patient in patients.items():
        print("------Paciente-----")
        for k, v in patient.items():
           
            print(k, "->\t", v)

def search_patient():
    print("*******************")
    print("Buscar paciente por nombre")
    print("*******************")

    patient_name = input("Ingrese el nombre del paciente que desea buscar: ")

    if(patient_name in patients):
        print("Esta es la infomracion del paciente que busca: ")
        patient = patients[patient_name]
        print("Nombre: " + patient["name"])
        print("Edad:" , patient["age"])
        print("Historial clinico: " + patient["history"])
    else:
        print("No se ha encontrado un paciente con ese nombre")

def show_menu():
    print("")
    print("")
    print("")
    print("")
    print("1. 🔵 Ingresar paciente")
    print("2. 🔵 Buscar paciente por nombre")
    print("3. 🔵 Listar paciente")
    print("4. 🔵 Salir")
    response = int(input("Ingres el numero de la funcion que desea ejecutar: "))
    return response


       


# **********************
# *      EJECUCION     *
# **********************

print("\t\t##########################################################")
print("\t\t\tBIENVENIDO AL SISTEMA DE HISTORIAS CLINICAS")
print("\t\t##########################################################")
while running:
    response = show_menu()
    if response == 1:
        enter_patient()
    elif response == 2:
        search_patient()
    elif response == 3:
        list_patients()
    elif response == 4:
        running = False
        print("Se ha finalizado la ejecucion del programa")
    else:
        print("Entrada no valida")
        

    

    

    


