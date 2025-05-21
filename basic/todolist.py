def todo():
    t = 1
    todolist = {

    }
    while True:
        print("\n")
        print("----TODO LIST----")
        for x, y in todolist.items():
            print(f"{x}: {y}")
        print("\n")
        print("exit")
        print("delete")
        print("tambahkan sesuatu")
        inp = input("input: ")
        if inp == "exit":
            break
        if inp.split(' ')[0] == 'delete':
            key = int(inp.split(' ')[-1])
            if key in todolist:
                del todolist[key]
                print("aktivitas sudah di hapus")
                t = key
            else:
                print("tidak ada aktivitas")
    
        else:
            if t in todolist:
                maximum = 0
                for i in todolist:
                    maximum = max(maximum, i)
                t = maximum + 1
                todolist[t] = inp
            else:
                todolist[t] = inp
                t += 1

todo()