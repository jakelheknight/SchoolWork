# some your hw score quiz score midterm and final score and display a letter grade.



# sum 90+ : A
#    80=89: B
#    70-79: C
#    60-69: D



# Prompt for name, Homework score, quiz score, and midterm/final scores
name = input("What is your name?");
hwScore = int(input("What is your overall homework score? (0-100)"));
qScore = int(input("What is your overall quiz score? (0-100)"));
mfScore = int(input("What is your overall combined Midterm and Final score? (0-100)"));

#sum the weighted scores
score = hwScore*0.50 + qScore*0.2 + mfScore*0.3;
print("Overall score:" , score);

#Caclucate the letter grade based on the sum
if score >= 90:
    grade = "A"
elif score >= 89:
    grade = "B"
elif score >= 79:
    grade = "C"
elif score >= 69:
    grade = "D"
else:
    grade = "F"
#display the grade.
print(name, "your grade for the course is", grade);
