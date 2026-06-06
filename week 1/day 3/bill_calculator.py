rest_name = input("Enter Restuarant Name: ").strip()

no_ppl = int(input("Enter the Number of People Dining: "))
if no_ppl <= 0:
    print("[!] Invalid number of people.")

total_bill = float(input("Enter the Total Bill Amount: "))
if total_bill < 0:
    print("[!] Invalid bill amount.")

bill_pp = total_bill / no_ppl
tip = bill_pp * 0.1
total_pp = tip + bill_pp





print("=" * 40)
print(f"{'BILL CALCULATOR' :^40}")
print("=" * 40)

print(f"{'Restaurant' :<12}: {rest_name}")
print(f"{'People' :<12}: {no_ppl}")
print(f"{'Total Bill' :<12}: ${total_bill:.2f}")

print("-" * 40)

print(f"{'Bill per person' :<18}: ${bill_pp:.2f}")
print(f"{'Tip (10%)' :<18}: ${tip:.2f}")
print(f"{'Total Per Person' :<18}: ${total_pp:.2f}")

print("=" * 40)