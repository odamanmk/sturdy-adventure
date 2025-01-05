import math

# 1. Noktaların Tanımlanması (2D uzaydaki noktalar)
points = [(1, 2), (4, 6), (7, 8), (2, 3), (5, 1)]

# 2. Öklid Mesafesi İçin Fonksiyon Tanımlanması
def euclideanDistance(point1, point2):
    # İki nokta arasındaki Öklid mesafesini hesaplayan formül
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# 3. Mesafelerin Hesaplanması
distances = []

# Tüm nokta çiftleri için mesafe hesaplama
for i in range(len(points)):
    for j in range(i+1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# 4. Minimum Mesafenin Bulunması
min_distance = min(distances)

# Minimum mesafeyi yazdırma
print("Minimum mesafe:", min_distance)
