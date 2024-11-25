import matplotlib.pyplot as plt
import math
import numpy as np

#функція для зчитування датасету
def read_dataset(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split())
            points.append((x, y))
    return points
 
#функція для афінних перетворень
def rotate_points(points, center, angle_deg):
    angle_rad = np.radians(angle_deg)
    cos_a, sin_a = np.cos(angle_rad), np.sin(angle_rad) 

    cx, cy = center

    # перенесення кожної точки на -сx та -cy координат 
    T1 = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [-cx, -cy, 1 ]
    ])

    # обертання об'єкта на заданий кут 
    R =  np.array([
        [cos_a, sin_a, 0],
        [-sin_a, cos_a, 0],
        [0, 0, 1 ]
    ])

    T2 = np.array([
        [1, 0, 0],
        [0, 1, 0],
        [cx, cy, 1 ]
    ])

    # Композиція перетворень
    M = np.dot(T1, R)
    M = np.dot(M, T2)  
    
    rotated_points = []
    for x, y in points:
        point = np.array([x, y, 1])

        # Застосування матриці перетворення
        rotated_point = np.dot(point, M) 

        # Додаємо результати
        rotated_points.append((rotated_point[0], rotated_point[1]))
    
    return rotated_points


# Функція для візуалізації точок та збереження
def plot_points_and_save(points, output_path):
    x_coords, y_coords = zip(*points)
    
    canvas_width, canvas_height = 960, 960
    dpi = 100 
    figsize = (canvas_width / dpi, canvas_height / dpi)

    plt.figure(figsize = figsize)

    plt.scatter(x_coords, y_coords, c='blue', s=10)
    plt.title("Координатна площина з точками", fontsize = 14)
    plt.xlabel("X", fontsize = 12)
    plt.ylabel("Y", fontsize = 12)

    plt.xlim(0, canvas_width)
    plt.ylim(0, canvas_height)

    plt.savefig(output_path, dpi = dpi)
    print(f"Графік збережено у файл: {output_path}")
    plt.show()

def main():
    dataset_file = "DS7.txt"
    output_file = "result.png"
    center = (480, 480)
    angle = 18  

    #зчитуємо датасет
    points = read_dataset(dataset_file)
    
    # plot_points_and_save(points, output_file)

    #обертаємо точки
    rotated_points = rotate_points(points, center, angle)

    #будуємо зобаження та зберігаємо
    plot_points_and_save(rotated_points, output_file)

if __name__ == '__main__':
    main()