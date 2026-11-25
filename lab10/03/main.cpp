#include <iostream>

int main() {
    int a = 5, b = 3;
    int* p = &a; 
    int& r = *p; 
    int res = (a * b) & r; 
    std::cout << res;
    return 0;
}
