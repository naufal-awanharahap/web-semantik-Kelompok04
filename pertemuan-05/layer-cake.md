# Semantic Web Layer Cake

## Pemetaan Layer

| Layer | Teknologi | Fungsi |
|---|---|---|
| 1 | URI dan Unicode | Memberikan identitas global dan representasi karakter |
| 2 | XML | Menyediakan sintaks untuk pertukaran data |
| 3 | RDF dan RDFS | Merepresentasikan data dalam bentuk graph dan menyediakan kosakata dasar |
| 4 | Ontology / OWL | Memberikan makna yang lebih kaya terhadap konsep, hubungan, dan aturan dalam suatu domain |
| 5 | SPARQL | Digunakan untuk melakukan query terhadap graph RDF |
| 6 | Rules, Proof, Trust | Mendukung aturan, pembuktian, dan kepercayaan terhadap informasi |

## Posisi Ontology

Ontology berada di atas RDF/RDFS karena ontology menggunakan representasi RDF/RDFS untuk memberikan semantik yang lebih kaya. Dengan OWL, dapat didefinisikan class, subclass, individual, property, domain, range, serta axiom seperti hubungan disjoint antar-class.

Ontology berada di bawah SPARQL karena SPARQL digunakan untuk mengambil dan meng-query informasi yang direpresentasikan dalam graph RDF dan ontology.

## Kesimpulan

Semantic Web Layer Cake menunjukkan bahwa teknologi Semantic Web dibangun secara bertingkat. RDF/RDFS digunakan untuk merepresentasikan informasi dan kosakata dasar, sedangkan ontology/OWL memberikan pemodelan konsep dan hubungan yang lebih kaya. SPARQL kemudian digunakan untuk mengakses informasi tersebut melalui query.
