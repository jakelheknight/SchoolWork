#include <iostream>
#include <time.h>
#include  <Windows.h>

using namespace std;
int main() {
	bool play = true;
	int wins = 0;
	int loss = 0;
	int dice1 = 0;
	int dice2 = 0;
	int role = 0;
	int point = 0;
	int round = 1;
	char cont = 'y';

	while (play) {
		cout << "Start round " << round++ << endl;
		dice1 = 1 + (rand() % 6);
		dice2 = 1 + (rand() % 6);
		role = dice1 + dice2;
		cout << "You roled " << dice1 << " and " << dice2 << " for a total of " << role << endl;
		Sleep(1000);
		if (role == 7 || role == 11) {
			cout << "You won on the first role you lucky dog with a role of " << role << endl;
			Sleep(2000);
			cout << ++wins << " Wins and " << loss << "Losses" << endl;
		} else if (role == 2 || role == 3 || role == 12) {
			cout << "You lost on the first role craps, with a role of " << role << endl;
			Sleep(2000);
			cout << wins << " Wins and " << ++loss << "Losses" << endl;
		}
		else {
			point = role;
			cout << "Point set at " << point << endl;
			do  {
				role = 1 + (rand() % 6) + 1 + (rand() % 6);
				cout << "You roled " << role << endl;
				Sleep(1000);
				if (role == 7) {
					cout << "Craps you lose." << endl;
					Sleep(2000);
					cout << wins << " wins and " << ++loss << " losses." << endl;
				}
				else if(role == point)
				{
					cout << "Craps you win." << endl;
					Sleep(2000);
					cout << wins << " wins and " << ++loss << " losses." << endl;
				}
			} while (point != role && role != 7);
		}
		cout << "Would you like to play again?(y or n) ";
		cin >> cont;
		if (cont == 'y') {
			play = true;
			system("cls");
		}
		else if (cont == 'n') {
			play = false;
			cout << "Thanks for playing." << endl;
			cout << wins << " wins and " << loss << " losses." << endl;
			Sleep(2000);
		}
	}
	return 0;
}