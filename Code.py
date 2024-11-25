import matplotlib.pyplot as plt

#функція для зчитування датасету
def read_dataset(file_path):
    points = []
    with open(file_path, 'r') as file:
        for line in file:
                x, y = map(int, line.strip().split())
                points.append((x, y))
    return points

def main():
    dataset_file = "DS7.txt"
    output_file = "rotated_result.png"

if __name__ == '__main__':
    main()