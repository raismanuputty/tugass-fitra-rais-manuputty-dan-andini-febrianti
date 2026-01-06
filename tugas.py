# 0/1 Knapsack Problem - Dynamic Programming
# Kasus: Tim Ekspedisi Pendakian Gunung

items = [
    ("Tenda", 5, 30),
    ("Kompor Portable", 3, 20),
    ("Sleeping Bag", 4, 25),
    ("Matras", 2, 12),
    ("Jaket Gunung", 2, 14)
]

capacity = 15
n = len(items)

# Membuat tabel DP
dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

# Mengisi tabel DP
for i in range(1, n + 1):
    weight = items[i - 1][1]
    value = items[i - 1][2]
    for w in range(capacity + 1):
        if weight <= w:
            dp[i][w] = max(
                dp[i - 1][w],
                dp[i - 1][w - weight] + value
            )
        else:
            dp[i][w] = dp[i - 1][w]

# Menentukan item yang terpilih
w = capacity
selected_items = []

for i in range(n, 0, -1):
    if dp[i][w] != dp[i - 1][w]:
        selected_items.append(items[i - 1])
        w -= items[i - 1][1]

selected_items.reverse()

# Output hasil
print("Kapasitas Ransel :", capacity, "kg")
print("Nilai Maksimum   :", dp[n][capacity])
print("\nItem Terpilih:")

total_weight = 0
for item in selected_items:
    print(f"- {item[0]} (Berat: {item[1]} kg, Nilai: {item[2]})")
    total_weight += item[1]

print("\nTotal Berat:", total_weight, "kg")
