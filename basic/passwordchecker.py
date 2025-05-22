# password checker
t = 0
def berhasil():
    print("password anda sudah di buat")

while True:
    password = input("masukan password: ")
    if t == 3:
        print("anda sudah memasukan password tidak valid 3x")
        print("coba lagi nanti")
        break

    if len(password) < 8:
        print("masukan password minimal 8 digit")
        print("\n")
        print("ulangi:")
        t += 1

    elif password[0].islower():
        print("usahakan huruf kapital")
        print("\n")
        print("ulangi")
        t += 1
    else:
        ok = False
        for i in password:
            if i.isdigit():
                ok = True
            
        if ok == False:
            t += 1
            print("usahakan ada angka di password anda")

        if ok == True:
            ok_2 = False
            tambahan = ".!"
            for j in password:
                if j in tambahan:
                    ok_2 = True

            if ok_2 == True:
                berhasil()
                break
            
            else:
                t += 1
                print("tambakan titik atau sebagainya")