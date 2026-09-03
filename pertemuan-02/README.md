# Pertemuan 2 - Format Dokumen XML

## 1. Profil XML

File `profil_saya.xml` dibuat untuk menyimpan data profil mahasiswa dalam struktur XML yang well-formed.

## 2. Analisis Kesalahan XML

| No | Bagian yang Salah | Alasan | Perbaikan |
|---|---|---|---|
| 1 | `<nama>Budi Santoso</Nama>` | Huruf besar dan kecil pada tag XML bersifat case-sensitive. Tag pembuka dan penutup harus sama. | Ubah menjadi `<nama>Budi Santoso</nama>` |
| 2 | `<hobi>Programming</hobi>` lalu `<hobi>Membaca</hobi>` tanpa masalah struktur lain, tetapi jika ada tag yang tidak ditutup maka XML menjadi tidak well-formed. | Setiap elemen XML wajib memiliki tag penutup yang sesuai. | Pastikan setiap `<hobi>` ditutup dengan `</hobi>` |
| 3 | `<deskripsi>Saya suka AI & Web Semantik</deskripsi>` | Karakter `&` tidak boleh ditulis langsung dalam XML karena merupakan karakter khusus. | Ubah menjadi `Saya suka AI &amp; Web Semantik` |
