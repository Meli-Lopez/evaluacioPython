#se define una clase llamda votante
class Votante:
    def __init__(self, id, nombre):#se definen los parametros, constructor __init__ para inicializar los parametros
        self.id = id
        self.nombre = nombre
        self.voto = None  #se define el voto en none que significa que aun no ha votado y no tiene valor
#se define una clase llama sistemaVotacion
class SistemaVotacion:
    def __init__(self):
        self.votantes = []#se crea una lista vacia para almacenar los votantes que se vayan resgistrando
        self.candidatos = {"Bella": 0, "Willi": 0, "Rebecca": 0, "Voto en blanco": 0}#se crea un diccionario donde se establece los nombres de los candidatos y el 0 indica el valor de votos que tiene cada candidato
#se define un metodo llamado registrarVotante 
    def registrarVotante(self, id, nombre):#se definen los parametros 
        votante = Votante(id, nombre)
        self.votantes.append(votante)#se agrega el nombre y id registrado por el votante a la lista Votante
        print(f"Votante {nombre} se ha registrado correctamente")#se imprime un mensaje con el nombre del votante y que ha sido registrado correctamente
#se define un metodo llamado votar
    def votar(self, id, candidato):#se definen los parametros 
        for votante in self.votantes:#este bucle itera en la clase votante 
            if votante.id == id and votante.voto is None:#verifica con el id si existe el votante 
                votante.voto = candidato
                self.candidatos[candidato] += 1#en caso de que si se incrementa el voto al candidato elegido
                print(f"Voto de {votante.nombre} registrado para {candidato}.")
                return True#retorna verdadero
            elif votante.id == id and votante.voto is not None:#en caso de que ya haya votado 
                print(f"El votante {votante.nombre} ya ha votado.")#mostrara un mensaje donde indica que ya voto
                return False#retorna en falso
        print("El votante no ha sido encontrado en la base de datos")
        return False
#se define metodo mostrarREsultados
    def mostrarResultados(self):
        print("\nResultados de la votacion:")
        for candidato, votos in self.candidatos.items():
            print(f"{candidato}: {votos} votos")

        numMaxVotos = max(self.candidatos.values())
        ganadores = [candidato for candidato, votos in self.candidatos.items() if votos == numMaxVotos]

        if len(ganadores) == 1:
            print(f"\nEl ganador es: {ganadores[0]} con {numMaxVotos} votos.")
        else:
            print("\nEmpate entre los siguientes candidatos:")
            for ganador in ganadores:
                print(f"{ganador} con {numMaxVotos} votos.")

# Función principal
def main():
    sistema = SistemaVotacion()

    while True:
        print("\nMenu de Votacion:")
        print("A. Registrar votante")
        print("B. Ingresar al sistema de votacion")
        print("C. Votar en blanco")
        print("D. Mostrar resultados")
        print("S. Salir")

        opcion = input("Seleccione una opcion: ")

        if opcion.lower() == "a":
            id = input("Ingrese el numero del ID del votante: ")
            nombre = input("Ingrese el nombre del votante: ")
            sistema.registrarVotante(id, nombre)
        elif opcion.lower() == "b":
            id = input("Ingrese el ID del votante: ")
            print("los candidatos son: (Bella,Willi,Rebecca )")
            candidato = input("Ingrese el nombre del candidato: ")
            sistema.votar(id, candidato)
        elif opcion.lower() == "c":
            id = input("Ingrese el numero de ID del votante: ")
            sistema.votar(id, "Voto en blanco")
        elif opcion.lower()== "d":
            sistema.mostrarResultados()
        elif opcion.lower() == "s":
            print("El programa ha finalizado con exito!!! :D")
            break
        else:
            print("La opcion que selecciono no es valida , selecciona una de las opciones del menu")

if __name__ == "__main__":
    main();