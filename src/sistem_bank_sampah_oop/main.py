from datetime import datetime
from decimal import Decimal
from sistem_bank_sampah_oop.petugas import Petugas
from sistem_bank_sampah_oop.jenis_sampah import JenisSampah
from sistem_bank_sampah_oop.setoran_sampah import SetoranSampah
from sistem_bank_sampah_oop.status_setoran import StatusSetoran
from sistem_bank_sampah_oop.laporan_sampah import LaporanSampah


if __name__ == "__main__":
    petugas1 = Petugas(_id="P001", _nama="Budi Santoso", aktif=True)

    plastik = JenisSampah(id_jenis="J01", nama="Botol Plastik PET", kategori="Plastik", dapat_didaur_ulang=True)
    kertas = JenisSampah(id_jenis="J02", nama="Kardus Bekas", kategori="Kertas", dapat_didaur_ulang=True)

    setoran1 = SetoranSampah(
        id_setoran="S001",
        jenis_sampah=plastik,
        berat_kg=Decimal("2.5"),
        tanggal=datetime.now(),
        status=StatusSetoran.MENUNGGU,
        petugas=petugas1
    )
    
    setoran2 = SetoranSampah(
        id_setoran="S002",
        jenis_sampah=kertas,
        berat_kg=Decimal("5.0"),
        tanggal=datetime.now(),
        status=StatusSetoran.MENUNGGU,
        petugas=petugas1
    )

    setoran3 = SetoranSampah(
        id_setoran="S003",
        jenis_sampah=plastik,
        berat_kg=Decimal("1.2"),
        tanggal=datetime.now(),
        status=StatusSetoran.MENUNGGU,
        petugas=petugas1
    )

    setoran1.terima()
    setoran2.terima()
    setoran3.tolak("Sampah basah/kotor")

    laporan = LaporanSampah(daftar_setoran=[setoran1, setoran2, setoran3])

    print("\n" + laporan.buat_laporan())