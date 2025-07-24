import requests
import hashlib
from config import HEADERS

def get_hash(url):
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()
        content = response.text.encode('utf-8')
        return hashlib.md5(content).hexdigest(), content
        # return hashlib.md5(response.text.encode('utf-8')).hexdigest()
    except requests.exceptions.RequestException as e:
        print(f"[Error] Request failed: {e}")
        return None
