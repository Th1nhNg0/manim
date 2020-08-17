#include <iostream>
using namespace std;
int main() {
    int a[14] = {6, 11, 10, 13, 5, 2, 1,
                 12, 4, 3, 0, 8, 9, 7};
    quickSort(a, 0, 13);
    return 0;
}