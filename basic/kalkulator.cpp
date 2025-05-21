#include <iostream>
#include <string>

int pertambahan(int angka_1, int angka_2 ) {
    return angka_1 + angka_2;
}
int pengurangan(int angka_1, int angka_2 ) {
    return angka_1 - angka_2;
}
int perkalian(int angka_1, int angka_2 ) {
    return angka_1 * angka_2;
}
int pembagian(int angka_1, int angka_2 ) {
    return angka_1 / angka_2;
}

int main() {
    std::string op;
    std::cout << "masukan operator (+,-,/,*): ";
    std::cin >> op;
    if (op == "+") {
        int angka_1;
        int angka_2;
        std::cout << "pilih angka pertama: ";
        std::cin >> angka_1;
        std::cout << "pilih angka ke dua: ";
        std::cin >> angka_2;
        std::cout << "hasil: " << pertambahan(angka_1, angka_2) << std:: endl;
    };
    if (op == "-") {
        int angka_1;
        int angka_2;
        std::cout << "pilih angka pertama: ";
        std::cin >> angka_1;
        std::cout << "pilih angka ke dua: ";
        std::cin >> angka_2;
        std::cout << "hasil: " << pengurangan(angka_1, angka_2) << std:: endl;
    };
    if (op == "*") {
        int angka_1;
        int angka_2;
        std::cout << "pilih angka pertama: ";
        std::cin >> angka_1;
        std::cout << "pilih angka ke dua: ";
        std::cin >> angka_2;
        std::cout << "hasil: " << perkalian(angka_1, angka_2) << std:: endl;
    };
    if (op == "/") {
        int angka_1;
        int angka_2;
        std::cout << "pilih angka pertama: ";
        std::cin >> angka_1;
        std::cout << "pilih angka ke dua: ";
        std::cin >> angka_2;
        std::cout << "hasil: " << pembagian(angka_1, angka_2) << std:: endl;
    };
    
    return 0;

}