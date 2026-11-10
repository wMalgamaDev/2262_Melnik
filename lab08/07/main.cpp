#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> nums;
    int x;
    while (cin >> x)
    {
        nums.push_back(x);
    }

    bool found = false;
    for (int i = 0; i < nums.size(); i++)
    {
        if (nums[i] < 0)
        {
            cout << "найдено отрицательное: " << nums[i] << endl;
            found = true;
            break;
        }
    }

    if (!found)
    {
        cout << "все неотрицательные" << endl;
    }

    return 0;
}