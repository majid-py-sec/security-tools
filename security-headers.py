import requests

url = input("آدرس سایت رو وارد کن (مثل google.com): ")

if not url.startswith("http"):
    url = "https://" + url

response = requests.get(url)
headers = response.headers

print("\n" + "="*50)
print(f"🔍 بررسی امنیتی: {url}")
print("="*50)

server = headers.get("Server", "مخفی")
print(f"🖥️  Server: {server}")

content_type = headers.get("Content-Type", "نامشخص")
print(f"📄 Content-Type: {content_type}")

print("="*50)
