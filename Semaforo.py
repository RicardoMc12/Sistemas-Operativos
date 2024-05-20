import threading
import time

semaphore = threading.Semaphore(2)

def tarea(id):
    print(f"Tarea {id} intentando acceder el recurso")
    with semaphore:
     print(f"Tarea {id} ha adquirido el semaforo")
     time.sleep(2)
     print(f"Tarea {id} ha liberado el semaforo")

threads = []
for i in range(5):
    thread = threading.Thread(target=tarea, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()