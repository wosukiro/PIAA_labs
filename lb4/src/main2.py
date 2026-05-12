def prefix_function(p):
    n = len(p)
    pi = [0] * n
    j = 0

    for i in range(1, n):
        c = p[i]

        print("i =", i, "c =", c, "j =", j)

        while j > 0 and c != p[j]:
            print("Откат j:", j, "->", pi[j - 1])
            j = pi[j - 1]

        if c == p[j]:
            j += 1

        pi[i] = j

        print("pi =", pi)
        print()

    print("Префиксный массив =", pi)
    print()

    return pi

def kmp_search(pattern, text):
    n = len(text)

    if n == 0:
        return 0

    pi = prefix_function(pattern)
    j = 0


    for i in range(n):
        c = text[i]

        print("i =", i, "c =", c, "j =", j)

        while j > 0 and c != pattern[j]:
            print("Откат j:", j, "->", pi[j - 1])
            j = pi[j - 1]

        if c == pattern[j]:
            j += 1

        print("Новый j =", j)
        print()

        if j == n:
            result = i - n + 1
            return result

    for i in range(n - 1):
        c = text[i]

        print("i =", i, "c =", c, "j =", j)

        while j > 0 and c != pattern[j]:
            print("Откат j:", j, "->", pi[j - 1])
            j = pi[j - 1]

        if c == pattern[j]:
            j += 1

        print("Новый j =", j)
        print()

        if j == n:
            result = i + 1
            return result

    print("Не найдено")
    return -1


if __name__ == "__main__":
    text = input()
    pattern = input()

    if len(text) != len(pattern):
        print(-1)
    else:
        result = kmp_search(pattern, text)
        print("Результат =", result)