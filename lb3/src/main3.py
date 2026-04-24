def get_levenshtein_distance(str_a: str, str_b: str, 
                             special_char_rep: str = None, special_price_rep: int = None, 
                             special_char_ins: str = None, special_price_ins: int = None) -> int:

    n = len(str_a)
    m = len(str_b)
    
    price_rep = 1
    price_ins = 1
    price_del = 1

    if n == 0:
        cost = 0
        for char in str_b:
            if (special_char_ins is not None and char == special_char_ins):
                cost += special_price_ins
            else:
                cost += price_ins
        return cost
        
    prev_row = [0] * (m + 1)
    for j in range(1, m + 1):
        if (special_char_ins is not None) and (str_b[j-1] == special_char_ins):
            current_ins_price = special_price_ins
        else:
            current_ins_price = price_ins
        prev_row[j] = prev_row[j-1] + current_ins_price
    
    for i in range(1, n + 1):
        curr_row = [0] * (m + 1)
        curr_row[0] = prev_row[0] + price_del
        
        char_a = str_a[i-1]
        if (special_char_rep is not None) and (char_a == special_char_rep):
            current_rep_price = special_price_rep
        else:
            current_rep_price = price_rep

        for j in range(1, m + 1):
            char_b = str_b[j-1]
            
            if char_a == char_b:
                curr_row[j] = prev_row[j-1]
            else:
                if (special_char_ins is not None) and (char_b == special_char_ins):
                    current_ins_price = special_price_ins 
                else:
                    current_ins_price = price_ins
                curr_row[j] = min(
                    prev_row[j-1] + current_rep_price, 
                    curr_row[j-1] + current_ins_price, 
                    prev_row[j] + price_del            
                )
        print(f"Шаг {i} (Обработка символа '{char_a}'):")
        print(f"{prev_row}")
        print(f"{curr_row}\n\n")
        prev_row = curr_row

    return prev_row[m]

if __name__ == "__main__":
    s_a = input().strip()
    s_b = input().strip()
    
    # Флаг: 1 - есть доп. данные, 0 - классическое расстояние Левенштейна

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

    print(get_levenshtein_distance(
        s_a, s_b, 
        sp_char_rep, sp_price_rep, 
        sp_char_ins, sp_price_ins
    ))