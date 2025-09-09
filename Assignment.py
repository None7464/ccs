print("Wassup")
print("Enter Input")
print("=" * 55)

student_name = input("ENTER STUDENT NAME: ").upper()
course = input("ENTER YOUR COURSE (e.g., 'BSIT'): ").upper()
year = int(input("ENTER YEAR (1, 2, 3, 4): "))
tuition_per_unit = float(input("TUITION PER UNIT: "))
num_units = int(input("NUMBER OF UNITS: "))
misc_fee = float(input("MISC FEE: "))

total_tuition = tuition_per_unit * num_units
total_fee = total_tuition + misc_fee

print("=" * 55)
print("Output")
print(f"STUDENT NAME: {student_name}")
print(f"COURSE: {course} 🎓")
print(f"YEAR: {year} 📅")
print(f"TUITION PER UNIT: {tuition_per_unit}")
print(f"NUMBER OF UNITS: {num_units}")
print(f"MISC FEE: {misc_fee}")
print("-" * 55)
print(f"TOTAL TUITION: {total_tuition}")
print(f"GRAND TOTAL FEE: {total_fee}")
print("=" * 55)
print("Done!")