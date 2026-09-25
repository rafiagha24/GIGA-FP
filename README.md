## Catch! GDD

## 1. Description

Catch! adalah game arcade sederhana di mana pemain menggerakkan karakter ke kiri dan kanan untuk menangkap makanan yang jatuh dari langit. Pemain harus mengumpulkan skor sebanyak mungkin sambil menghindari bom. Seiring berjalannya waktu, benda yang jatuh akan bergerak semakin cepat sehingga tingkat kesulitan meningkat.

---

## 2. Game Objective

Tujuan utama pemain adalah memperoleh score setinggi mungkin sebelum seluruh nyawa habis.

Pemain harus:
- Menangkap makanan untuk mendapatkan poin.
- Memprioritaskan makanan dengan nilai poin lebih tinggi.
- Menghindari bom.
- Beradaptasi dengan kecepatan benda yang terus meningkat.

---

## 3. Core Gameplay Loop

1. Benda muncul secara acak dari bagian atas layar.
2. Benda jatuh menuju ground.
3. Pemain bergerak ke kiri atau kanan.
4. Jika benda bertabrakan dengan player:
   - Food = score bertambah 1.
   - Double Food = score bertambah 2.
   - Bomb = nyawa berkurang 1.
5. Setelah terkena player atau mencapai ground, benda baru muncul.
6. Setiap 10 detik, kecepatan benda yang jatuh meningkat.
7. Permainan berakhir ketika nyawa mencapai 0.

---

## 4. Player

### Deskripsi

Player merupakan karakter yang dikendalikan menggunakan keyboard dan berada di area ground.

### Kontrol

| Input | Aksi |
|---|---|
| Left Arrow | Bergerak ke kiri |
| Right Arrow | Bergerak ke kanan |

### Batas Gerakan

Player tidak dapat bergerak melewati batas kiri dan kanan layar.

---

## 5. Item

Terdapat tiga jenis item yang dapat muncul secara acak.

| Item | Warna | Efek |
|---|---|---|
| Food | Merah | Score +1 |
| Double Food | Kuning | Score +2 |
| Bomb | Hitam | Nyawa -1 |

### Food

Food merupakan item normal yang memberikan **1 poin** ketika ditangkap.

### Double Food

Double Food merupakan item khusus yang memberikan **2 poin** ketika ditangkap. Item ini memberikan reward lebih besar sehingga pemain memiliki alasan untuk mengejarnya.

### Bomb

Bomb merupakan item berbahaya. Jika player bertabrakan dengan bomb, player kehilangan **1 nyawa**.

---

## 6. Scoring System

Score diperoleh berdasarkan item yang berhasil ditangkap.

| Kondisi | Perubahan Score |
|---|---:|
| Menangkap Food | +1 |
| Menangkap Double Food | +2 |
| Menangkap Bomb | Tidak menambah score |

Score ditampilkan selama permainan.

---

## 7. Health / Lives System

Player memulai permainan dengan **3 nyawa**.

Setiap kali player terkena bomb:

```text
Lives = Lives - 1
```

Ketika:

```text
Lives = 0
```

permainan berakhir dan menampilkan **GAME OVER**.

---

## 8. Difficulty Progression

Tingkat kesulitan meningkat berdasarkan waktu permainan.

Kecepatan awal item adalah:

```text
Speed = 3
```

Setiap 10 detik, kecepatan bertambah 1.

Contoh:

| Waktu | Kecepatan |
|---|---:|
| 0–9 detik | 3 |
| 10–19 detik | 4 |
| 20–29 detik | 5 |
| 30–39 detik | 6 |
| 40–49 detik | 7 |

Dengan sistem ini, permainan akan semakin sulit semakin lama pemain bertahan.

---

## 9. Item Spawn System

Item muncul dari bagian atas layar dengan posisi horizontal yang dipilih secara acak.

Posisi X item ditentukan menggunakan randomizer:

```python
random.randint(0, WIDTH - item.width)
```

Jenis item juga dipilih secara acak dari:

```python
random.choice([
    "food",
    "double",
    "bomb"
])
```

Dengan demikian, pemain tidak dapat mengetahui jenis maupun posisi item berikutnya.

---

## 10. Collision System

Game menggunakan `pygame.Rect` untuk menangani collision.

Collision antara player dan item diperiksa menggunakan:

```python
item.colliderect(player)
```

Jika collision terjadi, efek item dijalankan sesuai dengan jenisnya.

---

## 11. Game Over

Game berakhir ketika player kehilangan seluruh nyawa.

Tampilan game over menampilkan:

```text
GAME OVER
```

Game berhenti menerima input gameplay setelah kondisi game over tercapai.

---

## 12. User Interface

Informasi yang ditampilkan selama permainan:

```text
Score: 0
Lives: 3
```

Informasi speed tidak ditampilkan kepada pemain agar UI tetap sederhana.

Ketika player kehilangan seluruh nyawa:

```text
GAME OVER
```

ditampilkan di tengah layar.

---

## 13. Visual Style

Game menggunakan visual sederhana berbasis bentuk persegi untuk memudahkan implementasi dan menjaga fokus pada gameplay.

### Warna Utama

- **Player:** Biru
- **Ground:** Hijau
- **Food:** Merah
- **Double Food:** Kuning
- **Bomb:** Hitam
- **Background:** Putih

Visual dapat dikembangkan lebih lanjut dengan sprite, animasi, efek partikel, dan sound effect.

---

## 14. Game State

Game memiliki dua kondisi utama:

### Playing

Player dapat bergerak dan item terus jatuh.

```python
game_over = False
```

### Game Over

Player sudah kehilangan seluruh nyawa.

```python
game_over = True
```

Saat kondisi ini aktif, gameplay dihentikan.

---

## 15. Game Flow

```text
START
  |
  v
Player mulai dengan 3 Lives
  |
  v
Item muncul secara random
  |
  v
Item jatuh
  |
  +----> Player menangkap Food
  |             |
  |             v
  |          Score +1
  |
  +----> Player menangkap Double Food
  |             |
  |             v
  |          Score +2
  |
  +----> Player terkena Bomb
  |             |
  |             v
  |          Lives -1
  |
  v
Item baru muncul
  |
  v
Setiap 10 detik → Speed meningkat
  |
  v
Lives = 0?
  |
  +---- Tidak ----> Permainan berlanjut
  |
  +---- Ya -------> GAME OVER
```

---

## 16. Summary

**Catch the Food** merupakan game arcade sederhana yang berfokus pada refleks dan pengambilan keputusan. Pemain harus mengumpulkan makanan untuk mendapatkan score sambil menghindari bomb. Adanya Double Food memberikan kesempatan untuk mendapatkan score lebih besar, sedangkan peningkatan kecepatan item secara berkala membuat permainan semakin menantang.

Game dirancang dengan mekanik yang sederhana sehingga cocok sebagai proyek pembelajaran Pygame, terutama untuk memahami game loop, input handling, collision detection, randomization, timer, scoring, dan game state.
