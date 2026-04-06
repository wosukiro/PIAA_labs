def find_path(matrix: list, k: int):
    mem = {}

    def dp(mask, last):
        if mask == (1 << k) - 1:
            if matrix[last][0] != 0:
                return matrix[last][0], 0
            else:
                return float("+inf"), -1

        state = (mask, last)
        if state in mem:
            return mem[state]

        lowest_len = float("+inf")
        best_next = -1
        
        for i in range(k):
            if (mask & (1 << i)) == 0 and matrix[last][i] != 0:
                child_len, _ = dp(mask | (1 << i), i)
                
                if child_len != float("+inf"):
                    way_len = child_len + matrix[last][i]
                    
                    if way_len < lowest_len:
                        lowest_len = way_len
                        best_next = i
        
        mem[state] = (lowest_len, best_next)
        return lowest_len, best_next

    ans_len, _ = dp(1, 0)
    
    if ans_len == float("+inf"):
        return "no path", []
        
    path = [0]
    curr_mask = 1
    curr_node = 0
    target_mask = (1 << k) - 1
    
    while curr_mask != target_mask:
        _, nxt = mem[(curr_mask, curr_node)]
        path.append(nxt)
        curr_mask |= (1 << nxt)
        curr_node = nxt
        
    path.append(0)

    return ans_len, path


if __name__ == "__main__":
    n = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().split())))
        
    ans = find_path(matrix, n)
    if ans[0] == "no path":
        print("no path")
    else:
        print(ans[0])
        print(*ans[1])