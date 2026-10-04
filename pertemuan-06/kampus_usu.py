
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, FOAF, XSD


# Membuat graph RDF
g = Graph()

# Namespace Kelompok 04
EX = Namespace(
    "https://naufal-awnharahap.github.io/web-semantik-Kelompok04/ontology/kampus#"
)

# Prefix
g.bind("ex", EX)
g.bind("foaf", FOAF)
g.bind("rdf", RDF)
g.bind("xsd", XSD)


# ============================================================
# DOSEN
# ============================================================

g.add((EX.CintaPardameSialoho, RDF.type, EX.Lecturer))
g.add((
    EX.CintaPardameSialoho,
    EX.hasName,
    Literal("Cinta Pardame Sialoho", lang="id")
))

g.add((EX.DosenRDF, RDF.type, EX.Lecturer))
g.add((
    EX.DosenRDF,
    EX.hasName,
    Literal("Dosen RDF", lang="id")
))

g.add((EX.DosenWebSemantik, RDF.type, EX.Lecturer))
g.add((
    EX.DosenWebSemantik,
    EX.hasName,
    Literal("Dosen Web Semantik", lang="id")
))


# ============================================================
# MATA KULIAH
# ============================================================

g.add((EX.WebSemantik, RDF.type, EX.Course))
g.add((
    EX.WebSemantik,
    FOAF.name,
    Literal("Web Semantik", lang="id")
))

g.add((EX.RDFDasar, RDF.type, EX.Course))
g.add((
    EX.RDFDasar,
    FOAF.name,
    Literal("RDF Dasar", lang="id")
))

g.add((EX.OntologiWeb, RDF.type, EX.Course))
g.add((
    EX.OntologiWeb,
    FOAF.name,
    Literal("Ontologi Web", lang="id")
))


# ============================================================
# MAHASISWA
# ============================================================

g.add((EX.NaufalAwan, RDF.type, EX.Student))
g.add((
    EX.NaufalAwan,
    EX.hasNIM,
    Literal("251402145", datatype=XSD.string)
))
g.add((
    EX.NaufalAwan,
    EX.hasName,
    Literal("Naufal Awan", lang="id")
))

g.add((EX.FelixDesseloTambunan, RDF.type, EX.Student))
g.add((
    EX.FelixDesseloTambunan,
    EX.hasNIM,
    Literal("251402033", datatype=XSD.string)
))
g.add((
    EX.FelixDesseloTambunan,
    EX.hasName,
    Literal("Felix Desselo Tambunan", lang="id")
))


# ============================================================
# DEPARTEMEN
# ============================================================

g.add((EX.TeknikInformatika, RDF.type, EX.Department))


# ============================================================
# RELASI DOSEN DENGAN MATA KULIAH
# ============================================================

g.add((
    EX.CintaPardameSialoho,
    EX.teachesCourse,
    EX.WebSemantik
))

g.add((
    EX.DosenRDF,
    EX.teachesCourse,
    EX.RDFDasar
))

g.add((
    EX.DosenWebSemantik,
    EX.teachesCourse,
    EX.OntologiWeb
))


# ============================================================
# RELASI MAHASISWA DENGAN MATA KULIAH
# ============================================================

g.add((
    EX.NaufalAwan,
    EX.takesCourse,
    EX.WebSemantik
))

g.add((
    EX.FelixDesseloTambunan,
    EX.takesCourse,
    EX.RDFDasar
))


# ============================================================
# RELASI PERSON DENGAN DEPARTEMEN
# ============================================================

g.add((
    EX.CintaPardameSialoho,
    EX.belongsToDepartment,
    EX.TeknikInformatika
))

g.add((
    EX.NaufalAwan,
    EX.belongsToDepartment,
    EX.TeknikInformatika
))

g.add((
    EX.FelixDesseloTambunan,
    EX.belongsToDepartment,
    EX.TeknikInformatika
))


# ============================================================
# SERIALISASI RDF
# ============================================================

g.serialize(
    "kampus_usu.ttl",
    format="turtle"
)

g.serialize(
    "kampus_usu.jsonld",
    format="json-ld",
    indent=2
)


# ============================================================
# INFORMASI GRAPH
# ============================================================

print("=== RDF KAMPUS KELOMPOK 04 ===")
print("Jumlah triple:", len(g))


# ============================================================
# OUTPUT TURTLE
# ============================================================

print("\nOutput Turtle:")
print("=" * 50)
print(g.serialize(format="turtle"))


# ============================================================
# QUERY DAFTAR DOSEN
# ============================================================

print("\nDaftar dosen:")
print("=" * 50)

for subject, predicate, obj in g.triples(
    (None, RDF.type, EX.Lecturer)
):
    print(subject)
