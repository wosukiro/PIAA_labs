import matplotlib.pyplot as plt
from main import main
import time

if __name__ == "__main__":
    metrics = []
    sizes = list(range(2, 31))
    measurements_count = 5

    for i in sizes:
        times = []
        print(f"\n---- Solve for N = {i} ----")

        for j in range(measurements_count):
            start = time.perf_counter()
            main(i)
            end = time.perf_counter()

            elapsed_ms = (end - start) * 1000
            times.append(elapsed_ms)

            print(f"Замер {j + 1}: {elapsed_ms:.3f} мс")

        avg_time = sum(times) / measurements_count
        metrics.append(avg_time)

        print(f"Среднее время для N = {i}: {avg_time:.3f} мс")

    plt.figure(figsize=(12, 6))

    plt.plot(sizes, metrics, label="Среднее время поиска", color="black")
    plt.plot(sizes, metrics, "o", color="red")

    plt.title("Зависимость времени поиска разбиения от размера квадрата")
    plt.xlabel("Размер квадрата N")
    plt.ylabel("Время выполнения (мс)")

    plt.xticks(sizes)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.legend()

    for x, y in zip(sizes, metrics):
        plt.text(x, y, f"{y:.2f}", fontsize=8)

    plt.tight_layout()
    plt.show()