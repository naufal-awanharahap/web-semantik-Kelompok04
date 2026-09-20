# Pertemuan 4 — Metadata dan Interoperabilitas

## Identitas sumber

* **Judul:** Klasifikasi Topik Skripsi Berdasarkan Makna dengan Pendekatan Semantik Web
* **Pembuat:** Aditya Pradana dan Randy Ridwansyah
* **URI sumber:** https://www.jurnal.pcr.ac.id/index.php/jkt/id/article/view/4603
* **Jenis sumber:** Text (Artikel jurnal)
* **Deskripsi:** Artikel ilmiah yang membahas klasifikasi topik skripsi berdasarkan makna menggunakan pendekatan Semantik Web, dengan penerapan ontologi, RDF, dan SPARQL.
* **Tanggal:** 2021-05-31
* **Bahasa:** id
* **Hak:** Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)
* **DOI:** 10.35143/jkt.v7i1.4603

## Pemetaan Dublin Core Terms

| Properti              | Nilai                                                                                                                                                     | Alasan pemilihan                                                                                 |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| `dcterms:title`       | Klasifikasi Topik Skripsi Berdasarkan Makna dengan Pendekatan Semantik Web                                                                                | Digunakan untuk menunjukkan judul resmi artikel sehingga sumber dapat dikenali dengan jelas.     |
| `dcterms:creator`     | Aditya Pradana dan Randy Ridwansyah                                                                                                                       | Digunakan untuk menunjukkan penulis atau pembuat artikel.                                        |
| `dcterms:description` | Artikel ilmiah yang membahas klasifikasi topik skripsi berdasarkan makna menggunakan pendekatan Semantik Web, dengan penerapan ontologi, RDF, dan SPARQL. | Digunakan untuk memberikan gambaran singkat mengenai isi dan topik utama artikel.                |
| `dcterms:created`     | 2021-05-31                                                                                                                                                | Digunakan untuk mencatat tanggal publikasi artikel dalam format ISO 8601.                        |
| `dcterms:type`        | Text                                                                                                                                                      | Digunakan untuk menunjukkan bahwa sumber merupakan dokumen teks berupa artikel jurnal.           |
| `dcterms:language`    | id                                                                                                                                                        | Digunakan untuk menunjukkan bahwa bahasa utama artikel adalah bahasa Indonesia.                  |
| `dcterms:rights`      | Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)                                                                 | Digunakan untuk memberikan informasi mengenai hak dan lisensi penggunaan sumber.                 |
| `dcterms:identifier`  | 10.35143/jkt.v7i1.4603                                                                                                                                    | Digunakan sebagai identitas DOI yang dapat digunakan untuk mengidentifikasi artikel secara unik. |
| `dcterms:source`      | https://www.jurnal.pcr.ac.id/index.php/jkt/id/article/view/4603                                                                                           | Digunakan untuk menunjukkan halaman resmi tempat artikel diterbitkan.                            |

## Hasil Validasi

### JSON-LD Playground

File `metadata-sumber.jsonld` diuji menggunakan JSON-LD Playground untuk memastikan struktur JSON-LD dapat diproses dan metadata dapat direpresentasikan dalam bentuk RDF. Pengujian juga digunakan untuk memastikan URI subjek dan properti metadata sesuai dengan pemetaan Dublin Core Terms.

**Hasil:** Struktur JSON-LD dapat diproses dan metadata dapat direpresentasikan dalam bentuk RDF.

### Schema Markup Validator

File `metadata-schema.jsonld` diuji menggunakan Schema Markup Validator untuk memeriksa struktur data terstruktur yang menggunakan vocabulary Schema.org.

**Hasil:** Struktur JSON-LD menggunakan vocabulary Schema.org dan dapat diproses oleh validator.

## Refleksi

### 1. Mengapa URI yang sama penting untuk Turtle dan JSON-LD?

URI yang sama digunakan agar metadata dalam format Turtle dan JSON-LD merujuk pada sumber yang sama. Dengan demikian, kedua format dapat dikenali sebagai representasi metadata dari satu resource yang sama.

### 2. Apa perbedaan peran DC Terms dan schema.org pada pekerjaan ini?

Dublin Core Terms digunakan untuk mendeskripsikan metadata sumber secara umum, seperti judul, pembuat, deskripsi, tanggal, jenis, bahasa, dan hak. Sementara itu, Schema.org digunakan untuk merepresentasikan informasi dalam vocabulary yang dapat dipahami oleh aplikasi dan mesin pada web.

### 3. Sebutkan satu risiko jika metadata HTML, Turtle, dan JSON-LD tidak konsisten.

Jika metadata HTML, Turtle, dan JSON-LD tidak konsisten, informasi mengenai sumber dapat berbeda antarformat. Misalnya, judul atau nama pembuat berbeda sehingga sistem dapat mengalami kesulitan dalam mengenali bahwa metadata tersebut merujuk pada sumber yang sama.

## Catatan Akhir

Metadata pada HTML, Turtle, dan JSON-LD disusun berdasarkan sumber artikel jurnal yang sama dan menggunakan URI sumber yang konsisten. Informasi utama seperti judul, pembuat, deskripsi, tanggal, bahasa, jenis, DOI, dan hak disusun secara konsisten pada setiap format. Perbedaan format dan vocabulary digunakan sesuai dengan fungsi masing-masing sehingga metadata dapat dipertukarkan dan mendukung interoperabilitas antar sistem.

