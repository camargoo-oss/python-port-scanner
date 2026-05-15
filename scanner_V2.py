import socket 
import datetime
import sys 

#validar argumentos
if len(sys.argv) != 4:
    print("Uso: python scanner_V2.py <IP> <puerto_inicio> <puerto_fin>")
    print("Ejemplo: python scanner_V2.py 192.168.1.1 1 1024")
    sys.exit()

target = sys.argv[1]
port_start = int(sys.argv[2])
port_end = int(sys.argv[3])

print("="*50)
print(f"   PYTHON PORT SCANNER - v2")
print(f"   Target: {target}")
print(f"   Puertos: {port_start} - {port_end}")
print(f"   Fecha: {datetime.datetime.now()}")
print("="*50)

for port in range(port_start, port_end + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        try:
            service = socket.getservbyport(port)
        except:
            service = "desconocido"
        print(f" [ABIERTO] Puerto {port} --> {service}")
    s.close()

print("\nEscaneo completado.")
