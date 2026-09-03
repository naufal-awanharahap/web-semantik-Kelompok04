# Pertemuan 2 - Format Dokumen XML

## 1. Profil XML

File `profil_saya.xml` dibuat untuk menyimpan data profil mahasiswa dalam struktur XML yang well-formed.

## 2. Analisis Kesalahan XML

| No | Bagian yang Salah                                    | Alasan                                                                                          | Perbaikan                                                             |
| -- | ---------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------------------------- |
| 1  | `<nama>Budi Santoso</Nama>`                          | XML bersifat *case-sensitive*. Tag pembuka `<nama>` dan tag penutup `</Nama>` dianggap berbeda. | Ubah menjadi `<nama>Budi Santoso</nama>`                              |
| 2  | `<angkatan>2024`                                     | Elemen `<angkatan>` tidak memiliki tag penutup sehingga dokumen XML tidak *well-formed*.        | Ubah menjadi `<angkatan>2024</angkatan>`                              |
| 3  | `<deskripsi>Saya suka AI & Web Semantik</deskripsi>` | Karakter `&` merupakan karakter khusus dalam XML sehingga tidak boleh ditulis secara langsung.  | Ubah menjadi `<deskripsi>Saya suka AI &amp; Web Semantik</deskripsi>` |

## 3. Analisis XML Schema
```text
Root element yang diizinkan: buku.
Tipe data elemen judul: xs:string.
Tipe data elemen tahun: xs:gYear.
Tipe data elemen harga: xs:decimal.
Atribut isbn wajib dituliskan karena pada XSD menggunakan use="required".
```
