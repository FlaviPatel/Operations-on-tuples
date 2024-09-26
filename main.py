t = (1, "Zara", 89, ["Maths", "Science"], (56, 45))

print("First Element:", t[0])
print("Second Element:", t[1])
print("To get a nested index:", t[3][1])
print("Slicing:", t[4:5])

for i in t:
    print(i)