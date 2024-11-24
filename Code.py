import matplotlib.pyplot as plt

#функція для зчитування датасету
def read_dataset(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
                x, y = map(int, line.strip().split())
                points.append((x, y))
    return points

def plot_points_and_save(dataset_path, output_path):
    """
    Відображає точки з датасету на координатній площині та зберігає графік у файл.

    Функція зчитує пари координат точок із заданого текстового файлу, будує графік із точками 
    на координатній площині, показує його на екрані та зберігає у файл у форматі PNG.

    Параметри:
    -----------
    dataset_path : str
        Шлях до текстового файлу, який містить координати точок .
    output_path : str
        Шлях до файлу для збереження зображення.
    """
    
    # Зчитуємо координати
    points = read_dataset(dataset_path)
    
    # Якщо немає точок у файлі
    if not points:
        print("Файл порожній або не містить правильних даних.")
        return
    
    #Витягуємо координати X і Y
    x_coords, y_coords = zip(*points)
    
    #Створюємо полотно
    canvas_width, canvas_height = 960, 540
    dpi = 100  # Щільність точок на дюйм
    figsize = (canvas_width / dpi, canvas_height / dpi)

    plt.figure(figsize = figsize)


    #виводимо точки
    plt.scatter(x_coords, y_coords, color = 'black', s = 10)

    #налаштовуємо вигляд графіка
    plt.title("Координатна площина з точками", fontsize = 14)
    plt.xlabel("X", fontsize = 12)
    plt.ylabel("Y", fontsize = 12)

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
