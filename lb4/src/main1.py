def prefix_function(p):
    pi = [0] * len(p)

    for i in range(1, len(p)):
        j = pi[i - 1]

        print("i =", i, "c =", p[i], "j =", j)

        while j > 0 and p[i] != p[j]:
            print("Откат j:", j, "->", pi[j - 1])
            j = pi[j - 1]

        if p[i] == p[j]:
            j += 1

        pi[i] = j

        print("pi =", pi)
        print()

    print("Префиксный массив =", pi)
    print()

    return pi


def kmp_search(pattern, text):
    pi = prefix_function(pattern)
    result = []

    j = 0

    for i in range(len(text)):
        print("i =", i, "c =", text[i], "j =", j)

        while j > 0 and text[i] != pattern[j]:
            print("Откат j:", j, "->", pi[j - 1])
            j = pi[j - 1]

        if text[i] == pattern[j]:
            j += 1

        print("Новый j =", j)
        print()

        if j == len(pattern):
            found_index = i - len(pattern) + 1
            result.append(found_index)

            print("Найдено вхождение с индекса =", found_index)
            print("result =", result)

            print("Откат j после найденного вхождения:", j, "->", pi[j - 1])
            j = pi[j - 1]

            print("Новый j =", j)
            print()

    if not result:
        print("Не найдено")

    return result

if __name__ == "__main__":
    pattern = input()
    text = input()

    result = kmp_search(pattern, text)

    if result:
        print(",".join(map(str, result)))
    else:
        print(-1)