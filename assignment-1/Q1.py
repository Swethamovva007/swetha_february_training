#Taking input from the user:
Student_name=input("Enter your name:")
Age=int(input("Enter your age:"))
Percentage=float(input("Enter your percentage:"))
Family_income=float(input("Enter your family income:"))
Area=bool(input("Do you live in rural area?(Yes/No):"))

#Displaying the student details:
print("\n--- Student Details ---")
print(f"Name           : {Student_name}")
print(f"Age            : {Age}")
print(f"Percentage     : {Percentage}%")
print(f"Family Income  : ₹{Family_income}")
print(f"Rural Area     : {Area}")

#Scholorship eligibility criteria:
if (Percentage>=85 and Family_income<=300000) or Percentage>=90:
    print("You are eligible for scholorship")
else:
    print("You are not eligible for scholorship")
