import socket

HOST = "0.0.0.0"  # Сервер слушает все подключения
PORT = 9090       # Порт сервера

def receive_image():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)
        print(f"[Ожидание подключения] {HOST}:{PORT}")

        conn, addr = server_socket.accept()
        with conn:
            print(f"[Подключено] {addr}")
            data_buffer = b""
            receiving = False

            while True:
                data = conn.recv(4096)
                if not data:
                    break

                if not receiving and b"START_IMAGE" in data:
                    print("[Старт передачи изображения]")
                    receiving = True
                    data = data.split(b"START_IMAGE")[1]  # отбросить всё до START_IMAGE

                if receiving:
                    if b"END_IMAGE" in data:
                        parts = data.split(b"END_IMAGE")
                        data_buffer += parts[0]
                        print("[Завершение передачи изображения]")
                        break
                    else:
                        data_buffer += data

            if data_buffer:
                with open("photo.jpg", "wb") as f:
                    f.write(data_buffer)
                print("[Сохранено] Изображение в 'photo.jpg'")
            else:
                print("[Ошибка] Буфер данных пуст")

while True:
    try:
        receive_image()
    except Exception as e:
        print(f"[Ошибка сервера] {e}")

