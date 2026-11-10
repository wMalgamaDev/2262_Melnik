#include <iostream>
using namespace std;

int main()
{
    for (int i = 0; i < 10; i++)
    {
        cout << i << " ";
        if (i == 3)
            i += 2;
    }
    cout << endl;

    {
        int __i = 0, __n = 10;
        for (const int &i = __i; i < __n; __i++)
        {
            cout << i << " ";
            // if (i == 3) i += 2;
        }
    }
    cout << endl;
}