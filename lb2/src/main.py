def find_path(matrix: list, k: int):
    mem = {}
    print(f"\nНачинаем рекурсивный обход для {k} вершин:")

    def dp(mask, last):
        if mask == (1 << k) - 1:
            dist_to_start = matrix[last][0]
            if dist_to_start != 0:
                return dist_to_start, 0
            return float("+inf"), -1

        state = (mask, last)
        if state in mem:
            return mem[state]

        lowest_len = float("+inf")
        best_next = -1
        bin_mask = bin(mask)[2:].zfill(k)
        
        for i in range(k):
            if (mask & (1 << i)) == 0 and matrix[last][i] != 0:
                child_len, _ = dp(mask | (1 << i), i)
                
                if child_len != float("+inf"):
                    way_len = child_len + matrix[last][i]
                    if way_len < lowest_len:
                        lowest_len = way_len
                        best_next = i
        
        if lowest_len != float("+inf"):
            print(f"Состояние (маска:{bin_mask}, последняя:{last}) -> "
                  f"лучший следующий шаг: {best_next}, длина до конца: {lowest_len}")
        
        mem[state] = (lowest_len, best_next)
        return lowest_len, best_next

    ans_len, _ = dp(1, 0)
    
    if ans_len == float("+inf"):
        return "no path", []
        
    print("\nВосстановление оптимального пути по таблице мемоизации:")
    path = [0]
    curr_mask = 1
    curr_node = 0
    target_mask = (1 << k) - 1
    
    while curr_mask != target_mask:
        _, nxt = mem[(curr_mask, curr_node)]
        print(f"Из узла {curr_node} переходим в {nxt} (длина ребра: {matrix[curr_node][nxt]})")
        path.append(nxt)
        curr_mask |= (1 << nxt)
        curr_node = nxt
        
    path.append(0)
    print(f"Возврат в начало: из {curr_node} в 0 (длина ребра: {matrix[curr_node][0]})\n")

    return ans_len, path


def alsh_1(matrix: list, k: int):
    print(f"\nСтартуем из вершины 0")
    current_node = 0
    path = [current_node]
    visited = {current_node}
    total_len = 0
    
    for step in range(1, k):
        next_node = -1
        min_dist = float("+inf")
        
        print(f"\nШаг {step}. Текущая вершина: {current_node}. Ищем ближайшего соседа:")
        
        for neighbor in range(k):
            if neighbor not in visited:
                dist = matrix[current_node][neighbor]
                if dist != 0:
                    status = f"расстояние {dist}"
                    if dist < min_dist:
                        min_dist = dist
                        next_node = neighbor
                        status += " (новый минимум)"
                    print(f"Проверка соседа {neighbor}: {status}")
                else:
                    print(f"Проверка соседа {neighbor}: пути нет")
        
        if next_node == -1:
            print("НЕТ ДОСТУПНЫХ НЕПОСЕЩЕННЫХ ПЕРШИН!!! - no path")
            return "no path", []
            
        total_len += min_dist
        print(f"Итог шага {step}: Выбран сосед {next_node} с расстоянием {min_dist}. Текущая общая длина: {total_len}")
        current_node = next_node
        path.append(current_node)
        visited.add(current_node)
    
    dist_to_start = matrix[current_node][0]
    print(f"\nЗавершение. Возврат в вершину 0 из {current_node}.")
    if dist_to_start != 0:
        total_len += dist_to_start
        path.append(0)
        print(f"Путь замкнут. Длина ребра: {dist_to_start}. Итоговая длина: {total_len}\n")
    else:
        print("НЕВОЗМОЖНО ВЕРНУТЬСЯ В СТАРТОВУЮ ВЕРШИНУ!!!\n")
        return "no path", []
        
    return total_len, path

if __name__ == "__main__":
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
        
    print("Точный метод (динамическое программирование)")
    ans_dp = find_path(matrix, n)
    if ans_dp[0] == "no path":
        print("no path")
    else:
        print(f"Длина: {ans_dp[0]}")
        print(f"Путь: {' '.join(map(str, ans_dp[1]))}")

    print("\nПриближенный метод (АЛШ-1)")
    ans_alsh = alsh_1(matrix, n)
    if ans_alsh[0] == "no path":
        print("no path")
    else:
        print(f"Длина: {ans_alsh[0]}")
        print(f"Путь: {' '.join(map(str, ans_alsh[1]))}")