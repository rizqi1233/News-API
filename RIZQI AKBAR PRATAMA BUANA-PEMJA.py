import requests

API_KEY = '62d99c5f4126499790c14588724fcd6b'

# URL untuk endpoint yang ingin diakses
url = 'https://newsapi.org/v2/top-headlines'

parameters = {
    'country': 'id',  # Ubah kode negara jika Anda ingin berita dari negara lain
    'category': 'technology', #Kategori berita
    'language': 'id', #bahasa berita
    'sortBy': 'popularity', # Mengurutkan berdasarkan popularitas
    'apiKey': API_KEY
    
}

# Buat GET request
response = requests.get(url, params=parameters)

# Cek jika request berhasil (status code 200)
if response.status_code == 200:
   
    news_data = response.json()
    
    # DTampilkan beberapa informasi dari respons
    for article in news_data['articles']:
        print(f"Title: {article['title']}")
        print(f"Source: {article['source']['name']}")
        print(f"URL: {article['url']}")
        print("--------------------------------------------------")
else:
    print("Gagal untuk mendapatkan berita. Status code:", response.status_code)



