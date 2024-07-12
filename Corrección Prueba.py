#Prueba Parcial 3 [Javiera Aguilar]
#0. Funciones de Validación
def ValidarVerificador(Rut: str) -> str:
    from itertools import cycle
    reversa = map(int, reversed(str(Rut)))
    ciclo = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversa, ciclo))
    verificador = (-s) % 11
    if verificador == 10:
        return 'k'
    elif verificador == 11:
        return '0'
    else:
        return str(verificador)

def ValidarFormatoRut(Rut: str) -> bool:
    Rut = Rut.lower()
    if len(Rut) < 3 or "-" not in Rut:
        return False
    numero, digito = Rut.rsplit("-", 1)
    numero = numero.replace(".", "")
    if not numero.isnumeric() or len(numero) < 7 or len(numero) > 8:
        return False
    return digito == ValidarVerificador(numero)

#1. Registro Estudiantes
def RegistroEstudiante()-> tuple:
    print("""[Registro de Estudiante]
        \r Ingrese los datos solicitados en los formatos correctos.""")
    try:
        Rut = input("Ingrese el Rut del Estudiante (11.111.111-1): ")
        assert ValidarFormatoRut(Rut), "El RUT fue ingresado en un formato incorrecto." 
        Nombre = input("Ingrese el nombre del Estudiante: ").capitalize()
        assert Nombre.isalpha(), "Ingreso caracteres númericos."
        Nota1 = input("Ingrese la Calificación N°1 (Ejemplo: 70): ")
        assert Nota1.isnumeric(), "No ingreso un valor numérico"
        Nota1 = int(Nota1)    
        assert 0 <= Nota1 <= 70, "La nota no corresponde con un valor permitido"
        Nota2 = input("Ingrese la Calificación N°2 (Ejemplo: 70): ")
        assert Nota2.isnumeric(), "No ingreso un valor numérico"
        Nota2 = int(Nota2)
        assert 0 <= Nota2 <= 70, "La nota no corresponde con un valor permitido"
        Nota3 = input("Ingrese la Calificación N°3 (Ejemplo: 70): ")
        assert Nota3.isnumeric(), "No ingreso un valor numérico"
        Nota3 = int(Nota3)
        assert 0 <= Nota3 <= 70, "La nota no corresponde con un valor permitido"
        Nota4 = input("Ingrese la Calificación N°4 (Ejemplo: 70): ")
        assert Nota4.isnumeric(), "No ingreso un valor numérico"
        Nota4 = int(Nota4)
        assert 0 <= Nota4 <= 70, "La nota no corresponde con un valor permitido"
        NotaPresentación = int((Nota1 * 0.30) + (Nota2 * 0.30) + (Nota3 * 0.30) + (Nota4 * 0.10))
        NotaExamen = input("Ingrese la Calificación del Examen (Ejemplo: 70): ")
        assert NotaExamen.isnumeric(), "No ingreso un valor numérico"
        NotaExamen = int(NotaExamen)
        assert 0 <= NotaExamen <= 70, "La nota no corresponde con un valor permitido"
        NotaExamen = int(NotaExamen)
        NotaFinal = int((NotaPresentación * 0.6) + (NotaExamen * 0.4))
        Estado = "Aprobado" if NotaFinal >= 40 else "Reprobado"
        print("\n Registro Completado Correctamente")
        return (Rut, Nombre,int(Nota1),int(Nota2),int(Nota3),int(Nota4),NotaPresentación,NotaFinal,Estado)
    except AssertionError as e:
       print(f"\n Ha ocurrido un ERROR: {e} \n Vuelva a intentarlo.")
    return None
#2.	Visualización de Todos los Estudiantes
def ListaEstudiantes(ListaEstudiantes:list)->None:
    if len(ListaEstudiantes) > 0:
        Campos=("N°","RUT","Nombre","Nota N°1","Nota N°2","Nota N°3","Nota N°4","Nota Presentación","Nota Final","Estado")#0,1.2.3.4.5.6.7,8 lista cifra
        print(f"\n{Campos[0].center(5)}{Campos[1].center(15)}{Campos[2].center(16)}{Campos[3].center(13)}{Campos[4].center(15)}{Campos[5].center(10)}{Campos[6].center(15)}{Campos[7].center(20)}{Campos[8].center(17)}{Campos[9].center(12)}")
        k = 1
        for i in ListaEstudiantes:
            print(f"{str(k).center(5)}", end="")
            for j in i:
                print(f"{str(j).center(15)}", end="")
            print()
            k += 1
    else:
        print("No has registrado estudiantes nuevos.")

