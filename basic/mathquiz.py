quiz = {
    1: {"3 + 2? ": 5},
    2: {"10 * 10? " :100},
    3: {"2 + 1? ": 3},
    4: {"4 + 2? ": 6},
    5: {"24 / 4? ": 6},
    6: {"11 * 3? ": 33},
    7: {"-4 + 20? ": 16},
    8: {"36 - 12? ": 24},
    9: {"4 - (- 18)? ": 22},
    0: {"27 + (-3)? ": 24},
}

nilai = 0
seed = str(input("tulis 10 digit angka: "))
seed = list(map(int ,seed))
if len(seed) < 10:
    print("belum 10 digit")
else:   
    i = 0
    while i != 10:
        for random_number in seed:
            question, answer = list(quiz[random_number].items())[0]
            inp = int(input(f"{question}: "))
            if inp == answer:
                nilai += 10
            i += 1
            
    print(f"nilai anda: {nilai}")