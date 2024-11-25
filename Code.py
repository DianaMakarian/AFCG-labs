import matplotlib.pyplot as plt

#функція для зчитування датасету
def read_dataset(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
                x, y = map(int, line.strip().split())
                points.append((x, y))
    return points

# функція для виведення точок на екран та збереження у файл png
def plot_points_and_save(dataset_path, output_path): 
    # Зчитуємо координати
    points = read_dataset(dataset_path)
    x_coords, y_coords = zip(*points)
    
    #Створюємо полотно
    canvas_width, canvas_height = 960, 540
    dpi = 100 
    figsize = (canvas_width / dpi, canvas_height / dpi)
    plt.figure(figsize = figsize)

    #виводимо точки
    plt.scatter(x_coords, y_coords, color = 'black', s = 10)

    #налаштовуємо вигляд графіка
    plt.title("Координатна площина з точками", fontsize = 14)
    plt.xlabel("X", fontsize = 12)
    plt.ylabel("Y", fontsize = 12)
    plt.xlim(0, canvas_width)
    plt.ylim(0, canvas_height)

    #Зберігаємо результат у файл
    plt.savefig(output_path, dpi = dpi)  # Збереження з роздільною здатністю 96 DPI
    print(f"Графік збережено у файл: {output_path}")

    # показуємо та закриваємо картинку
    plt.show()
    plt.close()


def main():
    #шляхи до датасету, та шлях до файлу для збереження зображення
    dataset_file = "DS7.txt"  
    output_file = "result.png"  

    #побудова графіка
    plot_points_and_save(dataset_file, output_file)

if __name__ == '__main__':
    main()
