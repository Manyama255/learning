#include<iostream>
using namespace std;
int main () {
    float length, width, area;

    cout << "Enter Length: ";
    cin >> length;

    cout << "Enter width: ";
    cin >> width;

    area = length * width;

    cout << "Area of the rectangle = " << area << endl;
    return 0;
}