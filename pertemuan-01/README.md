# KELOMPOK 4 – WEB SEMANTIK

| No | Nama | NIM |
|---|---|---|
| 1 | Naufal Awan Harahap | 251402145 |
| 2 | Felix Desselol Tambunan | 251402033 |
| 3 | Cinta Pardame Sihaloho | 251402090 |
| 4 | Chris Martin | 251402116 |

# Pertemuan 1 - Pengenalan Web Semantik

## 1. Eksplorasi Wikidata

- Nama entitas: Universitas Sumatera Utara
- Identifier Wikidata: Q4200341
- Deskripsi: Universitas di Indonesia
- Negara: Indonesia
- Lokasi: Medan, Sumatera Utara
- Tahun berdiri: 1952
- Website: https://www.usu.ac.id/
- Informasi lain: Memiliki singkatan USU

## 2. Entitas, Atribut, dan Relasi

| Informasi | Kategori | Alasan |
|---|---|---|
| Universitas Sumatera Utara | Entitas | Merupakan objek utama yang memiliki identitas |
| Medan | Entitas | Merupakan lokasi yang memiliki identitas |
| Indonesia | Entitas | Merupakan negara yang memiliki identitas |
| Tahun berdiri 1952 | Atribut | Menjelaskan tahun berdirinya universitas |
| Website resmi USU | Atribut | Menjelaskan alamat situs resmi universitas |
| Universitas Sumatera Utara → berlokasi di → Medan | Relasi | Menunjukkan hubungan universitas dengan lokasi |
| Universitas Sumatera Utara → berada di negara → Indonesia | Relasi | Menunjukkan hubungan universitas dengan negara |

## 3. Eksplorasi Schema.org

| Property | Fungsi | Contoh Nilai |
|---|---|---|
| `name` | Menyatakan nama universitas | Universitas Sumatera Utara |
| `address` | Menyatakan alamat universitas | Jl. Dr. T. Mansur No. 9, Padang Bulan, Medan, Sumatera Utara, Indonesia |
| `foundingDate` | Menyatakan tanggal atau tahun berdirinya universitas | 1952-07-04 |
| `url` | Menyatakan alamat website universitas | https://www.usu.ac.id/ |
| `logo` | Menyatakan logo universitas | https://upload.wikimedia.org/wikipedia/commons/7/7a/University_of_north_sumatera_logo.jpg |
| `email` | Menyatakan email universitas | info@usu.ac.id |
| `telephone` | Menyatakan nomor telepon universitas | 0821-6888-9060 |
| `alternateName` | Menyatakan nama atau singkatan lain universitas | USU |
| `description` | Menyatakan deskripsi singkat mengenai universitas | Universitas Sumatera Utara merupakan perguruan tinggi negeri di Medan, Sumatera Utara |
| `addressLocality` | Menyatakan kota tempat universitas berada | Medan |
| `addressRegion` | Menyatakan provinsi tempat universitas berada | Sumatera Utara |
| `postalCode` | Menyatakan kode pos alamat universitas | 20155 |
| `addressCountry` | Menyatakan negara tempat universitas berada | Indonesia |
| `event` | Menyatakan acara yang berkaitan dengan universitas | PKKMB USU 2026 |
| `department` | Menyatakan departemen atau unit akademik universitas | Departemen Teknologi Informasi |

## 4. Pertanyaan Evaluasi

### 1. Apa perbedaan utama antara web tradisional dan Web Semantik?
Jawaban: Web tradisional menyajikan informasi terutama agar dapat dibaca manusia, sedangkan Web Semantik memberikan struktur dan makna pada data sehingga dapat dipahami dan diproses oleh mesin.

### 2. Mengapa suatu entitas membutuhkan identifier unik?
Jawaban: Identifier unik digunakan untuk membedakan suatu entitas dari entitas lainnya secara jelas dan menghindari kesalahan dalam mengidentifikasi data.

### 3. Jelaskan perbedaan subject, predicate, dan object menggunakan satu contoh.
Jawaban: Subject adalah entitas yang dibicarakan, predicate adalah hubungan atau sifat yang menghubungkan, dan object adalah nilai atau entitas tujuan. Contoh: Universitas Sumatera Utara → berlokasi di → Medan. Universitas Sumatera Utara adalah subject, berlokasi di adalah predicate, dan Medan adalah object.

### 4. Apa keuntungan merepresentasikan informasi sebagai hubungan antarentitas dibandingkan hanya menyimpannya sebagai teks biasa?
Jawaban: Hubungan antarentitas membuat informasi lebih terstruktur sehingga keterkaitan antardata dapat dikenali, ditelusuri, dan diproses oleh komputer dengan lebih mudah.

### 5. Menurut Anda, bagaimana Knowledge Graph dapat membantu sistem pencarian atau AI dalam memahami informasi?
Jawaban: Knowledge Graph membantu sistem pencarian dan AI memahami hubungan serta konteks antarentitas sehingga informasi yang diberikan dapat menjadi lebih relevan dan terstruktur.

## 5. Bagaimana Knowledge Graph membantu AI?
Knowledge Graph membantu sistem pencarian dan AI memahami informasi dengan menghubungkan berbagai entitas beserta hubungan di antaranya secara terstruktur. Dengan struktur tersebut, AI dapat mengenali konteks dan keterkaitan suatu informasi sehingga dapat menghasilkan pencarian, rekomendasi, atau jawaban yang lebih relevan. Contohnya, AI dapat memahami bahwa Universitas Sumatera Utara berlokasi di Medan, Medan berada di Sumatera Utara, dan Sumatera Utara berada di Indonesia, karena hubungan antarentitas tersebut direpresentasikan secara jelas dalam Knowledge Graph.
