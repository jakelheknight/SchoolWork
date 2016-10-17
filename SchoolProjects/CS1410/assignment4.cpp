#include <iostream>
#include "DateUtil.h"

using namespace std;
//___________Class Statements______________
class Date {
private:
	int month;
	int day;
	int year;
	void intAddSub(int days) {
		long int dateNum = getNumberFromDate(day, month, year);
		dateNum += days;
		getDateFromNumber(dateNum, day, month, year);
	}
public:
	Date() { getCurrentDate(day, month, year); }
	Date(int m, int d, int y) : month(m), day(d), year(y) {}
	int getMonth() { return month; }
	int getDay() { return day; }
	int getYear() { return year; }
	void setMonth(int m) { month = m; }
	void setDay(int d) { day = d; }
	void setYear(int y) { year = y; }
	void addDays(int more) { intAddSub(more); }
	void subtractDays(int less) { intAddSub(-less); }
	void displayDate() {
		if (month < 10) { cout << "0"; }
		cout << month << "/";
		if (day < 10) { cout << "0"; }
		cout << day << "/";
		cout << year << endl; }
	void populateDate() {
		cout << "Enter date in the following format: (mm dd yyyy)  ";
		cin >> month >> day >> year;
	}
};
//____________Main Function________________
int main() {
	Date d1;
	Date d2(11, 11, 2011);
	cout << "Heres a random date:   ";
	d2.displayDate();
	cout << "If I add 333 days that makes it: ";
	d2.addDays(333);
	d2.displayDate();
	cout << "If I subtract 333 days that makes it: ";
	d2.subtractDays(333);
	d2.displayDate();
	cout << endl;
	cout << "I can set the date again." << endl;
	d2.setDay(23);
	d2.setMonth(11);
	d2.setYear(2014);
	cout << "The new date is " << d2.getMonth() << "/" << d2.getDay() << "/" << d2.getYear() << endl;
	cout << "Todays date is ";
	d1.displayDate();
	d1.populateDate();
	cout << "That was a good day... ";
	d1.displayDate();
	system("pause");
	return 0;
}
