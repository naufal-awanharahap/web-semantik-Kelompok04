# Latihan Pertemuan 3 - JSON-LD dan Structured Data

## Struktur Hasil

- profil_saya.jsonld
- profil_perbaikan.jsonld
- seminar.html
- folder screenshots

## 1. JSON Biasa dan JSON-LD

1. *Perbedaan fungsi kunci:*  
   Pada JSON biasa, kunci seperti nama dan pekerjaan digunakan untuk menyimpan data sesuai kebutuhan pembuat aplikasi. Pada JSON-LD, properti seperti name dan jobTitle mengikuti kosakata Schema.org sehingga makna data dapat dipahami secara konsisten oleh mesin.

2. *Fungsi @context, @type, dan @id:*  
   - @context menentukan kosakata atau konteks yang digunakan dalam JSON-LD.
   - @type menentukan jenis entitas, misalnya Person.
   - @id memberikan identitas unik berupa IRI/URL kepada suatu entitas sehingga dapat dikenali dan dirujuk.

3. *Node tanpa @id:*  
   Node tanpa @id tetap dapat digunakan dalam JSON-LD, tetapi tidak memiliki identitas global yang unik. Node seperti ini disebut blank node sehingga lebih sulit dirujuk secara langsung dari data lain.

## 2. Pemeriksaan schema.org

1. *Alasan memilih tipe paling spesifik:*  
   Tipe yang paling spesifik dipilih agar jenis entitas dapat dijelaskan dengan lebih tepat. Hal ini membantu mesin memahami makna dan konteks data secara lebih akurat.

2. *Nama properti dan bahasa nilai:*  
   Nama properti harus mengikuti kosakata Schema.org agar mempunyai makna yang standar dan dapat dikenali oleh mesin. Sementara itu, nilai dari properti dapat menggunakan bahasa Indonesia karena nilai tersebut merupakan informasi yang ingin disampaikan.

3. *Manfaat array pada knowsAbout:*  
   Array pada knowsAbout memungkinkan satu orang memiliki lebih dari satu bidang pengetahuan atau keahlian. Dengan demikian, beberapa topik dapat disimpan dalam satu properti secara terstruktur.

## 3. Perbaikan Lima Kesalahan

| No. | Bagian Salah | Alasan | Perbaikan |
|-----|--------------|--------|-----------|
| 1 | "@type": "person" | Penulisan tipe Schema.org harus menggunakan kapitalisasi yang benar. | "@type": "Person" |
| 2 | 'name': "Rina Anggraini" | JSON harus menggunakan tanda kutip ganda pada nama properti. | "name": "Rina Anggraini" |
| 3 | "birthDate": "12 September 2004" | Tanggal harus ditulis menggunakan format ISO 8601. | "birthDate": "2004-09-12" |
| 4 | "nomorInduk": "221401001" | nomorInduk bukan properti standar yang digunakan pada Schema.org untuk data tersebut. | "identifier": "221401001" |
| 5 | "identifier": "221401001", | Properti terakhir dalam objek JSON tidak boleh diakhiri tanda koma. | "identifier": "221401001" |

## 4. Triplet dari JSON-LD Playground

Tuliskan satu baris N-Quads yang terbentuk:

```text
<https://usu.ac.id/mhs/251402145> <https://schema.org/name> "Naufal Awan Harahap"

## Identitas

| No. | Nama | NIM |
|---|---|---|
| 1 | Naufal Awan Harahap | 251402145 |
| 2 | Felix Desselol Tambunan | 251402033 |
| 3 | Cinta Pardame Sialoho | 251402090 |
| 4 | Chris Martin | 251402116 |

## Struktur Hasil

## 5. Hasil Validasi
Schema Markup Validator: profil_saya.jsonld berhasil diperiksa dan struktur data dikenali sebagai Person tanpa kesalahan sintaks.
Rich Results Test: seminar.html berhasil dikenali sebagai Event dan terdapat 1 item valid terdeteksi. Beberapa properti tambahan yang belum dicantumkan bersifat opsional.
JSON-LD Playground: profil_saya.jsonld berhasil diproses menjadi data terstruktur dan dapat menghasilkan bentuk RDF/N-Quads.

## 6. Refleksi**
Mengapa @context disebut jembatan menuju makna?
@context disebut jembatan menuju makna karena menghubungkan istilah yang digunakan dalam JSON-LD dengan kosakata yang memiliki arti tertentu, seperti Schema.org. Dengan demikian, mesin dapat memahami arti dari properti yang digunakan.
Apa perbedaan fungsi Schema Markup Validator dan Rich Results Test?
Schema Markup Validator digunakan untuk memeriksa apakah struktur dan properti data terstruktur sudah sesuai dengan kosakata Schema.org. Sedangkan Rich Results Test digunakan untuk memeriksa apakah data terstruktur pada halaman memenuhi persyaratan Google untuk menghasilkan fitur rich results pada hasil pencarian.
Mengapa isi JSON-LD harus sama dengan konten yang terlihat pada halaman?
Isi JSON-LD harus sesuai dengan konten yang terlihat agar data terstruktur benar-benar menggambarkan informasi pada halaman. Jika berbeda, data dapat menjadi tidak konsisten dan berpotensi memberikan informasi yang menyesatkan kepada mesin pencari.

## Bukti

![Schema Markup Validator](screenshots/profil-schema-validator.png)

![JSON-LD Playground](screenshots/profil-playground.png)

![Rich Results Test](screenshots/seminar-rich-results.png)


