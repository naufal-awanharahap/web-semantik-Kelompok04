# Pertemuan 11 - Tugas Mandiri: Dari Endpoint ke Graf Lokal

## Bagian A - LIMIT dan triple
- Triple dengan LIMIT 10: [30]
- Triple dengan LIMIT 30: [90]
- Baris SELECT LIMIT 10 / kota berbeda: [10] / [10]
- Mengapa tidak (atau mengapa tepat) 30 triple:
  Karena terdapat tiga pola triple dalam template CONSTRUCT. Setiap solution dapat menghasilkan maksimal tiga triple. Dengan LIMIT 10, batas maksimalnya adalah 30 triple. Namun, jumlah sebenarnya dapat lebih sedikit karena triple yang sama hanya disimpan satu kali dalam RDF Graph.

## Bagian B - DBpedia ke Turtle
- Output demo_c.py: [12] triple, film tanpa tanggal: [0]
- Sumber data: DBpedia / data contoh film.ttl
- Triple yang tetap tercetak untuk film tanpa tanggal:
  Triple schema:Movie, schema:name, dan schema:director tetap tercetak. Sementara itu, schema:datePublished tidak tercetak karena film tersebut tidak mempunyai tanggal rilis. Hal ini terjadi karena tanggal rilis menggunakan OPTIONAL sehingga tidak wajib ditemukan.
- Query lokal tanpa internet:
  Query lokal dapat dijalankan tanpa internet karena data sudah disimpan dalam file film_nolan.ttl. RDFLib membaca data dari file lokal sehingga tidak perlu menghubungi DBpedia lagi. Namun, apabila seluruh demo_c.py dijalankan ulang tanpa internet, pengambilan data dari endpoint DBpedia akan gagal.
- Mengapa dbo:Film memberi 0 pada film_nolan.ttl:
  Karena query CONSTRUCT mengubah tipe film menjadi schema:Movie, bukan dbo:Film. Oleh karena itu, pencarian menggunakan dbo:Film tidak menemukan triple yang sesuai dan menghasilkan 0.

## Bagian C - Materialisasi
- Output demo_d.py: [3]
- Mengapa Ada Rina bernilai 3:
  Karena proses materialisasi hanya dilakukan sebelum Rina ditambahkan. Setelah Rina dimasukkan sebagai ex:DosenTetap, aturan CONSTRUCT tidak dijalankan kembali. Akibatnya, tipe turunan foaf:Person untuk Rina belum terbentuk. Query hanya menemukan tiga individu yang sudah dimaterialisasi sebelumnya.
- Output materialisasi_ulang.py:
  Putaran 1: 4 triple baru | Person: 3
Rina masuk | Person: 3
Putaran 2 | Person: 4
Triple turunan disimpan terpisah: 6
- Tiga triple yang bukan baru: 
  Tiga triple tersebut merupakan triple hasil inferensi yang sudah terdapat dalam graf awal. Property path a/rdfs:subClassOf* juga menghasilkan hubungan dengan jalur nol langkah karena tanda * memungkinkan suatu kelas menjadi superclass dari dirinya sendiri. Oleh sebab itu, hasil CONSTRUCT dapat mencakup triple yang sudah ada.
- Kegunaan kampus_turunan.ttl dan langkah manual yang tersisa:
  File kampus_turunan.ttl digunakan untuk menyimpan triple hasil inferensi secara terpisah dari data asli. Jika hubungan subclass berubah, triple hasil inferensi dapat diperiksa dan dibandingkan dengan aturan terbaru. Langkah manual yang masih diperlukan adalah memperbarui aturan, menjalankan ulang materialisasi, memeriksa hasilnya, dan mengganti triple turunan yang sudah tidak sesuai.

## Bagian D - Diagnosis
| Query | Hasil mesin | Gejala | Penyebab (baris yang salah) | Hasil setelah diperbaiki |
|-------|-------------|--------|-----------------------------|--------------------------|
| rusak_a | 	0 triple | Graf kosong | Template menggunakan ?film, sedangkan WHERE menggunakan ?f. Variabel ?film tidak terikat | 3 triple judul film Nolan |
| rusak_b | Lebih dari 3 triple | Satu orang dapat mempunyai beberapa nilai nama | Property path mengambil nama dari beberapa predikat sekaligus. | 3 triple, satu nama per orang |
| rusak_c | Hanya menemukan tipe langsung |Superkelas tidak ditemukan | WHERE hanya mencari ?x a ex:Permukiman dan tidak menelusuri subclass | 3 triple: Medan, Surabaya, Tomok |

