from datetime import datetime
from decimal import Decimal

from sistem_bank_sampah_oop.jenis_sampah import JenisSampah
from sistem_bank_sampah_oop.petugas import Petugas
from sistem_bank_sampah_oop.status_setoran import StatusSetoran


class SetoranSampah:
    def __init__(
        self,
        id_setoran: str,
        jenis_sampah: JenisSampah,
        berat_kg: Decimal,
        tanggal: datetime,
        petugas: Petugas,
        status: StatusSetoran = StatusSetoran.MENUNGGU,
    ):
        self._id_setoran = id_setoran
        self._jenis_sampah = jenis_sampah
        self._berat_kg = berat_kg
        self._tanggal = tanggal
        self._petugas = petugas
        self._status = status
        self._alasan_penolakan: str | None = None

    @property
    def berat_kg(self):
        return self._berat_kg

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status: StatusSetoran):
        self._status = status

    @property
    def alasan_penolakan(self):
        return self._alasan_penolakan

    @alasan_penolakan.setter
    def alasan_penolakan(self, alasan: str):
        self._alasan_penolakan = alasan

    def hitung_berat(self) -> Decimal:
        return self.berat_kg

    def terima(self) -> None:
        self._pastikan_menunggu()
        self.status = StatusSetoran.DITERIMA

    def tolak(self, alasan: str):
        self._pastikan_menunggu()
        self.alasan_penolakan = alasan
        self.status = StatusSetoran.DITOLAK

    def _pastikan_menunggu(self):
        if self.status is not StatusSetoran.MENUNGGU:
            raise ValueError("Hanya setoran berstatus MENUNGGU yang dapat diproses.")
