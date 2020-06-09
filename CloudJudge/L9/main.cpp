#include <iostream>
#include <iomanip>
using namespace std;

class Rectangle
{
public:
	double width, height;

	Rectangle(double newWidth,double newHeight)
	{
		width = newWidth;
		height = newHeight;
	}
	double getArea()
	{
		return width * height;
	}
	double getPerimeter()
	{
		return (width + height) * 2;
	}
};

int main()
{
	double w1, h1, w2, h2;
	cin >> w1 >> h1 >> w2 >> h2;
	Rectangle r1(w1, h1);
	Rectangle r2(w2, h2);
	
	cout << fixed << setprecision(2) << r1.getArea() << " " << r1.getPerimeter() << endl;
	cout << fixed << setprecision(2) << r2.getArea() << " " << r2.getPerimeter() << endl;

	r2.width = 5.0;
	r2.height = 2.5;
	cout << fixed << setprecision(2) << r2.getArea() << " " << r2.getPerimeter() << endl;

	system("pause");
	return 0;
}