import requests
from bs4 import BeautifulSoup


def ekstraksi_data():

    try:
        content = requests.get('https://bmkg.go.id')
    except Exception:
        return None

    if content.status_code == 200:
        soup = BeautifulSoup(content.text, 'html.parser')
        hasil = soup.find('span', {'class': 'waktu'})
        hasil = hasil.text.split(',')
        tanggal = hasil[1]
        waktu = hasil[0]
        magnitudo = soup.find('span', {'class': 'ic magnitude'})


        hasil = dict()
        hasil['tanggal'] = tanggal
        hasil['waktu'] = waktu
        hasil['magnitudo'] = magnitudo
        hasil['kedalaman'] = '118 km'
        hasil['lokasi'] = {
            'LU': 1.48,
            'BT': 134.01
        }
        hasil['pusat'] = '53 km BaratLaut HALMAHERABARAT-MALUT'
        hasil['dampak'] = 'tidak berpotensi tsunami'

        return hasil
    else:
        return None


def tampilkan_data(result):
    if result is None:
        print('Tidak bisa menampilkan data terkini')
        return
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal : {result['tanggal']}")
    print(f"Waktu : {result['waktu']}")
    print(f"Magnitudo : {result['magnitudo']}")
    print(f"Kedalaman : {result['kedalaman']}")
    print(f"Lokasi LU : {result['lokasi']['LU']}, LS : {result['lokasi']['LU']}")
    print(f"Dampak : {result['dampak']}")

