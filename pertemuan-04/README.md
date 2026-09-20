# Pertemuan 4 — Metadata dan Interoperabilitas

Tautan Repository : https://github.com/naufal-awanharahap/web-semantik-Kelompok04/tree/main/pertemuan-04

## Identitas sumber

* **Judul:** Introduction to the Semantic Web (tutorial)
* **Pembuat:** Ivan Herman
* **URI sumber:** https://www.w3.org/events/talks/2009/introduction-to-the-semantic-web-2/
* **Jenis sumber:** LearningResource
* **Deskripsi:** Tutorial yang memberikan pengantar mengenai teknologi dasar Semantic Web yang dikembangkan oleh W3C, termasuk RDF, RDF Schema, SPARQL, OWL, OWL 2, dan RIF.
* **Tanggal:** 2009-10-30
* **Bahasa:** en
* **Hak:** W3C

## Pemetaan Dublin Core Terms

| Properti              | Nilai                                                                                                                                                       | Alasan pemilihan                                                                        |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- |
| `dcterms:title`       | Introduction to the Semantic Web (tutorial)                                                                                                                 | Digunakan untuk menunjukkan judul sumber agar dapat dikenali dengan jelas.              |
| `dcterms:creator`     | Ivan Herman                                                                                                                                                 | Digunakan untuk menunjukkan pembicara atau pembuat materi tutorial.                     |
| `dcterms:description` | Tutorial yang memberikan pengantar mengenai teknologi dasar Semantic Web yang dikembangkan oleh W3C, termasuk RDF, RDF Schema, SPARQL, OWL, OWL 2, dan RIF. | Digunakan untuk memberikan gambaran singkat mengenai isi sumber.                        |
| `dcterms:created`     | 2009-10-30                                                                                                                                                  | Digunakan untuk mencatat tanggal tutorial dalam format ISO 8601.                        |
| `dcterms:type`        | LearningResource                                                                                                                                            | Digunakan untuk menunjukkan bahwa sumber merupakan materi pembelajaran berupa tutorial. |
| `dcterms:language`    | en                                                                                                                                                          | Digunakan untuk menunjukkan bahwa sumber menggunakan bahasa Inggris.                    |
| `dcterms:rights`      | W3C                                                                                                                                                         | Digunakan untuk memberikan informasi mengenai pihak yang menyediakan sumber.            |
| `dcterms:identifier`  | https://www.w3.org/events/talks/2009/introduction-to-the-semantic-web-2/                                                                                    | Digunakan sebagai URI yang mengidentifikasi sumber secara stabil.                       |

## Hasil validasi

### JSON-LD Playground

File `metadata-sumber.jsonld` diuji menggunakan JSON-LD Playground untuk memastikan struktur JSON-LD dapat diproses dan direpresentasikan dalam bentuk RDF. URI subjek dan properti metadata disusun berdasarkan pemetaan Dublin Core Terms.

### Schema Markup Validator

File `metadata-schema.jsonld` diuji menggunakan Schema Markup Validator untuk memastikan metadata menggunakan vocabulary Schema.org dan dapat diproses sebagai data terstruktur.

## Refleksi

### Mengapa URI yang sama penting untuk Turtle dan JSON-LD?

URI yang sama digunakan agar metadata dalam format Turtle dan JSON-LD merujuk pada sumber yang sama. Dengan demikian, kedua format tersebut dapat dikenali sebagai representasi metadata dari satu sumber.

### Apa perbedaan peran DC Terms dan schema.org pada pekerjaan ini?

DC Terms digunakan untuk mendeskripsikan metadata sumber seperti judul, pembuat, deskripsi, tanggal, bahasa, jenis, dan hak. Sementara itu, Schema.org digunakan untuk memberikan struktur metadata dengan vocabulary yang berbeda sehingga dapat diproses oleh aplikasi dan sistem web.

### Sebutkan satu risiko jika metadata HTML, Turtle, dan JSON-LD tidak konsisten.

Jika metadata HTML, Turtle, dan JSON-LD tidak konsisten, informasi yang diterima oleh sistem dapat berbeda, misalnya judul atau pembuat tidak sama. Hal tersebut dapat menyebabkan sumber sulit dikenali atau dihubungkan dengan benar.

## Catatan akhir

Metadata pada HTML, Turtle, dan JSON-LD disusun dengan menggunakan URI sumber yang sama serta informasi utama yang konsisten, seperti judul, pembuat, deskripsi, tanggal, bahasa, dan hak. Perbedaan format dan vocabulary tetap digunakan sesuai fungsi masing-masing sehingga metadata dapat mendukung interoperabilitas antar sistem.
