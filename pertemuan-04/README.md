# Pertemuan 4 — Metadata dan Interoperabilitas

## Identitas sumber

* **Judul:** Evolusi Penggunaan Teknologi Web 3.0 : Semantic Web
* **Pembuat:** Himawan, Trinugi Wira Harjanti, Ruli Supriati, dan Hari Setiyani
* **URI sumber:** https://jurnal.istts.ac.id/index.php/insight/article/view/107
* **Jenis sumber:** Text (Artikel jurnal)
* **Deskripsi:** Artikel ilmiah yang membahas perkembangan Web 3.0 atau Semantic Web, termasuk karakteristik serta teknologi RDF (Resource Description Framework), SPARQL, dan Web Ontology.
* **Tanggal:** 2020-11-16
* **Bahasa:** id
* **Hak:** Creative Commons Attribution 4.0 International (CC BY 4.0)
* **DOI:** 10.37823/insight.v2i02.107

## Pemetaan Dublin Core Terms

| Properti              | Nilai                                                                                                                                      | Alasan pemilihan                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------ |
| `dcterms:title`       | Evolusi Penggunaan Teknologi Web 3.0 : Semantic Web                                                                                        | Digunakan untuk menunjukkan judul resmi artikel sehingga sumber dapat dikenali dengan jelas.     |
| `dcterms:creator`     | Himawan, Trinugi Wira Harjanti, Ruli Supriati, dan Hari Setiyani                                                                           | Digunakan untuk menunjukkan pihak yang membuat atau menulis artikel.                             |
| `dcterms:description` | Artikel ilmiah yang membahas perkembangan Web 3.0 atau Semantic Web, termasuk karakteristik serta teknologi RDF, SPARQL, dan Web Ontology. | Digunakan untuk memberikan gambaran singkat mengenai isi artikel.                                |
| `dcterms:created`     | 2020-11-16                                                                                                                                 | Digunakan untuk mencatat tanggal publikasi artikel dalam format ISO 8601.                        |
| `dcterms:type`        | Text                                                                                                                                       | Digunakan untuk menunjukkan bahwa sumber merupakan dokumen teks berupa artikel jurnal.           |
| `dcterms:language`    | id                                                                                                                                         | Digunakan untuk menunjukkan bahwa bahasa utama artikel adalah bahasa Indonesia.                  |
| `dcterms:rights`      | Creative Commons Attribution 4.0 International (CC BY 4.0)                                                                                 | Digunakan untuk memberikan informasi mengenai hak penggunaan dan lisensi sumber.                 |
| `dcterms:identifier`  | 10.37823/insight.v2i02.107                                                                                                                 | Digunakan sebagai identitas DOI yang dapat digunakan untuk mengidentifikasi artikel secara unik. |
| `dcterms:source`      | https://jurnal.istts.ac.id/index.php/insight/article/view/107                                                                              | Digunakan untuk menunjukkan halaman resmi tempat artikel diterbitkan.                            |

## Hasil Validasi

### JSON-LD Playground

File `metadata-sumber.jsonld` diuji menggunakan JSON-LD Playground untuk memastikan struktur JSON-LD dapat diproses dan direpresentasikan dalam bentuk RDF. Pengujian juga digunakan untuk memastikan URI subjek dan properti metadata sesuai dengan pemetaan Dublin Core Terms.

**Hasil:** Struktur JSON-LD dapat diproses dan metadata dapat direpresentasikan dalam bentuk RDF.

### Schema Markup Validator

File `metadata-schema.jsonld` diuji menggunakan Schema Markup Validator untuk memeriksa struktur data terstruktur yang menggunakan vocabulary Schema.org.

**Hasil:** Struktur JSON-LD menggunakan vocabulary Schema.org dan dapat diproses oleh validator.

## Refleksi

### 1. Mengapa URI yang sama penting untuk Turtle dan JSON-LD?

URI yang sama digunakan agar metadata dalam format Turtle dan JSON-LD merujuk pada sumber yang sama. Dengan menggunakan identitas sumber yang sama, kedua format tersebut dapat dipahami sebagai representasi metadata dari satu resource yang sama.

### 2. Apa perbedaan peran DC Terms dan schema.org pada pekerjaan ini?

Dublin Core Terms digunakan untuk mendeskripsikan metadata sumber secara umum, seperti judul, pembuat, deskripsi, tanggal, bahasa, jenis, dan hak. Sementara itu, Schema.org digunakan untuk merepresentasikan informasi dalam vocabulary yang banyak digunakan pada data terstruktur di web sehingga dapat dipahami oleh aplikasi dan mesin.

### 3. Sebutkan satu risiko jika metadata HTML, Turtle, dan JSON-LD tidak konsisten.

Jika metadata HTML, Turtle, dan JSON-LD tidak konsisten, informasi mengenai suatu sumber dapat berbeda antarformat. Misalnya, judul atau nama pembuat berbeda sehingga sistem dapat mengalami kesulitan dalam mengenali bahwa metadata tersebut merujuk pada sumber yang sama.

## Catatan Akhir

Metadata pada HTML, Turtle, dan JSON-LD dibuat berdasarkan sumber jurnal yang sama dan menggunakan URI sumber yang konsisten. Informasi utama seperti judul, pembuat, deskripsi, tanggal, bahasa, jenis, DOI, dan hak disusun secara konsisten pada setiap format. Perbedaan format dan vocabulary digunakan sesuai dengan fungsi masing-masing sehingga metadata dapat dipertukarkan dan mendukung interoperabilitas antar sistem.
