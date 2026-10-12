import urllib.request

# Daftar URL playlist sumber Anda
urls = [
    "https://raw.githubusercontent.com/apistech/project/refs/heads/main/IndihomeTV.m3u",
    "https://pastebin.support.one/view/raw/53bd4fb6",
    "https://raw.githubusercontent.com/apistech/project/refs/heads/main/playlists/liveeventsfilter.m3u8"
]

combined_content = "#EXTM3U\n"

for url in urls:
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as response:
            content = response.read().decode('utf-8', errors='ignore')
            # Bersihkan baris #EXTM3U di awal sub-file agar tidak duplikat
            lines = content.splitlines()
            cleaned_lines = [line for line in lines if not line.strip().startswith('#EXTM3U')]
            combined_content += "\n".join(cleaned_lines) + "\n"
    except Exception as e:
        print(f"Gagal mengambil URL {url}: {e}")

# Simpan hasil gabungan ke file master.m3u
with open("master.m3u", "w", encoding="utf-8") as f:
    f.write(combined_content)

print("Playlist berhasil digabungkan!")
