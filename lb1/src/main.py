import math

def solve_for_even(n):
    print(4)
    print(1,1,n//2)
    print(1+n//2,1,n//2)
    print(1,1+n//2,n//2)
    print(1+n//2,1+n//2,n//2)
    return

def solve_for_divisable_on_three(N,a):
    b = N//a
    print(a*2)
    print(1,1,b*(a-1))
    for i in range(a):
        print(1+b*(i),1+b*(a-1),b)
        if i != a-1:
            print(1+b*(a-1),1+b*(i),b)
    
def solve_for_others(N,s):
    board = [[0]*N for _ in range(N)]
    best = [float("+inf")]
    best_ans = []

    def is_placeable_at(x,y,size):
        if size + x > N or size + y > N:
            return False
        for i in range(x,x+size):
            for k in range(y,y+size):
                if board[k][i]:
                    return False
        return True

    def place(x,y,size,val):
        for i in range(x,x+size):
            for k in range(y,y+size):
               board[k][i] = val

    def find_first_empty():
        for i in range(N):
            for k in range(N):
                if not board[k][i]:
                    return [i,k]
        return [-1,-1]

    def get_max_square_size(x,y):
        size = 0
        while size+x <= N and size+y <= N:
            if is_placeable_at(x,y, size):
                size+=1
            else:
                break
        return size-1


    def backtracking(cur):
        if len(cur)>=best[0]:
            return

        pos = find_first_empty()
        x,y = pos
        if x == -1:
            best[0] = len(cur)
            best_ans.clear()
            best_ans.extend(cur[:])
            return
        
        max_possible = get_max_square_size(x, y)

        for size in range(max_possible, 0, -1):
            if size == N:
                continue
            if is_placeable_at(x,y,size):
                place(x,y, size, 1)
                cur.append([x,y, size])
                backtracking(cur)
                cur.pop()
                place(x,y, size, 0)
   
    p = N//2
   
    start = [[0,0,p+1], [0,p+1,p], [p+1,0,p]]
            
    for x,y,size in start:
        place(x,y,size,1)

    backtracking(start)

    s.extend(best_ans)    


def check_is_non_prime(N):
    for i in range(2,int(math.sqrt(N))+1):
        if N%i==0:
            return i
    return False


def main(N):

    a = check_is_non_prime(N)

    if N%2==0:
        solve_for_even(N)
    elif a==3:
        solve_for_divisable_on_three(N,a)
    else:
        s = []
        if a:
            reduced = a
            k = N // reduced
            solve_for_others(reduced, s)
            print(len(s))
            for i in s:
                print(i[0]*k+1, i[1]*k+1, i[2]*k)
        else:
            solve_for_others(N, s)
            print(len(s))
            for i in s:
                print(i[0]+1, i[1]+1, i[2])



if __name__ == "__main__":
    N = int(input())
    main(N)
    
