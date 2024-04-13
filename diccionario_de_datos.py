
import itertools
import time
inicio = time.time() 
def generate_combinations():
    alphabet = 'ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789'
    for combination in itertools.product(alphabet, repeat=4):
        yield ''.join(combination)

def save_combinations_to_file(filename):
    with open(filename, 'w') as file:
        for combination in generate_combinations():
            file.write(combination + '\n')

# Nombre del archivo donde deseas guardar las combinaciones
filename = 'combinaciones.txt'

# Llamamos a la función para guardar las combinaciones en el archivo
save_combinations_to_file(filename)

print(f"Todas las combinaciones han sido guardadas en el archivo '{filename}'.")
fin = time.time()  # Marca el final del código
tiempo_transcurrido = fin - inicio
print(f"Tiempo transcurrido: {tiempo_transcurrido:.6f} segundos")