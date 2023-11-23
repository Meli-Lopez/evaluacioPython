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
#se define metodo mostrarResultados
    def mostrarResultados(self):
        print("\nResultados de la votacion:")
        for candidato, votos in self.candidatos.items():#itera el nombre del candidato en los votos
            print(f"{candidato}: {votos} votos")#imprie nombre del candidato y cantidad de los votos

        numMaxVotos = max(self.candidatos.values())#calcula el numero maximo de votos
        ganadores = [candidato for candidato, votos in self.candidatos.items() if votos == numMaxVotos]#se crea una variable ganadores para que muestre el cambio del candidato que gane

        if len(ganadores) == 1: #se utiliza el metodo len para la longitud de la lista
            print(f"\nEl ganador es: {ganadores[0]} con {numMaxVotos} votos.")#imprime al ganador de la lista
        else:
            print("\nEmpate entre los siguientes candidatos:")#en caso de que haya empate imprime los empates y la cantidad  de votos
            for ganador in ganadores:
                print(f"{ganador} con {numMaxVotos} votos.")

# se define la funcion principal
def main():
    sistema = SistemaVotacion()
#se crea el menu con las respectivas opciones 
    while True:
        print("\nMenu de Votacion:")
        print("A. Registrar votante")
        print("B. Ingresar al sistema de votacion")
        print("C. Votar en blanco")
        print("D. Mostrar resultados")
        print("S. Salir")

        opcion = input("Seleccione una opcion: ")
#en caso de que sea a se registra al votante
        if opcion.lower() == "a":
            id = input("Ingrese el numero del ID del votante: ")
            nombre = input("Ingrese el nombre del votante: ")
            sistema.registrarVotante(id, nombre)
        elif opcion.lower() == "b":#en caso de que sea b ingresa con el id al sistema
            id = input("Ingrese el ID del votante: ")
            print("los candidatos son: (Bella,Willi,Rebecca )")#despues se muestra el nombre de los candidatos
            candidato = input("Ingrese el nombre del candidato teniendo en cuenta que los nombres empiezan con letra mayuscula: ")#selecciona uno de los nombres mostrados , 
            sistema.votar(id, candidato)
        elif opcion.lower() == "c":#en caso de que sea c votara en blanco
            id = input("Ingrese el numero de ID del votante: ")
            sistema.votar(id, "Voto en blanco")
        elif opcion.lower()== "d":#en caso de sea d se mostrar el resultado de las votaciones
            sistema.mostrarResultados()#llama al metodo mostrarResultados
        elif opcion.lower() == "s":#en caso de que sea s se terminara el programa
            print("El programa ha finalizado con exito!!! :D")
            break
        else:#se imprime el mensaje si la opcion seleccionada no esta en el menu
            print("La opcion que selecciono no es valida , selecciona una de las opciones del menu")

if __name__ == "__main__":
    main(); # el main se utiliza para manejar el menu
