import random 
import math 

""""
cities = ["A", "B", "C", "D", "E"]  
distances = {  
    "A": {"A": 0, "B": 5, "C": 9, "D": 10, "E": 6},  
    "B": {"A": 5, "B": 0, "C": 4, "D": 8, "E": 7},  
    "C": {"A": 9, "B": 4, "C": 0, "D": 3, "E": 2},  
    "D": {"A": 10, "B": 8, "C": 3, "D": 0, "E": 1},  
    "E": {"A": 6, "B": 7, "C": 2, "D": 1, "E": 0}  
}
"""  
""
cities = ["A", "B", "C", "D", "E", "F", "G", "H"]  
distances = {
   "A": {"A": 0, "B": 328, "C": 259, "D": 180, "E": 314, "F": 294, "G": 269, "H": 391},
   "B": {"A": 328, "B": 0, "C": 83, "D": 279, "E": 107, "F": 131, "G": 208, "H": 136},
   "C": {"A": 259, "B": 83, "C": 0, "D": 257, "E": 70, "F": 86, "G": 172, "H": 152},
   "D": {"A": 180, "B": 279, "C": 257, "D": 0, "E": 190, "F": 169, "G": 157, "H": 273},
   "E": {"A": 314, "B": 107, "C": 70, "D": 190, "E": 0, "F": 25, "G": 108, "H": 182},
   "F": {"A": 294, "B": 131, "C": 86, "D": 169, "E": 25, "F": 0, "G": 84, "H": 158},
   "G": {"A": 269, "B": 208, "C": 172, "D": 157, "E": 108, "F": 84, "G": 0, "H": 140},
   "H": {"A": 391, "B": 136, "C": 152, "D": 273, "E": 182, "F": 158, "G": 140, "H": 0},
}
""
# Tabu Search Parámetros 
tabu_list = []  
tabu_tenure = 5  
max_iterations = 100  
  
# Primera solución  
current_solution = (random.sample(cities, len(cities)),0,0)  
best_solution = current_solution[0].copy()
print("1 Best Solution :", best_solution)   
  
# Evaluar el fitness de una solución (total_distance)  
def evaluate(solution):  
    total_distance = 0  
    for i in range(len(solution)):  
        current_city = solution[i]  
        next_city = solution[(i + 1) % len(solution)]  
        total_distance += distances[current_city][next_city]  
    return total_distance  

def cambioCamino(cam,h,k):
    for i in range(0,math.ceil((k-h)/2)):
        cam[h+i], cam[k-i] = cam[k-i], cam[h+i]
    return cam
  
# Main Tabu Search Loop  
iteration = 0  
while iteration < max_iterations:  
    # Soluciones vecinas  
    neighbors = []  
    for i in range(len(current_solution[0])):  
        for j in range(i + 1, len(current_solution[0])):  
            # Crea un vecino dando la vuelta al camino entre dos ciudades  
            neigh = current_solution[0].copy()  
            neigh = cambioCamino(neigh,i,j) # Cambia el camino entero entre i y j
            neighbors.append((neigh,i,j))  
  
    # Evaluar las soluciones vecinas y elegir la mejor  
    best_neighbor = None  
    best_fitness = float('inf')  
    for neighbor in neighbors:  
        # Evaluar el firness de las soluciones vecinas 
        fitness = evaluate(neighbor[0])  
        # Ver si no están en la lista tabu y tienen mejor fitness 
        if (neighbor[0][neighbor[1]],neighbor[1],neighbor[0][neighbor[2]],neighbor[2]) not in tabu_list and fitness < best_fitness:  
            bn = neighbor  
            best_fitness = fitness  
            
    # Guardar en la lista tabu
    tabu_list.append((bn[0][bn[1]],bn[1],bn[0][bn[2]],bn[2]))  # Guarda (nombre de ciudad 1, posición, nombre de ciudad 2, posición)
    if len(tabu_list) > tabu_tenure:  
        # Quita el elemento más viejo de la lista tabu
        tabu_list.pop(0) 
  
    # Actualizar la solución
    current_solution = bn  
    if best_fitness < evaluate(best_solution):  
        best_solution = bn[0]
        print("Best Solution:", best_solution)   
        
 
  
    iteration += 1  
 
print("Best Solution:", best_solution)  
print("Total Distance:", evaluate(best_solution)) 
print(iteration)