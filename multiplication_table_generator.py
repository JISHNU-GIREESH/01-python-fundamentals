number = int(input("Enter a Number: "))



print("=" * 40)
print("MULTIPLICATION TABLE".center(40))
print("=" * 40)

for i in range(1,11):
    ans = number * i
    print(f"{number} x {i} = {ans}")

print("=" * 40)