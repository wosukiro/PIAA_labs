import pprint
def calculate_and_print_prescription(price_rep: int, price_ins: int, price_del: int, 
                                     str_a: str, str_b: str, 
                                     special_char_rep: str = None, special_price_rep: int = None, 
                                     special_char_ins: str = None, special_price_ins: int = None):

    n = len(str_a)
    m = len(str_b)
    
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = dp[i-1][0] + price_del
        
    for j in range(1, m + 1):
        if (special_char_ins is not None) and (str_b[j-1] == special_char_ins):
            current_ins_price = special_price_ins
        else:
            current_ins_price = price_ins

        dp[0][j] = dp[0][j-1] + current_ins_price

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str_a[i-1] == str_b[j-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                if (special_char_rep is not None) and (str_a[i-1] == special_char_rep):
                    current_rep_price = special_price_rep
                else:
                    current_rep_price = price_rep

                if (special_char_ins is not None) and (str_b[j-1] == special_char_ins):
                    current_ins_price = special_price_ins
                else:
                    current_ins_price = price_ins

                dp[i][j] = min(
                    dp[i-1][j-1] + current_rep_price,  
                    dp[i][j-1] + current_ins_price,    
                    dp[i-1][j] + price_del             
                )
                print("     ","  ".join([i for i in str_b]))
                c=0
                for row in dp:
                    if c!=0:
                        print(str_a[c-1],row)
                    else: 
                        print(" ",row)
                    c+=1
                print()
        print(f"Матрица после обработки символа '{str_a[i-1]}' (Шаг {i}):")
        print("     ","  ".join([i for i in str_b]))
        c=0
        for row in dp:
            if c!=0:
                print(str_a[c-1],row)
            else: 
                print(" ",row)
            c+=1
        print()

    i, j = n, m
    ops = []
    res_a = []
    res_b = []

    while i > 0 or j > 0:
        if (special_char_rep is not None and i > 0 and str_a[i-1] == special_char_rep):
            current_rep_price = special_price_rep
        else:
            current_rep_price = price_rep

        if (special_char_ins is not None and j > 0 and str_b[j-1] == special_char_ins):
            current_ins_price = special_price_ins
        else:
            current_ins_price = price_ins

        if i > 0 and j > 0 and str_a[i-1] == str_b[j-1] and dp[i][j] == dp[i-1][j-1]:
            print(f"[{i}][{j}] -> [{i-1}][{j-1}]: Символы '{str_a[i-1]}' и '{str_b[j-1]}' совпадают. Операция 'M'.")
            ops.append('M')
            res_a.append(str_a[i-1])
            res_b.append(str_b[j-1])
            i -= 1
            j -= 1
            
        elif i > 0 and j > 0 and str_a[i-1] != str_b[j-1] and dp[i][j] == dp[i-1][j-1] + current_rep_price:
            print(f"[{i}][{j}] -> [{i-1}][{j-1}]: Замена '{str_a[i-1]}' на '{str_b[j-1]}'. Операция 'R'.")
            ops.append('R')
            res_a.append(str_a[i-1])
            res_b.append(str_b[j-1])
            i -= 1
            j -= 1
            
        elif i > 0 and dp[i][j] == dp[i-1][j] + price_del:
            print(f"[{i}][{j}] -> [{i-1}][{j}]: Удаление '{str_a[i-1]}'. Операция 'D'.")
            ops.append('D')
            res_a.append(str_a[i-1])
            res_b.append(' ')
            i -= 1
            
        elif j > 0 and dp[i][j] == dp[i][j-1] + current_ins_price:
            print(f"[{i}][{j}] -> [{i}][{j-1}]: Вставка '{str_b[j-1]}'. Операция 'I'.")
            ops.append('I')
            res_a.append(' ')
            res_b.append(str_b[j-1])
            j -= 1

    print(" ".join(reversed(ops)))
    print(" ".join(reversed(res_a)))
    print(" ".join(reversed(res_b)))


if __name__ == "__main__":
    prices = input().split()
    p_rep, p_ins, p_del = int(prices[0]), int(prices[1]), int(prices[2])
    
    s_a = input().strip()
    s_b = input().strip()
    
    # Флаг: 1 - есть доп. данные, 0 - нет доп. данных (четвертая строка)
    flag = 0
    
    sp_char_rep, sp_price_rep = None, None
    sp_char_ins, sp_price_ins = None, None
    
    if flag == 1:
        extra_rep = input().split()
        sp_char_rep = extra_rep[0]
        sp_price_rep = int(extra_rep[1] if len(extra_rep) > 1 else input())
        
        extra_ins = input().split()
        sp_char_ins = extra_ins[0]
        sp_price_ins = int(extra_ins[1] if len(extra_ins) > 1 else input())

    calculate_and_print_prescription(
        price_rep=p_rep, price_ins=p_ins, price_del=p_del,
        str_a=s_a, str_b=s_b,
        special_char_rep=sp_char_rep, special_price_rep=sp_price_rep,
        special_char_ins=sp_char_ins, special_price_ins=sp_price_ins
    )