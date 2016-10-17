#include <iostream>
#include <string>

using namespace std;

//-------------------------------------------------------- Declare Structures
struct fraction {
	int num;
	int denom;
};
struct dist {
	int feet;
	int inches;
	fraction partial;
};

//-------------------------------------------------------- Declair Functions
void standardize(dist &args) {//Function that reduces fractions and standardizes distances.
	int tmp = 1;
	for (int i = 1; i <= args.partial.num/2 && i <= args.partial.denom/2; i++) {
		if (args.partial.num%i == 0 && args.partial.denom%i == 0) {
			tmp = i;
		}
	}
	args.feet = args.feet + (args.inches + args.partial.num / args.partial.denom) / 12;
	args.inches = (args.inches + args.partial.num / args.partial.denom)%12;
	args.partial.denom = args.partial.denom / tmp;
	args.partial.num = (args.partial.num / tmp) % args.partial.denom;
}
//--------------------------------------------------------------
void populate(dist &args) {
	char frac;
	cout << "How many feet? ";
	cin >> args.feet;
	cout << "How many whole inches? ";
	cin >> args.inches;
	cout << "Are there fractional inches? (y/n)  ";
	cin >> frac;
	if (frac == 'y' || frac == 'Y') {
		cout << "How many parts of an inch in the folowing form?  (num denom)  ";
		cin >> args.partial.num >> args.partial.denom;
	}
	else {
		args.partial = { 0, 1 };
	}
	standardize(args);
}
void display(dist args) {
	cout << args.feet << "\" " << args.inches << "' ";
	if (args.partial.num != 0) {
		cout << args.partial.num << "/" << args.partial.denom;
	}
	cout << endl;
}
//--------------------------------------------------------------
dist add(dist a, dist b) {
	fraction cFrac = { a.partial.num *b.partial.denom + b.partial.num*a.partial.denom, a.partial.denom*b.partial.denom };
	dist c = { a.feet + b.feet, a.inches + b.inches, cFrac };
	standardize(c);
	return c;
}
//--------------------------------------------------------------
dist sum(dist arg[], int n) {
	dist result = { 0, 0, {0, 1} };
	for (int i = 0; i < n; i++) {
		result = add(result, arg[i]);
	}
	return result;
}




//--------------------MAIN---------------------------------
int main() {
	char run = 'y';
	while (run=='y' || run == 'Y') {
		dist a[25] = {};
		int n;
		cout << "How many distances would you like to sum? ";
		cin >> n;
		if (n > 25) {
			cout << "This calcualtor only allows sums of up to 25 distances. We will by default set the maximum." << endl;
			n = 25;
		}
		for (int i = 0; i < n; i++) {
			cout << "Distance " << i + 1 << ":" << endl;
			populate(a[i]);
		}
		cout << endl << endl;
		for (int i = 0; i < n - 1; i++) {
			cout << "  ";
			display(a[i]);
		}
		cout << "+ ";
		display(a[n - 1]);
		cout << "----------------" << endl << "  ";
		display(sum(a, n));
		cout << endl << "Whould you like to enter another batch? y or n ";
		cin >> run;
	}
	return 0;
}