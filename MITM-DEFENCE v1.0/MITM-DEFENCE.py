import os
import time
import datetime

print("* Güvenlik Taraması Başlatıdı")

def print_arp_table():
    current_time = datetime.datetime.now().time()
    arp_table = os.popen("arp -a").read()
    mac_count = {}
    for line in arp_table.split("\n"):
        if "dynamic" in line:
            ip = line.split()[0]
            mac = line.split()[1]
            if mac in mac_count:
                mac_count[mac] += 1
                if mac_count[mac] > 1:
                    print("Sistem Saldırı altında !")
                    print(" IP Adresi " + ip)
                    print(" Zaman ", current_time)
                    return
            else:
                mac_count[mac] = 1
    print("    - Sistem Güvende")

while True:
    print_arp_table()
    time.sleep(1)