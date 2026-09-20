# Pertemuan 4 — Metadata dan Interoperabilitas

Identitas sumber

- Judul: Evolusi Penggunaan Teknologi Web 3.0 : Semantic Web
- Pembuat: Himawan, Trinugi Wira Harjanti, Ruli Supriati, dan Hari Setiyani
- URI sumber: https://jurnal.istts.ac.id/index.php/insight/article/view/107
- Jenis sumber: Text (Artikel jurnal)
- Deskripsi: Artikel ilmiah yang membahas perkembangan Web 3.0 atau Semantic Web serta teknologi RDF, SPARQL, dan Web Ontology.
- Tanggal: 2020-11-16
- Bahasa: id
- Hak: Hak Cipta Penulis
- DOI: 10.37823/insight.v2i02.107

## Pemetaan Dublin Core Terms
| Properti | Nilai | Alasan pemilihan |
|---|---|---|
| dcterms:title | Evolusi Penggunaan Teknologi Web 3.0: Semantic Web | Digunakan untuk menunjukkan judul resmi sumber agar sumber dapat dikenali dengan jelas. |
| dcterms:creator | Himawan, Trinugi Wira Harjanti, Ruli Supriati, dan Hari Setiyani | Digunakan untuk menunjukkan pihak yang membuat atau menulis artikel. |
| dcterms:description | Artikel ilmiah yang membahas perkembangan Web 3.0 atau Semantic Web serta teknologi RDF, SPARQL, dan Web Ontology. | Digunakan untuk memberikan gambaran singkat mengenai isi sumber. |
| dcterms:created | 2020-11-16 | Digunakan untuk mencatat tanggal sumber dalam format ISO 8601. |
| dcterms:type | Text | Digunakan untuk menunjukkan bahwa sumber merupakan dokumen teks berupa artikel jurnal. |
| dcterms:language | id | Digunakan untuk menunjukkan bahwa bahasa yang digunakan dalam sumber adalah bahasa Indonesia. |
| dcterms:rights | Hak Cipta Penulis | Digunakan untuk memberikan informasi mengenai hak atas sumber. |
| dcterms:identifier | 10.37823/insight.v2i02.107 | Digunakan sebagai identitas DOI yang dapat digunakan untuk mengidentifikasi artikel. |
| dcterms:source | https://jurnal.istts.ac.id/index.php/insight/article/view/107 | Digunakan untuk menunjukkan halaman sumber artikel jurnal. |

## Hasil validasi

### JSON-LD Playground
File `metadata-sumber.jsonld` diuji menggunakan JSON-LD Playground untuk memastikan struktur JSON-LD dapat diproses dan direpresentasikan dalam bentuk RDF. URI subjek dan properti metadata disusun berdasarkan pemetaan Dublin Core Terms.

### Schema Markup Validator
File `metadata-schema.jsonld` diuji menggunakan Schema Markup Validator untuk memastikan metadata menggunakan vocabulary Schema.org dan dapat diproses sebagai data terstruktur.

## Refleksi

### Mengapa URI yang sama penting untuk Turtle dan JSON-LD?

URI yang sama digunakan agar metadata dalam format Turtle dan JSON-LD merujuk pada sumber yang sama. Dengan demikian, kedua format tersebut dapat dikenali sebagai representasi metadata dari satu resource.

### Apa perbedaan peran DC Terms dan schema.org pada pekerjaan ini?

DC Terms digunakan untuk mendeskripsikan metadata sumber seperti judul, pembuat, deskripsi, tanggal, bahasa, dan hak. Sementara itu, Schema.org digunakan untuk memberikan struktur metadata yang dapat dipahami oleh aplikasi dan mesin pencari di web.

### Sebutkan satu risiko jika metadata HTML, Turtle, dan JSON-LD tidak konsisten.

Jika metadata HTML, Turtle, dan JSON-LD tidak konsisten, informasi yang diterima oleh sistem dapat berbeda, misalnya judul atau pembuat tidak sama. Hal tersebut dapat menyebabkan sumber sulit dikenali atau dihubungkan dengan benar.
