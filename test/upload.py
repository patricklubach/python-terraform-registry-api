import requests

url_latest = 'http://127.0.0.1:8000/v1/modules/patricklubach/foo/google/novcs'
url_version = 'http://127.0.0.1:8000/v1/modules/patricklubach/foo/google/0.0.1/novcs'

with open('archive.tar.gz', 'rb') as f:
    file = {'file': f.read()}

resp = requests.put(url=url_latest, files=file)
print(resp.json())

resp = requests.put(url=url_version, files=file)
print(resp.json())