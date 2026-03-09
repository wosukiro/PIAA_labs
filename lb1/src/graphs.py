import matplotlib.pyplot as plt
from main import main
import time

if __name__ == "__main__":
    metrics = []
    sizes = list(range(2, 28))
    for i in sizes:
        start = time.time()
        print("")
        print(f"---- Solve for N = {i} ----")
        main(i)
        end = time.time()
        metrics.append(end-start)
    
    plt.figure(figsize=(12, 6))

    plt.plot(sizes, metrics, label="Время поиска", color="black")
    plt.plot(sizes, metrics, "bo", color="red")

    plt.title("Зависимость времени поиска разбиения от размера квадрата")
    plt.xlabel("Размер квадрата N")
    plt.ylabel("Время выполнения (сек)")

    plt.xticks(sizes)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()


    for x, y in zip(sizes, metrics):
        plt.text(x, y, f"{y:.2f}", fontsize=8)
    
    plt.tight_layout()
    plt.show()