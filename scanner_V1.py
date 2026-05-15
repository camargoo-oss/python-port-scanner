import socket
import datetime 

print("="*50)
print(" PYTHON PORT  SCANNER - V1")
print(f"   Fecha: {datetime.datetime.now()}")

target = input("Ingresa IP o dominio a escanear:  ")
print(f"\nEscaneando {target}...\n")

for port in range(1, 1025):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    if result == 0:
        print(f" [ABIERTO] Puerto {port}")
    s.close()

print("\nEscaneo completo.")