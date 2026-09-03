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

1. Root element yang diizinkan: `buku`.
2. Tipe data elemen `judul`: `xs:string`.
3. Tipe data elemen `tahun`: `xs:gYear`.
4. Tipe data elemen `harga`: `xs:decimal`.
5. Atribut `isbn` wajib dituliskan karena pada XSD menggunakan `use="required"`.

## 5. Pertanyaan Evaluasi

1. **Apa perbedaan utama XML dan HTML?**  
   XML digunakan untuk menyimpan dan mengorganisasi data secara terstruktur, sedangkan HTML digunakan untuk menampilkan dan mengatur tampilan informasi pada halaman web.

2. **Apa yang dimaksud XML yang well-formed?**  
   XML well-formed adalah dokumen XML yang mengikuti aturan sintaks XML dengan benar, seperti memiliki satu root element, tag pembuka dan penutup yang sesuai, serta struktur elemen yang benar.

3. **Jelaskan perbedaan well-formed dan valid.**  
   Well-formed berarti dokumen mengikuti aturan sintaks XML. Valid berarti dokumen tidak hanya well-formed, tetapi juga sesuai dengan aturan struktur yang ditentukan oleh schema seperti XSD.

4. **Mengapa XSD lebih kuat dibandingkan DTD?**  
   XSD mendukung lebih banyak tipe data, namespace, serta aturan struktur dan validasi data yang lebih rinci dibandingkan DTD.

5. **Mengapa namespace penting ketika data XML berasal dari beberapa kosakata berbeda?**  
   Namespace mencegah konflik nama elemen yang sama dengan memberikan identitas berbeda berdasarkan namespace masing-masing.

6. **Apa kegunaan XPath dalam pengolahan dokumen XML?**  
   XPath digunakan untuk memilih, mencari, dan mengambil elemen, atribut, atau nilai tertentu dari struktur dokumen XML.
