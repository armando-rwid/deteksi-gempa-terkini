"""
aplikasi deteksi gempa terkini
"""


def ekstraksi_data():
    """
    Tanggal : 13 November 2021,
    Waktu : 20:42:51 WIB
    Magnitudo : 5.0
    Kedalaman : 118 km
    Lokasi : LU = 1.77 LU - BT = 127.35 BT
    Pusat Gempa : 53 km BaratLaut HALMAHERABARAT-MALUT
    Dampak : tidak berpotensi TSUNAMI
    """
    hasil = dict()
    hasil['tanggal'] = '13 November 2021'
    hasil['waktu'] = '20:24:51 WIB'
    hasil['magnitudo'] = '5.0 SR'
    hasil['kedalaman'] = '118 km'
    hasil['lokasi'] = {
        'LU': 1.48,
        'BT': 134.01
    }
    hasil['pusat'] = '53 km BaratLaut HALMAHERABARAT-MALUT'
    hasil['dampak'] = 'tidak berpotensi tsunami'

    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Lokasi LU : {result['lokasi']['LU']}, LS : {result['lokasi']['LU']}")
    print(f"Dampak : {result['dampak']}")


if __name__ == '__main__':
    print('Aplikasi Utama')
    result = ekstraksi_data()
    tampilkan_data(result)
