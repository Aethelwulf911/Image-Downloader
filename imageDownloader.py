import requests

def download_files(url):
    local_filename = url.split('/')[-1]
    with requests.get(url,stream=True) as r:
        print("Download...")
        with open("C:/Users/Aethelwulf/Pictures/Aethelwulf.jpg",'wb') as f:
            print("Writing data to file")
            f.write(r.content)
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
        f.close()
        print("Download complete")
        print("File save as "+ local_filename)

download_files("https://www.pierre-giraud.com/wp-content/uploads/2019/05/html-img-display-block.png")