# PROJECT 1B - TRAVERSAL TREE
# Contoh struktur organisasi kampus

class Tree:
    # Membuat satu node (satu jabatan)
    def __init__(self, nama, jabatan):
        self.nama = nama
        self.jabatan = jabatan
        self.children = []

    # Menambahkan bawahan ke sebuah jabatan
    def tambah_anak(self, anak):
        self.children.append(anak)

    # Bagian 8: Preorder Traversal
    # Urutan: tampilkan atasan, lalu semua bawahannya
    def preorder(self):
        print(self.nama, "-", self.jabatan)

        for anak in self.children:
            anak.preorder()

    # Bagian 9: Inorder Traversal
    # Untuk General Tree, contoh ini memakai aturan:
    # anak pertama -> node saat ini -> anak-anak sisanya
    def inorder(self):
        if len(self.children) > 0:
            self.children[0].inorder()

        print(self.nama, "-", self.jabatan)

        for anak in self.children[1:]:
            anak.inorder()

    # Bagian 10: Postorder Traversal
    # Urutan: tampilkan semua bawahan, lalu atasannya
    def postorder(self):
        for anak in self.children:
            anak.postorder()

        print(self.nama, "-", self.jabatan)


# MEMBUAT DATA STRUKTUR ORGANISASI

rektor = Tree("Dr. Ahmad", "Rektor")
dekan = Tree("Dr. Siti", "Dekan")
kaprodi = Tree("Pak Budi", "Ketua Prodi")
dosen = Tree("Bu Rina", "Dosen")
staf = Tree("Pak Andi", "Staf")
kepala_bag = Tree("Bu Lina", "Kepala Bagian")

# MENGHUBUNGKAN ATASAN DENGAN BAWAHANNYA

rektor.tambah_anak(dekan)
dekan.tambah_anak(kaprodi)
dekan.tambah_anak(kepala_bag)
kaprodi.tambah_anak(dosen)
kaprodi.tambah_anak(staf)


# MENJALANKAN TRAVERSAL

print("=== BAGIAN 8: PREORDER ===")
rektor.preorder()

print("\n=== BAGIAN 9: INORDER ===")
rektor.inorder()

print("\n=== BAGIAN 10: POSTORDER ===")
rektor.postorder()