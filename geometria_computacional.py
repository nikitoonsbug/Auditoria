import numpy as np
import random
import matplotlib.pyplot as plt

class AccessPoint:
    def _init_(self, x, y, coverage_radius):
        self.x = x
        self.y = y
        self.coverage_radius = coverage_radius

def generate_random_points(num_points, min_x, max_x, min_y, max_y):
    points = []
    for _ in range(num_points):
        x = random.uniform(min_x, max_x)
        y = random.uniform(min_y, max_y)
        points.append((x, y))
    return points

def calculate_coverage_matrix(points, space_width, space_height, coverage_radius):
    coverage_matrix = np.zeros((space_height, space_width))

    for i in range(space_height):
        for j in range(space_width):
            for point in points:
                dist = np.sqrt((i - point[1]) ** 2 + (j - point[0]) ** 2)
                if dist <= coverage_radius:
                    coverage_matrix[i, j] += 1

    return coverage_matrix

def place_access_points(space_width, space_height, num_points, coverage_radius):
    min_x, max_x = 0, space_width
    min_y, max_y = 0, space_height

    random_points = generate_random_points(num_points, min_x, max_x, min_y, max_y)
    coverage_matrix = calculate_coverage_matrix(random_points, space_width, space_height, coverage_radius)

    best_coverage = np.max(coverage_matrix)
    best_points = random_points

    return best_points, best_coverage, coverage_matrix

# Parámetros del espacio y los puntos de acceso
space_width = 100
space_height = 100
num_points = 5
coverage_radius = 20

best_points, best_coverage, coverage_matrix = place_access_points(space_width, space_height, num_points, coverage_radius)

# Graficar el espacio y los puntos de acceso
plt.figure(figsize=(8, 8))
plt.imshow(coverage_matrix, cmap='viridis', origin='lower')
plt.colorbar(label='Cobertura de señal')
plt.scatter([point[0] for point in best_points], [point[1] for point in best_points], color='red', label='Puntos de acceso')
plt.xlabel('Ancho del espacio')
plt.ylabel('Altura del espacio')
plt.title('Distribución de puntos de acceso y cobertura de señal')
plt.legend()
plt.show()