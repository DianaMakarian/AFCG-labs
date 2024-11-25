import matplotlib.pyplot as plt
import math

# Функція для зчитування датасету
def read_dataset(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
            x, y = map(int, line.strip().split())
            points.append((x, y))
    return points
 
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
    
    #будуємо зобаження та зберігаємо
    plot_points_and_save(points, output_file)

if __name__ == '__main__':
    main()