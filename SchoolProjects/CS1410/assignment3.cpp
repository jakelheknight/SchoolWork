#include <iostream>
#include <string>
using namespace std;

struct fraction {
	int numerator;
	int denominator;
};
struct dist {
	int feet;
	int inches;
	fraction inchPartal;
	char frac;
};

void populate(dist & args) {
	//dist args;
	char frac;
	int feet;
	int inches;
	int numTmp;
	int denomTmp;
	int common = 1;
	cout << "How many feet? ";
	cin >> feet;
	cout << "How many whole inches? ";
	cin >> inches;
	cout << "Are there fractional inches? (y/n)  ";
	cin >> frac;
	if (frac == 'y' || frac == 'Y') {
		args.frac = 'y';
		cout << "How many parts of an inch in the folowing form?  (num denom)  ";
		cin >> numTmp >> denomTmp;
		for (int i = 1; i <= numTmp; i++) {
			if (numTmp%i == 0 && denomTmp%i == 0) {
				common = i;
			}
		}
	}
	else {
		numTmp = 0;
		denomTmp = 1;
		args.frac = 'n';
	}
	int num = numTmp / common;
	int denom = denomTmp / common;
	inches += num / denom;
	args.feet = feet + inches / 12; 
	args.inches = inches%12;
	args.inchPartal.numerator = num%denom;
	args.inchPartal.denominator = denom;
}
void displayF(fraction args) {
	cout << args.numerator << "/" << args.denominator;
}
dist add(dist a, dist b) {
	dist args;
	int denomTmp = a.inchPartal.denominator * b.inchPartal.denominator;
	int numTmp = (a.inchPartal.numerator*b.inchPartal.denominator + b.inchPartal.numerator*a.inchPartal.denominator);
	int common = 1;
	args.inches = (a.inches + b.inches + numTmp / denomTmp) % 12;
	args.feet = a.feet + b.feet + (a.inches + b.inches) / 12;
	numTmp = numTmp%denomTmp;
	for (int i = 1; i <= numTmp; i++) {
		if (numTmp % (i) == 0 && denomTmp % (i) == 0) {
			common = i;
		}
	}
	args.inchPartal.numerator = numTmp / common;
	args.inchPartal.denominator = denomTmp / common;
	if ((a.frac == 'y' || b.frac == 'y' ) && numTmp != 0) {
		args.frac = 'y';
	}
	else {
		args.frac = 'n';
	}
	return args;
}
void display(dist args) {
	cout << args.feet << "\" " << args.inches << "' ";
	if (args.frac == 'y' || args.frac == 'Y') {
		displayF(args.inchPartal);
	}
	cout << endl;
}

int main() {
	dist a;
	dist b;
	dist c;
	populate(a);
	display(a);
	populate(b);
	display(b);
	c = add(a, b);
	display(c);
	system("pause");
	return 0;
}