#include <iostream>

using namespace std;
int main() {
	// Initialize variables.
	bool run = true;
	char option;
	float curincy;
	float temp;
	float exchange[4] = {1.33, 0.77, 0.58, 0.00955};
	// Run loop
	while (run) {
		//Prompt choice
		cout << "Type m to Convert Currency, t to Convert Temperature or type q to quit.  ";
		cin >> option;
		if (option == 't') {
			cout << "Please enter the temperature in Celsius. ";
			cin >> temp;
			cout << "That is " << temp * 9 / 5 + 32 << " in Ferinheight.";
		}
		else if (option == 'm') {
			cout << "Please enter amoutn in american dollars. " << endl;
			cin >> curincy;
			cout << "The current vlaue of $" << curincy << " American dollars is " << curincy*exchange[0] << " in British Pounds." << endl;
			cout << "The current vlaue of $" << curincy << " American dollars is " << curincy*exchange[1] << " in Canadian Dollars." << endl;
			cout << "The current vlaue of $" << curincy << " American dollars is " << curincy*exchange[2] << " in German Deutschemark." << endl;
			cout << "The current vlaue of $" << curincy << " American dollars is " << curincy*exchange[3] << " in Japanese Yen." << endl;
		}
		else if (option == 'q') {
			cout << "Thank you for playing.";
			run = false;
		}
		else {
			cout << "Invalid input" << endl;
		}
		cout << endl;
	}

	return 0;
}