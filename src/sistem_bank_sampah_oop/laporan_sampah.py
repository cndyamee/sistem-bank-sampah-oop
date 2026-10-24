from decimal import Decimal
from typing import List, Dict

class LaporanSampah:
    def __init__(self, daftar_setoran: List = None):
        self._daftar_setoran: List = daftar_setoran if daftar_setoran is not None else []

    def hitung_total_berat(self) -> Decimal:
        """
        Menghitung total berat dari semua setoran sampah yang ada di dalam daftar setoran.
        """
        total = Decimal('0.0')
        for setoran in self._daftar_setoran:
            # Menggunakan method hitung_berat() atau atribut berat_kg dari SetoranSampah
            if hasattr(setoran, 'hitung_berat'):
                total += Decimal(str(setoran.hitung_berat()))
            elif hasattr(setoran, 'berat_kg'):
                total += Decimal(str(setoran.berat_kg))
        return total

    def hitung_berat_per_jenis(self) -> Dict[str, Decimal]:
        """
        Menghitung akumulasi berat sampah berdasarkan jenis/kategorinya.
        """
        hasil: Dict[str, Decimal] = {}
        for setoran in self._daftar_setoran:
            nama_jenis = "Tidaktahu"
            
            # Mengambil nama jenis dari relasi jenis_sampah
            if hasattr(setoran, 'jenis_sampah') and setoran.jenis_sampah:
                nama_jenis = getattr(setoran.jenis_sampah, 'nama', 'Tanpa Nama')
            
            berat = Decimal('0.0')
            if hasattr(setoran, 'hitung_berat'):
                berat = Decimal(str(setoran.hitung_berat()))
            elif hasattr(setoran, 'berat_kg'):
                berat = Decimal(str(setoran.berat_kg))

            if nama_jenis in hasil:
                hasil[nama_jenis] += berat
            else:
                hasil[nama_jenis] = berat

        return hasil

    def buat_laporan(self) -> str:
        """
        Menghasilkan ringkasan/laporan tertulis berbentuk string.
        """
        laporan = "=== LAPORAN SETORAN SAMPAH ===\n"
        laporan += f"Total Setoran: {len(self._daftar_setoran)} item\n"
        laporan += f"Total Berat  : {self.hitung_total_berat()} kg\n\n"
        laporan += "--- Rincian Per Jenis ---\n"
        
        rincian_jenis = self.hitung_berat_per_jenis()
        if not rincian_jenis:
            laporan += "Belum ada data setoran.\n"
        else:
            for jenis, berat in rincian_jenis.items():
                laporan += f"- {jenis}: {berat} kg\n"
                
        return laporan