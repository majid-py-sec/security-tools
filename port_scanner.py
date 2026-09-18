import socket

target = input("آدرس هدف رو وارد کن (مثل google.com): ")
ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 3306, 3389, 8080]

print(f"\n🔎 در حال اسکن {target}...\n")

for port in ports:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"✅ پورت {port} باز است")
        sock.close()
    except:
        pass

print("\n✅ اسکن تمام شد!")
