
RESTAURANTS = [
    ("Mango Rice", 4.2, 25),
    ("Pad Thai House", 4.8, 40),
    ("Chicken Rice", 4.6, 15),
    ("Som Tam Corner", 4.6, 25),
    ("Boat Noodles", 4.8, 30),
]

def by_rating(r):
    return (-r[1], r[2])

def by_time(r):
    return (r[2], -r[1])

print("RUNNING FOOD SORTER")

option = input("Sort by (rating/time): ").strip().lower()

print("DEBUG INPUT:", repr(option))

if option == "rating":
    result = sorted(RESTAURANTS, key=by_rating)

elif option == "time":
    result = sorted(RESTAURANTS, key=by_time)

else:
    print("Unknown option")
    result = []

for i, r in enumerate(result, start=1):
    print(f"{i}. {r[0]}, {r[1]} stars, {r[2]} min")