#3.	Buscar Estudiante Por RUT
from colorama import Fore
def BuscarEstudiantes(ListaEstudiantes: list) -> None:
    if len(ListaEstudiantes) == 0:
        print("No hay estudiantes registrados.")
        return None
    try:
        BuscarRut = input("\nIngrese el RUT que desea buscar en nuestros registros (11.111.111-1): ")
        assert ValidarFormatoRut(BuscarRut), "El formato del RUT fue ingresado incorrectamente."
        encontrado = False
        for Estudiante in ListaEstudiantes:
            if Estudiante[0] == BuscarRut:
                encontrado = True
                print("\n" + "="*80)
                print("Información del Estudiante".center(80))
                print("="*80)
                print(f"Nombre: {Estudiante[1]} - RUT: {Estudiante[0]}".center(80))
                print("="*80)

                print(f"{'Nota 1:':<15} {Estudiante[2]:<5} {'Nota 3:':<15} {Estudiante[4]:<5} {'Nota de Presentación:':<20} {Estudiante[6]}")
                print(f"{'Nota 2:':<15} {Estudiante[3]:<5} {'Nota 4:':<15} {Estudiante[5]:<5} {'Nota Final:':<20} {Estudiante[7]}")
                print("="*80)

                if Estudiante[8] == "Aprobado":
                    estado = f"Estado: {Fore.GREEN}{Estudiante[8]}{Fore.RESET}"
                else:
                    estado = f"Estado: {Fore.RED}{Estudiante[8]}{Fore.RESET}"
                print(f"{estado.center(80)}")
                print("="*80)
                break
        assert encontrado, f"No se encontró ningún estudiante con el RUT {BuscarRut}."
    except AssertionError as e:
        print(f"\nError: {e}\nPor favor, inténtelo nuevamente.")

#4.	Exportación a CSV
def ExportarEstudiantes(ListaEstudiantes:list)->None:
    if len(ListaEstudiantes) > 0:
        from os import listdir
        if "RespaldoRegistro.cvs" not in listdir():
            with open("RespaldoEstudiantes.csv","a",newline="") as archivo_csv:
                archivo_csv.write("N°","Rut","Nombre","Nota 1","Nota 2","Nota 3","Nota 4","Nota Presentación","Nota Final")
    
        with open("RespaldoEstudiantes.csv","a",newline="") as archivo_csv:
            for i in range(len(ListaEstudiantes)): 
                ListaEstudiantes[i] = ",".join(ListaEstudiantes[i])
                archivo_csv.write(ListaEstudiantes[i] + "\n")
        print("[Registros respaldados en \"RespaldoEstudiantes.csv\"]")
        del ListaEstudiantes[:]
    else:
        print("No hay Registro para respaldar.")
    
#Menú #Revisar porque no toma
total_registros = list()
copia_registros = list()
while True:
    try:
        print("""[Sistema de Calificaciones de Estudiantes]
            \r 1. Registro de Estudiante 
            \r 2. Visualización de Todos los Estudiantes
            \r 3. Buscar Estudiante Por RUT
            \r 4. Exportación a CSV notas de Estudiantes
            \r 5. Salir del Programa""")
        opción = input("\n -> Ingrese la opción que desee seleccionar:  ")
        assert opción in ("1","2","3","4","5"), "Opción Invalida"
        if opción == "1":
            estudiante_nuevo = RegistroEstudiante()
            if estudiante_nuevo is not None:
                total_registros.append(estudiante_nuevo)
                copia_registros.append(estudiante_nuevo)
        elif opción == "2":
            ListaEstudiantes(copia_registros)
        elif opción == "3":
            BuscarEstudiantes(total_registros)
        elif opción == "4":
            ExportarEstudiantes(total_registros)
        elif opción == "5":
            print("Saliendo del Programa. . .")
            break
    except AssertionError as e:
        print(f"\n Ha ocurrido un ERROR: {e} \n Vuelva a intentarlo...")