## Bagian E - Etika dan diskusi
| Aturan | a_kota_limit.rq | demo_c.py |
|--------|-----------------|-----------|
| 1 User-Agent | Tidak ditentukan di dalam query. Browser mengirim permintaan menggunakan kliennya. | Menggunakan UA berisi nama aplikasi dan email pengguna. |
| 2 LIMIT |  untuk membatasi solution Menggunakan LIMIT 10 | Tidak menggunakan LIMIT pada query pengambilan graf. |
| 3 Simpan, jangan ulangi | Hasil query dapat disimpan sebagai graf. | Mengambil data satu kali dan menyimpannya ke film_nolan.ttl untuk query lokal. |
| 4 Jangkar jalur | Menggunakan wd:Q515 sebagai IRI tetap pada ujung property path. | Tidak menggunakan property path pada query pengambilan data. |
- Versi yang melanggar aturan 4 (tidak dijalankan) dan alasannya:
  PREFIX wdt: <http://www.wikidata.org/prop/direct/>
  SELECT ?awal ?akhir
  WHERE {
    ?awal (wdt:P31|wdt:P279)* ?akhir .
  }
  Query tersebut melanggar aturan jangkar jalur karena menggunakan property path * tanpa IRI awal atau akhir yang spesifik. Akibatnya, endpoint harus menelusuri banyak kemungkinan hubungan kelas dan subkelas di seluruh graf Wikidata.

### Diskusi 1 - Taksonomi berubah
Materialisasi merupakan proses menyimpan hasil inferensi ke dalam graf RDF agar hasil tersebut dapat digunakan kembali tanpa harus menghitung seluruh aturan dari awal. Namun, hasil materialisasi dapat menjadi tidak sesuai ketika taksonomi mengalami perubahan.

Pada Demo D, file kampus_v4.ttl berisi graf yang sudah digabung dengan hasil materialisasi. Sementara itu, kampus_turunan.ttl menyimpan triple hasil inferensi secara terpisah. Misalnya, jika ex:Dosen tidak lagi menjadi subclass dari foaf:Person, maka triple yang menyatakan bahwa individu bertipe ex:Dosen juga merupakan foaf:Person tidak lagi sesuai dengan taksonomi terbaru.

Untuk menemukannya, saya akan membandingkan aturan subclass terbaru dengan triple hasil inferensi yang tersimpan. Triple yang tidak lagi didukung oleh aturan harus dihapus atau dihitung ulang. File kampus_turunan.ttl lebih mudah diperiksa karena hanya berisi hasil inferensi. Sebaliknya, pada kampus_v4.ttl, data asli dan hasil inferensi sudah digabung sehingga proses pemeriksaan lebih sulit. Oleh karena itu, materialisasi harus dijalankan kembali ketika taksonomi berubah agar data tetap konsisten.

### Diskusi 2 - SELECT atau CONSTRUCT
Untuk dashboard populasi kota, saya memilih SELECT karena hasilnya dapat ditampilkan dalam bentuk tabel yang berisi nama kota dan jumlah penduduk. Hasil SELECT juga dapat digunakan untuk membuat grafik atau melakukan pengolahan data lebih lanjut. Berdasarkan Bagian A, LIMIT membatasi jumlah solution, bukan jumlah triple. Satu solution dapat menghasilkan beberapa triple, tetapi triple yang sama hanya dihitung satu kali dalam RDF Graph.

Untuk menggabungkan data kota dari tiga sumber berbeda, saya memilih CONSTRUCT. CONSTRUCT dapat membentuk graf RDF baru dengan struktur dan kosakata yang seragam sehingga data dari berbagai sumber lebih mudah digabungkan.

Pada Bagian D, rusak_b.rq menunjukkan bahwa satu orang dapat mempunyai beberapa nilai nama melalui predikat foaf:name, rdfs:label, dan schema:name. Perbedaan tag bahasa juga dapat menyebabkan nilai yang terlihat sama dianggap berbeda oleh RDF. Oleh karena itu, proses penggabungan data harus menentukan predikat dan bahasa yang digunakan. Kesimpulannya, SELECT lebih sesuai untuk mengambil data berbentuk tabel, sedangkan CONSTRUCT lebih sesuai untuk membangun graf RDF terpadu dari beberapa sumber.

### Cek diri
| Pernyataan | Bukti dari tugas ini |
|------------|----------------------|
| 1.CONSTRUCT mencetak template sekali per solution dan menggabungkan triple kembar | Bagian A: terdapat tiga pola template. LIMIT 10 memiliki batas atas 30 triple, tetapi triple kembar hanya dihitung satu kali.
| 2. Triple dengan variabel tak terikat tidak dicetak, tanpa error | Bagian D: rusak_a.rq, variabel ?film tidak terikat karena WHERE menggunakan ?f. |
| 3. UNION, jalur \|, dan VALUES menyatukan predikat berbeda | Bagian D: rusak_b.rq menggunakan VALUES untuk memilih tiga orang dan property path untuk mengambil nama dari beberapa predikat |
| 4. Jalur + dan * menelusuri hierarki tanpa menyebut perantara | Bagian C dan D: property path a/rdfs:subClassOf* menelusuri hubungan subclass |
| 5. Materialisasi menyimpan kesimpulan, tetapi harus dihitung ulang. | Bagian C: setelah Rina ditambahkan, materialisasi ulang mengubah jumlah Person dari 3 menjadi 4 |
