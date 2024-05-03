import os
import time
import datetime
import http.client

conn = http.client.HTTPConnection("45.84.188.101")

message = ''' ne ariyorsun burada :/ '''

headers = { "Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain" }

print("* Güvenlik Taraması Başlatıdı")

def print_arp_table(conn,message,headers):
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
                    conn.request("POST", "", message.encode('utf-8'), headers)
                    print("Sistem Saldırı altında !")
                    print(" IP Adresi " + ip)
                    print(" Zaman ", current_time)
                    conn.close()
                    return
            else:
                mac_count[mac] = 1
    print("    - Sistem Güvende")

while True:
    print_arp_table(conn,message,headers)
    time.sleep(1)