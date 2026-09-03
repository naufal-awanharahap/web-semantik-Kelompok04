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

1. Root element: buku

2. Tipe data judul: xs:string

3. Tipe data tahun: xs:gYear

4. Tipe data harga: xs:decimal

5. Atribut ISBN: atribut ISBN tidak boleh tidak ditulis karena terdapat use="required" yang dimana atribut tersebut wajib untuk ditulis
