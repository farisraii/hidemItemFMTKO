import random

# Definisikan layout grid
grid = [
    "########",
    "#......#",
    "#.###..#",
    "#...#.##",
    "#X#....#",
    "#######"
]

# Fungsi untuk menampilkan grid
def tampilkan_grid():
    for baris in grid:
        print(baris)

# Fungsi untuk mencari lokasi item yang mungkin
def cari_lokasi_item_mungkin():
    lokasi_mungkin = []
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] == '.':
                lokasi_mungkin.append((i, j))
    return lokasi_mungkin

# Fungsi untuk menempatkan 3 item secara acak di dalam grid
def tempatkan_item(lokasi_mungkin):
    lokasi_item = random.sample(lokasi_mungkin, 3)
    for i, j in lokasi_item:
        grid[i] = grid[i][:j] + '$' + grid[i][j+1:]
    return lokasi_item

# Fungsi untuk memeriksa apakah pergerakan ke atas, ke bawah, atau ke kiri adalah langkah yang valid
def periksa_langkah_valid(x, y, langkah):
    if langkah == 'A':
        return 0 <= x - 1 < len(grid) and grid[x - 1][y] != '#'
    elif langkah == 'B':
        return 0 <= y + 1 < len(grid[0]) and grid[x][y + 1] != '#'
    elif langkah == 'C':
        return 0 <= y - 1 < len(grid[0]) and grid[x][y - 1] != '#'
    else:
        return False

# Fungsi utama permainan
def main():
    tampilkan_grid()
    
    # Koordinat awal pemain (X)
    x, y = 4, 1
    
    while True:
        try:
            A = int(input("Masukkan jumlah langkah ke atas (A): "))
            B = int(input("Masukkan jumlah langkah ke kanan (B): "))
            C = int(input("Masukkan jumlah langkah ke kiri (C): "))
            break
        except ValueError:
            print("Masukkan angka yang valid untuk jumlah langkah.")
    
    # Cari lokasi item yang mungkin secara acak
    lokasi_mungkin = cari_lokasi_item_mungkin()
    
    # Tempatkan 3 item secara acak
    lokasi_item = tempatkan_item(lokasi_mungkin)
    
    print("Lokasi item yang mungkin ditandai dengan '$':")
    tampilkan_grid()
    
    for _ in range(A):
        if not periksa_langkah_valid(x, y, 'A'):
            print("Anda menabrak rintangan atau mencapai batas atas. Game Over!")
            break
        x -= 1
    
    for _ in range(B):
        if not periksa_langkah_valid(x, y, 'B'):
            print("Anda menabrak rintangan atau mencapai batas kanan. Game Over!")
            break
        y += 1
    
    for _ in range(C):
        if not periksa_langkah_valid(x, y, 'C'):
            print("Anda menabrak rintangan atau mencapai batas kiri. Game Over!")
            break
        y -= 1
    
    if (x, y) in lokasi_item:
        print(f"Anda menemukan item di koordinat: ({x}, {y})")
    else:
        print("Anda mencapai akhir perjalanan, tetapi item tidak ditemukan.")
        print("Koordinat item yang mungkin adalah:")
        for i, j in lokasi_item:
            print(f"({i}, {j})")

if __name__ == "__main__":
    main()
import random

# Definisikan layout grid
grid = [
    "########",
    "#......#",
    "#.###..#",
    "#...#.##",
    "#X#....#",
    "#######"
]

# Fungsi untuk menampilkan grid
def tampilkan_grid():
    for baris in grid:
        print(baris)

# Fungsi untuk mencari lokasi item yang mungkin
def cari_lokasi_item_mungkin():
    lokasi_mungkin = []
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[i]) - 1):
            if grid[i][j] == '.':
                lokasi_mungkin.append((i, j))
    return lokasi_mungkin

# Fungsi untuk menempatkan 3 item secara acak di dalam grid
def tempatkan_item(lokasi_mungkin):
    lokasi_item = random.sample(lokasi_mungkin, 3)
    for i, j in lokasi_item:
        grid[i] = grid[i][:j] + '$' + grid[i][j+1:]
    return lokasi_item

# Fungsi untuk memeriksa apakah pergerakan ke atas, ke bawah, atau ke kiri adalah langkah yang valid
def periksa_langkah_valid(x, y, langkah):
    if langkah == 'A':
        return 0 <= x - 1 < len(grid) and grid[x - 1][y] != '#'
    elif langkah == 'B':
        return 0 <= y + 1 < len(grid[0]) and grid[x][y + 1] != '#'
    elif langkah == 'C':
        return 0 <= y - 1 < len(grid[0]) and grid[x][y - 1] != '#'
    else:
        return False

# Fungsi utama permainan
def main():
    tampilkan_grid()
    
    # Koordinat awal pemain (X)
    x, y = 4, 1
    
    while True:
        try:
            A = int(input("Masukkan jumlah langkah ke atas (A): "))
            B = int(input("Masukkan jumlah langkah ke kanan (B): "))
            C = int(input("Masukkan jumlah langkah ke kiri (C): "))
            break
        except ValueError:
            print("Masukkan angka yang valid untuk jumlah langkah.")
    
    # Cari lokasi item yang mungkin secara acak
    lokasi_mungkin = cari_lokasi_item_mungkin()
    
    # Tempatkan 3 item secara acak
    lokasi_item = tempatkan_item(lokasi_mungkin)
    
    print("Lokasi item yang mungkin ditandai dengan '$':")
    tampilkan_grid()
    
    for _ in range(A):
        if not periksa_langkah_valid(x, y, 'A'):
            print("Anda menabrak rintangan atau mencapai batas atas. Game Over!")
            break
        x -= 1
    
    for _ in range(B):
        if not periksa_langkah_valid(x, y, 'B'):
            print("Anda menabrak rintangan atau mencapai batas kanan. Game Over!")
            break
        y += 1
    
    for _ in range(C):
        if not periksa_langkah_valid(x, y, 'C'):
            print("Anda menabrak rintangan atau mencapai batas kiri. Game Over!")
            break
        y -= 1
    
    if (x, y) in lokasi_item:
        print(f"Anda menemukan item di koordinat: ({x}, {y})")
    else:
        print("Anda mencapai akhir perjalanan, tetapi item tidak ditemukan.")
        print("Koordinat item yang mungkin adalah:")
        for i, j in lokasi_item:
            print(f"({i}, {j})")

if __name__ == "__main__":
    main()
