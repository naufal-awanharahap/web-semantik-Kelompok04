# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: [30]
- Triple dengan LIMIT 30: [90]
- Baris SELECT LIMIT 10 / kota berbeda: [10] / [10]
- Mengapa tidak (atau mengapa tepat) 30 triple:
  Karena terdapat tiga pola triple dalam template CONSTRUCT. Setiap solution dapat menghasilkan maksimal tiga triple. Dengan LIMIT 10, batas maksimalnya adalah 30 triple. Namun, jumlah sebenarnya dapat lebih sedikit karena triple yang sama hanya disimpan satu kali dalam RDF Graph.

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: [12] triple, film tanpa tanggal: [sesuai query lokal]
- Sumber data: DBpedia / data contoh film.ttl
- Triple yang tetap tercetak untuk film tanpa tanggal:
  Triple schema:Movie, schema:name, dan schema:director tetap tercetak. Sementara itu, schema:datePublished tidak tercetak karena film tersebut tidak mempunyai tanggal rilis. Hal ini terjadi karena tanggal rilis menggunakan OPTIONAL sehingga tidak wajib ditemukan.
- Query lokal tanpa internet:
  Query lokal dapat dijalankan tanpa internet karena data sudah disimpan dalam file film_nolan.ttl. RDFLib membaca data dari file lokal sehingga tidak perlu menghubungi DBpedia lagi. Namun, apabila seluruh demo_c.py dijalankan ulang tanpa internet, pengambilan data dari endpoint DBpedia akan gagal.
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl:
  Karena query CONSTRUCT mengubah tipe film menjadi schema:Movie, bukan dbo:Film. Oleh karena itu, pencarian menggunakan dbo:Film tidak menemukan triple yang sesuai dan menghasilkan 0.

## Bagian C - Materialisasi
- Output demo_d.py: [isi]
- Mengapa Ada Rina bernilai 3: [jawaban]
- Output materialisasi_ulang.py: [isi]
- Tiga triple yang bukan baru: [jawaban]
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa: [jawaban]

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | [isi] | [isi] | [isi] | [isi] |
| rusak_b | [isi] | [isi] | [isi] | [isi] |
| rusak_c | [isi] | [isi] | [isi] | [isi] |

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | [isi] | [isi] |
| 2 LIMIT | [isi] | [isi] |
| 3 Simpan, jangan ulangi | [isi] | [isi] |
| 4 Jangkar jalur | [isi] | [isi] |
- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya: [isi]

### Diskusi 1 - Taksonomi berubah
[150-250 kata]

### Diskusi 2 - SELECT atau CONSTRUCT
[150-250 kata]

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| CONSTRUCT mencetak template sekali per solution dan menggabungkan triple kembar. | Bagian A: terdapat tiga pola template. LIMIT 10 memiliki batas atas 30 triple, tetapi triple kembar hanya dihitung satu kali.
| 2 | [isi] |
| 3 | [isi] |
| 4 | [isi] |
| 5 | [isi] |
