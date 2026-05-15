import socket
import datetime
import sys
import threading

print_lock = threading.Lock()

def scan_port(target, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "desconocido"
        with print_lock:
            print(f"  [ABIERTO] Puerto  {port} --> {service}")
    s.close()

if len(sys.argv) != 4:
    print("Uso: python scanner_V3.py <IP> <puerto_inicio> <puerto_fin")
    sys.exit()

target =  sys.argv[1]
port_start = int(sys.argv[2])
port_end = int(sys.argv[3])

print("="*50)
print(f"  PYTHON PORT SCANNER - v3 (Threading)")
print(f"  Target:   {target}")
print(f"  Puertos: {port_start} - {port_end}")
print(f"  Fecha: {datetime.datetime.now()}")
print("="*50)

threads =  []

for port in range (port_start,  port_end + 1):
    t = threading.Thread(target=scan_port, args=(target, port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nEscaneo completado.")
