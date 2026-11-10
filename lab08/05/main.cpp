#include <iostream>
#include <vector>
using namespace std;

int main(){    
  int n;
  cin >> n;
  vector<int> v(n);
  for (auto& i : v){
    cin >> i;
  }
  for (auto& i : v){
    i += v[n-1];
  }
  int m = 0;
  n = 0;
  for (auto& i : v){
    if (i >= 0){
      m += 1;
    }
    else {
      n += 1;
    }
  }
  cout << "Положительные: " << m << "\n" << "Отрицательные: " << n << endl;
}
