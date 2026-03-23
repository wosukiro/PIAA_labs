import math

def solve_for_even(n, logger=False):

    if logger:
        print("Случай: квадрат чётного размера.")
        print("Поле разбивается на 4 равных квадрата.")
        print(f"Размер каждого квадрата: {n//2}")
        print()
        print("Ответ: 4")
        print(f"Квадрат 1: (0, 0), размер {n//2}")
        print(f"Квадрат 2: ({n//2}, 0), размер {n//2}")
        print(f"Квадрат 3: (0, {n//2}), размер {n//2}")
        print(f"Квадрат 4: ({n//2}, {n//2}), размер {n//2}")

    else:
        print(4)
        print(0,0,n//2)
        print(n//2,0,n//2)
        print(0,n//2,n//2)
        print(n//2,n//2,n//2)
    return

def solve_for_divisable_on_three(N,a, logger=False):
    b = N//a

    if logger:
        print("Случай: сторона квадрата делится на 3.")
        print(f"N = {N}, найден делитель a = {a}")
        print(f"Размер базового блока b = N // a = {b}")
        print("Строится одно крупное разбиение и несколько малых квадратов.")
        print()
        print("Ответ:")
        print(a*2)
        print(f"Квадрат 1: (0, 0), размер {b*(a-1)}")
        print(0,0,b*(a-1))

        cnt = 2
        for i in range(a):
            print(f"Квадрат {cnt}: ({b*i}, {b*(a-1)}), размер {b}")
            cnt += 1

            if i != a-1:
                print(f"Квадрат {cnt}: ({b*(a-1)}, {b*i}), размер {b}")
                cnt += 1
    else:
        print(a*2)
        print(0,0,b*(a-1))
        for i in range(a):
            print(b*(i),b*(a-1),b)
            if i != a-1:
                print(b*(a-1),b*(i),b)
    
def solve_for_others(N,s, logger=False):
    board = [[0]*N for _ in range(N)]
    best = [float("+inf")]
    best_ans = []

    def print_board():
        if logger:
            print("Текущее состояние поля:")
            for row in board:
                print(" ".join(str(x) for x in row))
            print()

    def is_placeable_at(x,y,size):

        if logger:
            print(f"Проверяем, можно ли поставить квадрат размера {size} в точку ({x}, {y})")

        if size + x > N or size + y > N:

            if logger:
                print("Нельзя: квадрат выходит за границы поля.")

            return False
        for i in range(x,x+size):
            for k in range(y,y+size):
                if board[k][i]:

                    if logger:
                        print(f"Нельзя: клетка ({i}, {k}) уже занята.")

                    return False

        if logger:
            print("Квадрат можно поставить.")

        return True

    def place(x,y,size,val):

        if logger:
            if val==1:
                print(f"Размещаем квадрат размера {size} в точке ({x}, {y})")
            else:
                print(f"Убираем квадрат размера {size} из точки ({x}, {y})")

        for i in range(x,x+size):
            for k in range(y,y+size):
               board[k][i] = val

        if logger:
            print_board()

    def find_first_empty():

        if logger:
            print("Ищем первую свободную клетку.")

        for i in range(N):
            for k in range(N):
                if not board[k][i]:

                    if logger:
                        print(f"Первая свободная клетка найдена: ({i}, {k})")

                    return [i,k]

        if logger:
            print("Свободных клеток не осталось.")

        return [-1,-1]

    def get_max_square_size(x,y):

        if logger:
            print(f"Определяем максимальный размер квадрата для точки ({x}, {y})")

        size = 0
        while size+x <= N and size+y <= N:
            if is_placeable_at(x,y, size):
                size+=1
            else:
                break

        if logger:
            print(f"Максимально возможный размер: {size - 1}")

        return size-1


    def backtracking(cur):

        if logger:
            print("----------------------------------")
            print(f"Текущее частичное решение: {cur}")
            print(f"Сейчас использовано квадратов: {len(cur)}")
            if best[0] == float("+inf"):
                print("Лучшее решение пока не найдено.")
            else:
                print(f"Лучший найденный результат: {best[0]} квадратов")
            print()

        if len(cur)>=best[0]:

            if logger:
                print("Продолжение поиска не имеет смысла:")
                print("текущее решение уже не лучше найденного.")
                print()

            return

        pos = find_first_empty()
        x,y = pos
        if x == -1:

            if logger:
                print("Поле полностью заполнено.")
                print(f"Найдено новое лучшее решение: {len(cur)} квадратов")
                print(f"Новое решение: {cur}")
                print()

            best[0] = len(cur)
            best_ans.clear()
            best_ans.extend(cur[:])
            return
        
        max_possible = get_max_square_size(x, y)

        if logger:
            print(f"Начинаем перебор размеров от {max_possible} до 1")
            print()

        for size in range(max_possible, 0, -1):
            if size == N:

                if logger:
                    print("Этот вариант пропускается, так как квадрат совпадает со всем полем.")
                    print()

                continue
            if is_placeable_at(x,y,size):
                place(x,y, size, 1)
                cur.append([x,y, size])

                if logger:
                    print(f"Квадрат [{x}, {y}, {size}] добавлен в решение.")
                    print(f"Решение стало таким: {cur}")
                    print()

                backtracking(cur)
                cur.pop()

                if logger:
                    print(f"Откат: квадрат [{x}, {y}, {size}] удаляется из решения.")

                place(x,y, size, 0)

            else:
                if logger:
                    print(f"Квадрат размера {size} поставить нельзя.")
                    print()
   
    p = N//2

    if logger:
        print(f"Для ускорения поиска строится начальная конфигурация.")
        print(f"p = N // 2 = {p}")
   
    start = [[0,0,p+1], [0,p+1,p], [p+1,0,p]]

    if logger:
        print("Начальные квадраты:")
        for idx, (x, y, size) in enumerate(start,1):
            print(f"{idx}) ({x}, {y}), размер {size}")
        print()
            
    for x,y,size in start:
        place(x,y,size,1)

    if logger:
        print("После размещения стартовых квадратов запускается поиск с возвратом.")
        print()

    backtracking(start)

    if logger:
        print("Поиск завершён.")
        print(f"Лучшее найденное покрытие: {best_ans}")
        print()

    s.extend(best_ans)    


def check_is_non_prime(N, logger=False):

    if logger:
        print(f"Проверяем, является ли число {N} составным:")

    for i in range(2, int(math.sqrt(N)) + 1):

        if logger:
            print(f"Пробуем делитель {i}")

        if N % i == 0:

            if logger:
                print(f"Найден делитель: {i}")
                print()

            return i
    
    if logger:
        print("Делителей не найдено, число простое.")
        print()

    return False

def main(N, logger = False):

    if logger:
        print(f"Входное число N = {N}")
        print()

    a = check_is_non_prime(N,logger)

    if N%2==0:

        if logger:
            print("Так как N чётное, применяется оптимизация для четного квадрата:")
            print()
        solve_for_even(N, logger)

    elif a==3:

        if logger:
            print("Так как N делится на 3, применяется оптимизация для квадрата со стороной делящейся на 3:")
            print()
        solve_for_divisable_on_three(N,a, logger)

    else:

        if logger:
            print("Используется общий алгоритм.")
            print()

        s = []
        if a:
            reduced = a
            k = N // reduced

            if logger:
                print(f"Число составное, применяется оптимизация:")
                print(f"Размерность квадрата для поиска шаблона разбивания = {reduced}, коэффициент масштабирования k = {k}")
                print(f"Сначала решаем задачу для поля {reduced} x {reduced},")
                print("А затем масштабируем ответ обратно.")
                print()


            solve_for_others(reduced, s, logger)
            
            if logger:
                print(f"Получено разбиение для квадрата {reduced} x {reduced}:")
                print(len(s))
                for i in s:
                    print(i[0], i[1], i[2])
                print(f"Выполняем масштабирование обратно. (Умножаем все размеры на коэф k = {k})")
                print("Итоговый ответ:")

            print(len(s))
            for i in s:
                print(i[0]*k, i[1]*k, i[2]*k)
        else:

            if logger:
                print("Число простое, оптимизация задачи невозможно.")
                print("Поиск выполняется сразу на исходном поле.")
                print()

            solve_for_others(N, s, logger)

            if logger:
                print("Итоговый ответ:")
                
            print(len(s))

            for i in s:
                print(*i)



if __name__ == "__main__":
    N = int(input())
    main(N, True)
    
