s_name = input("Enter Student Name: ").strip()
subject_1 = input("Enter Subject 1: ").strip()
score_1 = int(input("Subject 1 Score: "))
if score_1 < 0 or score_1 > 100:
    print("[!] Invalid score.")
subject_2 = input("Enter Subject 2: ").strip()
score_2 = int(input("Subject  Score: "))
if score_2 < 0 or score_2 > 100:
    print("[!] Invalid score.")
subject_3 = input("Enter Subject 3: ").strip()
score_3 = int(input("Subject 3 Score: "))
if score_3 < 0 or score_3 > 100:
    print("[!] Invalid score.")

average = (score_1 + score_2 + score_3) / 3

grade = ""
if average >= 90:
    grade = "A"
elif average >= 80:
    grade = "B"
elif average >= 70:
    grade = "C"
elif average >= 60:
    grade = "D"
else:
    grade = "F"

print("=" * 40)
print(f"{'STUDENT REPORT CARD' :^40}")
print("=" * 40)

print(f"{'Student Name:' :<13} {s_name}")

print("-" * 40)

print(f"{subject_1 :<13}: {score_1}")
print(f"{subject_2 :<13}: {score_2}")
print(f"{subject_3 :<13}: {score_3}")

print("-" * 40)

print(f"{'Average' :<13}: {average:.2f}")
print(f"{'Grade' :<13}: {grade}")
print("=" * 40)
