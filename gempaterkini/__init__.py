def ekstraksi_data():
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

