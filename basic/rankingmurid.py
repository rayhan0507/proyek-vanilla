murid = {

}

print("nilai 10 murid di sekolah A kelas 1 A")
t = 0
while True:
    nama_murid = str(input("masukan nama murid: "))
    nilai_murid = int(input("masukan nilai murid: "))
    if nama_murid.isdigit():
        print("masukan nama murid dengan benar")
        print("\n")
        print("ulangi")
    if nilai_murid > 100 or nilai_murid < 0:
        print("berikan nilai murid dengan benar")
        print("\n")
        print("ulangi")

    else:
        murid[nama_murid] = nilai_murid
        t += 1
        if t == 10:
            break

list_nilai = []
for nama, nilai in murid.items():
    list_nilai.append((nama, nilai))

sorted_nilai = sorted(list_nilai, key=lambda x: x[-1], reverse=True)
print(sorted_nilai)
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")
print("\n")

print("--- hasil ranking ---")
for i, nama in enumerate(sorted_nilai):
    print(f"rank {i + 1}: {nama[0]}")