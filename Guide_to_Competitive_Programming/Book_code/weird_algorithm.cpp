#include <iostream>
using namespace std;
void myFunction(long n) {
    
    while (true) {
        cout << n << " ";
        if (n == 1) break;
        if (n%2 == 0) n /= 2; 
        else n = n*3+1;
        
    }
        cout << "\n";
    }

int main() {
    long n;
    cin >> n; 
    myFunction(n);
    
    return 0;
}