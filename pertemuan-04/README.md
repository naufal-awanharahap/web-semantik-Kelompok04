# Pertemuan 4 — Metadata dan Interoperabilitas

## Identitas sumber

* **Judul:** A Semantic Web Primer for Object-Oriented Software Developers
* **Pembuat:** Holger Knublauch, Daniel Oberle, Phil Tetlow, dan Evan Wallace
* **URI sumber:** https://www.w3.org/TR/sw-oosd-primer/
* **Jenis sumber:** LearningResource
* **Deskripsi:** Materi pengantar yang membahas teknologi Semantic Web, khususnya RDF Schema dan OWL, serta penggunaannya bersama bahasa pemrograman berorientasi objek.
* **Tanggal:** 2006-03-09
* **Bahasa:** en
* **Hak:** Copyright © 2006 W3C

## Pemetaan Dublin Core Terms

| Properti              | Nilai                                                                                                                                                   | Alasan pemilihan                                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| `dcterms:title`       | A Semantic Web Primer for Object-Oriented Software Developers                                                                                           | Digunakan untuk menunjukkan judul resmi sumber.                                 |
| `dcterms:creator`     | Holger Knublauch, Daniel Oberle, Phil Tetlow, dan Evan Wallace                                                                                          | Digunakan untuk menunjukkan pihak yang menyusun sumber.                         |
| `dcterms:description` | Materi pengantar yang membahas teknologi Semantic Web, khususnya RDF Schema dan OWL, serta penggunaannya bersama bahasa pemrograman berorientasi objek. | Digunakan untuk memberikan gambaran singkat mengenai isi sumber.                |
| `dcterms:created`     | 2006-03-09                                                                                                                                              | Digunakan untuk mencatat tanggal sumber dalam format ISO 8601.                  |
| `dcterms:type`        | LearningResource                                                                                                                                        | Digunakan untuk menunjukkan bahwa sumber digunakan sebagai materi pembelajaran. |
| `dcterms:language`    | en                                                                                                                                                      | Digunakan untuk menunjukkan bahwa sumber menggunakan bahasa Inggris.            |
| `dcterms:rights`      | Copyright © 2006 W3C                                                                                                                                    | Digunakan untuk memberikan informasi mengenai hak atas sumber.                  |
| `dcterms:identifier`  | https://www.w3.org/TR/sw-oosd-primer/                                                                                                                   | Digunakan sebagai URI yang mengidentifikasi sumber secara stabil.               |

## Hasil validasi

### JSON-LD Playground

File `metadata-sumber.jsonld` diuji menggunakan JSON-LD Playground untuk memastikan struktur JSON-LD dapat diproses dan direpresentasikan dalam bentuk RDF. URI subjek dan properti metadata disusun berdasarkan pemetaan Dublin Core Terms.

### Schema Markup Validator

File `metadata-schema.jsonld` diuji menggunakan Schema Markup Validator untuk memastikan metadata menggunakan vocabulary Schema.org dan dapat diproses sebagai data terstruktur.

## Refleksi

### Mengapa URI yang sama penting untuk Turtle dan JSON-LD?

URI yang sama digunakan agar metadata dalam format Turtle dan JSON-LD merujuk pada sumber yang sama. Dengan demikian, kedua format tersebut dapat dikenali sebagai representasi metadata dari satu sumber.

### Apa perbedaan peran DC Terms dan schema.org pada pekerjaan ini?

DC Terms digunakan untuk mendeskripsikan metadata sumber seperti judul, pembuat, deskripsi, tanggal, bahasa, dan hak. Sementara itu, Schema.org digunakan untuk memberikan struktur metadata dengan vocabulary yang berbeda sehingga dapat diproses oleh aplikasi dan sistem web.

### Sebutkan satu risiko jika metadata HTML, Turtle, dan JSON-LD tidak konsisten.

Jika metadata HTML, Turtle, dan JSON-LD tidak konsisten, informasi yang diterima oleh sistem dapat berbeda, misalnya judul atau pembuat tidak sama. Hal tersebut dapat menyebabkan sumber sulit dikenali atau dihubungkan dengan benar.

## Catatan akhir

Metadata pada HTML, Turtle, dan JSON-LD disusun dengan menggunakan URI sumber yang sama serta informasi utama yang konsisten, seperti judul, pembuat, deskripsi, tanggal, bahasa, dan hak. Perbedaan format dan vocabulary tetap digunakan sesuai fungsi masing-masing sehingga metadata dapat mendukung interoperabilitas antar sistem.
