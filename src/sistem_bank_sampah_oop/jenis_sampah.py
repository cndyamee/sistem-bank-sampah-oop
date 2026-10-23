class JenisSampah:
    def __init__(
        self,
        id_jenis: str,
        nama: str,
        kategori: str,
        dapat_didaur_ulang: bool,
    ):
        self._id_jenis = id_jenis
        self._nama = nama
        self._kategori = kategori
        self._dapat_didaur_ulang = dapat_didaur_ulang

    @property
    def id_jenis(self):
        return self._id_jenis

    @property
    def nama(self):
        return self._nama

    @property
    def kategori(self):
        return self._kategori

    @kategori.setter
    def kategori(self, kategori: str):
        self._kategori = kategori

    @property
    def dapat_didaur_ulang(self):
        return self._dapat_didaur_ulang

    def ubah_kategori(self, kategori: str):
        self.kategori = kategori

    def info_sampah(self):
        status_daur_ulang = "Ya" if self.dapat_didaur_ulang else "Tidak"
        return (
            f"ID: {self.id_jenis}\n"
            f"Nama: {self.nama}\n"
            f"Kategori: {self.kategori}\n"
            f"Dapat didaur ulang: {status_daur_ulang}"
        )
