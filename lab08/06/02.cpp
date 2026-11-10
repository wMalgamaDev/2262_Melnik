#include <iostream>
using namespace std;

int cnt = 0;

int limit()
{
    cnt++;
    return 5;
}

int main()
{
    cnt = 0;
    for (int i = 0; i < limit(); i++)
    {
        cout << i << " ";
    }
    cout << "cnt=" << cnt << endl;

    cnt = 0;
    {
        int __i = 0, __n = limit();
        for (const int &i = __i; i < __n; __i++)
        {
            cout << i << " ";
        }
    }
    cout << "cnt=" << cnt << endl;
}