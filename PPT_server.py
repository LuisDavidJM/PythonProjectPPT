from socket import socket 
from threading import Thread, Barrier
import time
import json
import sys

def client(conn, addr, contador):
    if contador > 2:
        contador -= 1
    print(f"[NEW] {addr} conectado cliente [{contador}]")
    conn.send("Bienvenido al servidor".encode("utf-8"))  
    dat = {}
    co = 1
    while True:       
        while contador == 1:
            if c == 1 and co == 1:
                conn.send("Esperando al otro jugador".encode("utf-8"))
                time.sleep(0.2)
            else:
                break
        if contador == 2 and co == 1:
            time.sleep(0.2)
            for i in range(10):
                conn.send("Listo para jugar 2".encode("utf-8")) 
                time.sleep(0.2)
        elif contador == 1 and co == 1:
            time.sleep(0.2)
            conn.send("Listo para jugar 1".encode("utf-8")) 
        co = 2
        
        dato = conn.recv(40).decode("utf-8")
        conn.send("Esperando respuesta del otro jugador".encode("utf-8")) 
        b.wait()          
        if contador == 1:
            with open("datos1.json", "w") as f:
                dat['dato1'] = dato
                json.dump(dat, f)
        if contador == 2:
            with open("datos2.json", "w") as f:
                dat['dato2'] = dato
                json.dump(dat, f)  

        with open("datos1.json") as f:
            dato1 = json.loads(f.read())  
        with open("datos2.json") as fi:
            dato2 = json.loads(fi.read()) 
        if (dato1['dato1'] == "Piedra" and dato2['dato2'] == "Papel") or (dato1['dato1'] == "Papel" and dato2['dato2'] == "Tijera") or (dato1['dato1'] == "Tijera" and dato2['dato2'] == "Piedra"): 
            envio = "Pierde1"
            time.sleep(0.2)
            conn.send(envio.encode("utf-8")) 
        elif (dato1['dato1'] == "Piedra" and dato2['dato2'] == "Tijera") or (dato1['dato1'] == "Papel" and dato2['dato2'] == "Piedra") or (dato1['dato1'] == "Tijera" and dato2['dato2'] == "Papel"): 
            envio = "Gana1"
            time.sleep(0.2)
            conn.send(envio.encode("utf-8")) 
        elif (dato1['dato1'] == "Piedra" and dato2['dato2'] == "Piedra") or (dato1['dato1'] == "Papel" and dato2['dato2'] == "Papel") or (dato1['dato1'] == "Tijera" and dato2['dato2'] == "Tijera"): 
            envio = "Empate"
            time.sleep(0.2)
            conn.send(envio.encode("utf-8"))
        else:
            envio = "El otro usuario se salio"
            if (dato1['dato1'] == "Salir1" or dato2['dato2'] == "Salir1"):
                if contador == 1:
                    print(f"El {contador} usuario salido ")
                    break
                elif contador == 2:
                    co = 1
                    time.sleep(0.2)
                    conn.send(envio.encode("utf-8"))
            elif (dato1['dato1'] == "Salir2" or dato2['dato2'] == "Salir2"):
                if contador == 2:
                    print(f"El {contador} usuario salido ")
                    break
                elif contador == 1:
                    co = 1
                    time.sleep(0.2)
                    conn.send(envio.encode("utf-8"))

    print(f"[DISSCONECT] {addr} desconectado [{contador}]")

if __name__ == '__main__': 
    s = socket()
    host = 'localhost'
    port = sys.argv[1]
    port = int(port)
    s.bind((host, port))
    s.listen()  
    b = Barrier(2)
    print("[START] El servidor esta iniciado")
    contador = 0
    while True:
        conn, addr = s.accept()
        contador += 1
        if contador == 1:
            c = 1
        if contador == 2:
            c = 2
        t1 = Thread(target=client, args=(conn, addr, contador))
        t1.start()


