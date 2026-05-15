import nmap
import sys
import datetime

if len(sys.argv) != 4:
    print("uso: python scanner_V4.py <IP> <puerto_inicio> <puerto_fin>")
    sys.exit()

target = sys.argv[1]
port_start = sys.argv[2]
port_end = sys.argv[3]
ports = f"{port_start} - {port_end}"

print("="*50)
print(f" PYTHON PORT SCANNER - v4 (Nmap)")
print(f" Target: {target}")
print(f" Puertos: {port_start} - {port_end}")
print(f" Fecha: {datetime.datetime.now()}")
print("="*50 + "\n")

scanner = nmap.PortScanner()
scanner.scan(target, ports, arguments="-sT -sV --open")

hosts = scanner.all_hosts()

if not hosts:
    print("No se encontraron resultados. Intenta con la IP directamente.")
    print("Obteniendo IP de scanme.nmap.org...")
    import socket
    ip = socket.gethostbyname(target)
    print(f"IP: {ip}")
    scanner.scan(ip, ports, arguments="-sT -sV --open")
    hosts = scanner.all_hosts()

if not hosts:
    print("Sin resultados. Prueba ejecutar VS Code como Administrador.")
else:
    host = hosts[0]
    for port in scanner[host]["tcp"]:
        state = scanner[host]["tcp"][port]["state"]
        service = scanner[host]["tcp"][port]["name"]
        version = scanner[host]["tcp"][port]["version"]
        product = scanner[host]["tcp"][port]["product"]
        if state == "open":
            print(f"  [ABIERTO] Puerto {port} --> {service} | {product} {version}")

print("\nEscaneo completado.")