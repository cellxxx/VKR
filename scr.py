# # # # import serial
# # # # def receive_image(port, baudrate, output_file):
# # # #     with serial.Serial(port, baudrate, timeout=1) as ser, open(output_file, 'wb') as file:
# # # #         print("Ожидание начала передачи изображения...")
# # # #         receiving_image = False

# # # #         while True:
# # # #             # Считываем строку, если мы еще не начали получать данные изображения
# # # #             if not receiving_image:
# # # #                 line = ser.readline().decode('utf-8', errors='ignore').strip()
# # # #                 if line == "START_IMAGE":
# # # #                     print("Начата передача изображения...")
# # # #                     receiving_image = True
# # # #             else:
# # # #                 # Читаем данные блоками
# # # #                 data = ser.read(2048)
# # # #                 if b'END_IMAGE' in data:
# # # #                     # Если нашли маркер конца изображения, сохраняем оставшиеся данные до маркера
# # # #                     end_index = data.find(b'END_IMAGE')
# # # #                     file.write(data[:end_index])  # Сохраняем данные до маркера
# # # #                     print("Передача изображения завершена.")
# # # #                     break
# # # #                 file.write(data)  # Сохраняем данные в файл
# # # #         print(f"Изображение сохранено в '{output_file}'")

# # # # # Параметры подключения
# # # # PORT = 'COM5'
# # # # BAUDRATE = 115200  # Скорость передачи
# # # # OUTPUT_FILE = 'photo.jpg'  # Имя выходного файла

# # # # receive_image(PORT, BAUDRATE, OUTPUT_FILE)
# # # import serial  # Импортируем библиотеку для работы с последовательными портами

# # # def receive_image(port, baudrate, output_file):
# # #     # Открываем последовательный порт и выходной файл для записи в бинарном режиме
# # #     with serial.Serial(port, baudrate, timeout=1) as ser, open(output_file, 'wb') as file:
# # #         print("Ожидание начала передачи изображения...")  # Информируем пользователя о начале ожидания
# # #         receiving_image = False  # Флаг, указывающий, началась ли передача изображения

# # #         while True:  # Бесконечный цикл для постоянного чтения данных
# # #             # Если мы еще не начали получать данные изображения
# # #             if not receiving_image:
# # #                 # Считываем строку из последовательного порта
# # #                 line = ser.readline().decode('utf-8', errors='ignore').strip()
                
# # #                 # Проверяем, соответствует ли считанная строка маркеру начала изображения
# # #                 if line == "START_IMAGE":
# # #                     print("Начата передача изображения...")  # Сообщаем, что передача началась
# # #                     receiving_image = True  # Устанавливаем флаг, что мы теперь находимся в режиме получения изображения
# # #             else:
# # #                 # Если передача изображения началась, читаем данные блоками по 2048 байт
# # #                 data = ser.read(2048)
                
# # #                 # Проверяем, содержит ли считанные данные маркер конца изображения
# # #                 if b'END_IMAGE' in data:
# # #                     # Если нашли маркер конца изображения, сохраняем оставшиеся данные до маркера
# # #                     end_index = data.find(b'END_IMAGE')  # Находим индекс конца изображения
# # #                     file.write(data[:end_index])  # Записываем в файл данные до маркера конца изображения
# # #                     print("Передача изображения завершена.")  # Сообщаем о завершении передачи
# # #                     break  # Выходим из цикла, так как передача закончена
                
# # #                 # Если маркер конца не найден, продолжаем записывать данные в файл
# # #                 file.write(data)  # Сохраняем считанные данные в выходной файл
        
# # #         # Информируем о том, что изображение сохранено
# # #         print(f"Изображение сохранено в '{output_file}'")

# # # # Параметры подключения
# # # PORT = 'COM5'  # Указываем имя последовательного порта (например, COM5 на Windows)
# # # BAUDRATE = 115200  # Указываем скорость передачи данных
# # # OUTPUT_FILE = 'photo.jpg'  # Имя выходного файла, в который будет сохранено изображение

# # # # Вызываем функцию для получения изображения
# # # receive_image(PORT, BAUDRATE, OUTPUT_FILE)

# # # import torch
# # # from torchvision.models import resnet18
# # # from torchvision import transforms
# # # from PIL import Image
# # # from datetime import datetime

# # # # Загрузка модели ResNet18
# # # model = resnet18(pretrained=False)  # Создаём модель
# # # num_classes = 10  # Количество классов в вашей задаче
# # # model.fc = torch.nn.Linear(model.fc.in_features, num_classes)  # Настраиваем последний слой

# # # model_path = 'resnet18_biology.pth'  # Укажите путь к вашей сохранённой модели
# # # model.load_state_dict(torch.load(model_path))  # Загружаем веса
# # # model.eval()

# # # # Устройство выполнения
# # # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# # # model = model.to(device)

# # # # Преобразования для изображения
# # # transform = transforms.Compose([
# # #     transforms.Resize((224, 224)),
# # #     transforms.ToTensor(),
# # #     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
# # # ])

# # # # Файл для журнала
# # # log_file = "classification_log.txt"

# # # # Функция классификации
# # # import torch
# # # from torchvision.models import resnet18
# # # from torchvision import transforms
# # # from PIL import Image
# # # from datetime import datetime
# # # import os

# # # # Загрузка модели ResNet18
# # # model = resnet18(pretrained=False)  # Создаём модель
# # # num_classes = 10  # Количество классов в вашей задаче
# # # model.fc = torch.nn.Linear(model.fc.in_features, num_classes)  # Настраиваем последний слой

# # # model_path = 'resnet18_biology.pth'  # Укажите путь к вашей сохранённой модели
# # # model.load_state_dict(torch.load(model_path))  # Загружаем веса
# # # model.eval()

# # # # Устройство выполнения
# # # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# # # model = model.to(device)

# # # # Преобразования для изображения
# # # transform = transforms.Compose([
# # #     transforms.Resize((224, 224)),
# # #     transforms.ToTensor(),
# # #     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
# # # ])

# # # # Папка для журнала с изображениями
# # # log_dir = "classification_log"
# # # os.makedirs(log_dir, exist_ok=True)

# # # # Функция классификации
# # # def classify_image(image_path):
# # #     try:
# # #         # Открываем изображение
# # #         image = Image.open(image_path).convert('RGB')

# # #         # Преобразуем изображение
# # #         input_tensor = transform(image).unsqueeze(0).to(device)

# # #         # Классификация
# # #         with torch.no_grad():
# # #             outputs = model(input_tensor)
# # #             _, predicted = torch.max(outputs, 1)
            
# # #         class_names = ["Собака", "Лошадь", "Слон", "Бабочка", "Курица", "Кошка", "Корова", "Овца", "Паук", "Белка"]
# # #         class_name = class_names[predicted.item()]

# # #         # Метка времени
# # #         timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# # #         # Сохраняем изображение в журнал
# # #         saved_image_path = os.path.join(log_dir, f"{timestamp}_{class_name}.jpg")
# # #         image.save(saved_image_path)

# # #         # Сохраняем запись в журнал
# # #         with open(os.path.join(log_dir, "log.txt"), "a") as log:
# # #             log.write(f"{timestamp}, {class_name}, {saved_image_path}\n")

# # #         print(f"Изображение сохранено: {saved_image_path}, Класс: {class_name}")
# # #     except Exception as e:
# # #         print(f"Ошибка при обработке изображения: {e}")

# # # # Классифицируем изображение photo.jpg
# # # classify_image("photo.jpg")

# # import serial  # Импортируем библиотеку для работы с последовательными портами
# # import torch
# # from torchvision.models import resnet18
# # from torchvision import transforms
# # from PIL import Image
# # from datetime import datetime
# # import os

# # # Загрузка модели ResNet18
# # model = resnet18(pretrained=False)  # Создаём модель
# # num_classes = 10  # Количество классов в вашей задаче
# # model.fc = torch.nn.Linear(model.fc.in_features, num_classes)  # Настраиваем последний слой

# # model_path = 'resnet18_biology.pth'  # Укажите путь к вашей сохранённой модели
# # model.load_state_dict(torch.load(model_path))  # Загружаем веса
# # model.eval()

# # # Устройство выполнения
# # device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# # model = model.to(device)

# # # Преобразования для изображения
# # transform = transforms.Compose([
# #     transforms.Resize((224, 224)),
# #     transforms.ToTensor(),
# #     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
# # ])

# # # Папка для журнала с изображениями
# # log_dir = "classification_log"
# # os.makedirs(log_dir, exist_ok=True)

# # def receive_image(port, baudrate, output_file):
# #     # Открываем последовательный порт и выходной файл для записи в бинарном режиме
# #     with serial.Serial(port, baudrate, timeout=1) as ser, open(output_file, 'wb') as file:
# #         print("Ожидание начала передачи изображения...")  # Информируем пользователя о начале ожидания
# #         receiving_image = False  # Флаг, указывающий, началась ли передача изображения

# #         while True:  # Бесконечный цикл для постоянного чтения данных
# #             # Если мы еще не начали получать данные изображения
# #             if not receiving_image:
# #                 # Считываем строку из последовательного порта
# #                 line = ser.readline().decode('utf-8', errors='ignore').strip()
                
# #                 # Проверяем, соответствует ли считанная строка маркеру начала изображения
# #                 if line == "START_IMAGE":
# #                     print("Начата передача изображения...")  # Сообщаем, что передача началась
# #                     receiving_image = True  # Устанавливаем флаг, что мы теперь находимся в режиме получения изображения
# #             else:
# #                 # Если передача изображения началась, читаем данные блоками по 2048 байт
# #                 data = ser.read(2048)
                
# #                 # Проверяем, содержит ли считанные данные маркер конца изображения
# #                 if b'END_IMAGE' in data:
# #                     # Если нашли маркер конца изображения, сохраняем оставшиеся данные до маркера
# #                     end_index = data.find(b'END_IMAGE')  # Находим индекс конца изображения
# #                     file.write(data[:end_index])  # Записываем в файл данные до маркера конца изображения
# #                     print("Передача изображения завершена.")  # Сообщаем о завершении передачи
# #                     break  # Выходим из цикла, так как передача закончена
                
# #                 # Если маркер конца не найден, продолжаем записывать данные в файл
# #                 file.write(data)  # Сохраняем считанные данные в выходной файл
        
# #         # Информируем о том, что изображение сохранено
# #         print(f"Изображение сохранено в '{output_file}'")

# # def classify_image(image_path):
# #     try:
# #         # Открываем изображение
# #         image = Image.open(image_path).convert('RGB')

# #         # Преобразуем изображение
# #         input_tensor = transform(image).unsqueeze(0).to(device)

# #         # Классификация
# #         with torch.no_grad():
# #             outputs = model(input_tensor)
# #             _, predicted = torch.max(outputs, 1)
            
# #         class_names = ["Собака", "Лошадь", "Слон", "Бабочка", "Курица", "Кошка", "Корова", "Овца", "Паук", "Белка"]
# #         class_name = class_names[predicted.item()]

# #         # Метка времени
# #         timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# #         # Сохраняем изображение в журнал
# #         saved_image_path = os.path.join(log_dir, f"{timestamp}_{class_name}.jpg")
# #         image.save(saved_image_path)

# #         # Сохраняем запись в журнал
# #         with open(os.path.join(log_dir, "log.txt"), "a") as log:
# #             log.write(f"{timestamp}, {class_name}, {saved_image_path}\n")

# #         print(f"Изображение сохранено: {saved_image_path}, Класс: {class_name}")
# #     except Exception as e:
# #         print(f"Ошибка при обработке изображения: {e}")

# # # Параметры подключения
# # PORT = 'COM5'  # Укажите ваш порт
# # BAUDRATE = 115200  # Укажите скорость передачи
# # OUTPUT_FILE = 'photo.jpg'  # Имя файла для сохранения изображения

# # # Бесконечный цикл
# # while True:
# #     # Получаем изображение
# #     receive_image(PORT, BAUDRATE, OUTPUT_FILE)
# #     # Классифицируем изображение
# #     classify_image(OUTPUT_FILE)

# #     # Спрашиваем пользователя, хочет ли он завершить
# #     print("Нажмите Enter для продолжения или введите любой текст, чтобы завершить.")
# #     user_input = input().strip()
# #     if user_input:
# #         print("Завершение программы.")
# #         break
# import serial  # Импортируем библиотеку для работы с последовательными портами
# import torch
# from torchvision.models import resnet18
# from torchvision import transforms
# from PIL import Image
# from datetime import datetime
# import os
# import time

# # Загрузка модели ResNet18
# model = resnet18(pretrained=False)  # Создаём модель
# num_classes = 10  # Количество классов в вашей задаче
# model.fc = torch.nn.Linear(model.fc.in_features, num_classes)  # Настраиваем последний слой

# model_path = 'resnet18_biology.pth'  # Укажите путь к вашей сохранённой модели
# model.load_state_dict(torch.load(model_path))  # Загружаем веса
# model.eval()

# # Устройство выполнения
# device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
# model = model.to(device)

# # Преобразования для изображения
# transform = transforms.Compose([
#     transforms.Resize((224, 224)),
#     transforms.ToTensor(),
#     transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
# ])

# # Папка для журнала с изображениями
# log_dir = "classification_log"
# os.makedirs(log_dir, exist_ok=True)

# import serial  # Импортируем библиотеку для работы с последовательными портами

# def receive_image(port, baudrate, output_file):
#     # Открываем последовательный порт
#     with serial.Serial(port, baudrate, timeout=1) as ser:
#         print("Ожидание начала передачи изображения...")  # Информируем пользователя о начале ожидания
#         receiving_image = False  # Флаг, указывающий, началась ли передача изображения

#         while True:  # Бесконечный цикл для постоянного чтения данных
#             # Если мы еще не начали получать данные изображения
#             if not receiving_image:
#                 # Считываем строку из последовательного порта
#                 line = ser.readline().decode('utf-8', errors='ignore').strip()
                
#                 # Проверяем, соответствует ли считанная строка маркеру начала изображения
#                 if line == "START_IMAGE":
#                     print("Начата передача изображения...")  # Сообщаем, что передача началась
#                     receiving_image = True  # Устанавливаем флаг, что мы теперь находимся в режиме получения изображения

#                     # Очищаем файл, открыв его в режиме записи
#                     with open(output_file, 'wb') as file:
#                         pass  # Просто открываем и закрываем файл для очистки

#             else:
#                 # Если передача изображения началась, открываем файл для записи в бинарном режиме
#                 with open(output_file, 'ab') as file:
#                     # Читаем данные блоками по 2048 байт
#                     data = ser.read(2048)
                    
#                     # Проверяем, содержит ли считанные данные маркер конца изображения
#                     if b'END_IMAGE' in data:
#                         # Если нашли маркер конца изображения, сохраняем оставшиеся данные до маркера
#                         end_index = data.find(b'END_IMAGE')  # Находим индекс конца изображения
#                         file.write(data[:end_index])  # Записываем в файл данные до маркера конца изображения
#                         print("Передача изображения завершена.")  # Сообщаем о завершении передачи
#                         break  # Выходим из цикла, так как передача закончена
                    
#                     # Если маркер конца не найден, продолжаем записывать данные в файл
#                     file.write(data)
        
#         # Информируем о том, что изображение сохранено
#         print(f"Изображение сохранено в '{output_file}'")

# # def classify_image(image_path):
# #     try:
# #         # Открываем изображение
# #         image = Image.open(image_path).convert('RGB')

# #         # Преобразуем изображение
# #         input_tensor = transform(image).unsqueeze(0).to(device)

# #         # Классификация
# #         with torch.no_grad():
# #             outputs = model(input_tensor)
# #             _, predicted = torch.max(outputs, 1)
            
# #         class_names = ["Собака", "Лошадь", "Слон", "Бабочка", "Курица", "Кошка", "Корова", "Овца", "Паук", "Белка"]
# #         class_name = class_names[predicted.item()]

# #         # Метка времени
# #         timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# #         # Сохраняем изображение в журнал
# #         saved_image_path = os.path.join(log_dir, f"{timestamp}_{class_name}.jpg")
# #         image.save(saved_image_path)

# #         # Сохраняем запись в журнал
# #         with open(os.path.join(log_dir, "log.txt"), "a") as log:
# #             log.write(f"{timestamp}, {class_name}, {saved_image_path}\n")

# #         print(f"Изображение сохранено: {saved_image_path}, Класс: {class_name}")
# #     except Exception as e:
# #         print(f"Ошибка при обработке изображения: {e}")

# # Параметры подключения
# PORT = 'COM5'  # Укажите ваш порт
# BAUDRATE = 115200  # Укажите скорость передачи
# OUTPUT_FILE = 'photo1.jpg'  # Имя файла для сохранения изображения

# # Бесконечный цикл
# while True:
#     # Получаем изображение
#     receive_image(PORT, BAUDRATE, OUTPUT_FILE)
#     # Классифицируем изображение
#     #classify_image(OUTPUT_FILE)

#     print("Ожидание 3 секунды. Чтобы завершить работу, нажмите Ctrl+C.")
#     time.sleep(3)  # Ожидание 3 секунды

# import serial
# def receive_image(port, baudrate, output_file):
#     with serial.Serial(port, baudrate, timeout=1) as ser, open(output_file, 'wb') as file:
#         print("Ожидание начала передачи изображения...")
#         receiving_image = False

#         while True:
#             # Считываем строку, если мы еще не начали получать данные изображения
#             if not receiving_image:
#                 line = ser.readline().decode('utf-8', errors='ignore').strip()
#                 if line == "START_IMAGE":
#                     print("Начата передача изображения...")
#                     receiving_image = True
#             else:
#                 # Читаем данные блоками
#                 data = ser.read(2048)
#                 if b'END_IMAGE' in data:
#                     # Если нашли маркер конца изображения, сохраняем оставшиеся данные до маркера
#                     end_index = data.find(b'END_IMAGE')
#                     file.write(data[:end_index])  # Сохраняем данные до маркера
#                     print("Передача изображения завершена.")
#                     break
#                 file.write(data)  # Сохраняем данные в файл
#         print(f"Изображение сохранено в '{output_file}'")

# # Параметры подключения
# PORT = 'COM5'
# BAUDRATE = 115200  # Скорость передачи
# OUTPUT_FILE = 'photo.jpg'  # Имя выходного файла

# receive_image(PORT, BAUDRATE, OUTPUT_FILE)
import serial  # Импортируем библиотеку для работы с последовательными портами

def receive_image(port, baudrate, output_file):
    # Открываем последовательный порт и выходной файл для записи в бинарном режиме
    with serial.Serial(port, baudrate, timeout=1) as ser, open(output_file, 'wb') as file:
        print("Ожидание начала передачи изображения...")  # Информируем пользователя о начале ожидания
        receiving_image = False  # Флаг, указывающий, началась ли передача изображения

        while True:  # Бесконечный цикл для постоянного чтения данных
            # Если мы еще не начали получать данные изображения
            if not receiving_image:
                # Считываем строку из последовательного порта
                line = ser.readline().decode('utf-8', errors='ignore').strip()
                
                # Проверяем, соответствует ли считанная строка маркеру начала изображения
                if line == "START_IMAGE":
                    print("Начата передача изображения...")  # Сообщаем, что передача началась
                    receiving_image = True  # Устанавливаем флаг, что мы теперь находимся в режиме получения изображения
            else:
                # Если передача изображения началась, читаем данные блоками по 2048 байт
                data = ser.read(2048)
                
                # Проверяем, содержит ли считанные данные маркер конца изображения
                if b'END_IMAGE' in data:
                    # Если нашли маркер конца изображения, сохраняем оставшиеся данные до маркера
                    end_index = data.find(b'END_IMAGE')  # Находим индекс конца изображения
                    file.write(data[:end_index])  # Записываем в файл данные до маркера конца изображения
                    print("Передача изображения завершена.")  # Сообщаем о завершении передачи
                    break  # Выходим из цикла, так как передача закончена
                
                # Если маркер конца не найден, продолжаем записывать данные в файл
                file.write(data)  # Сохраняем считанные данные в выходной файл
        
        # Информируем о том, что изображение сохранено
        print(f"Изображение сохранено в '{output_file}'")

# Параметры подключения
PORT = 'COM5'  # Указываем имя последовательного порта (например, COM5 на Windows)
BAUDRATE = 115200  # Указываем скорость передачи данных
OUTPUT_FILE = 'photo.jpg'  # Имя выходного файла, в который будет сохранено изображение

# Вызываем функцию для получения изображения
# receive_image(PORT, BAUDRATE, OUTPUT_FILE)

import serial  # Импортируем библиотеку для работы с последовательными портами
import torch
from torchvision.models import resnet18
from torchvision import transforms
from PIL import Image
from datetime import datetime
import os
import time

# Загрузка модели ResNet18
model = resnet18(pretrained=False)  # Создаём модель
num_classes = 10  # Количество классов в вашей задаче
model.fc = torch.nn.Linear(model.fc.in_features, num_classes)  # Настраиваем последний слой

model_path = 'resnet18_biology.pth'  # Укажите путь к вашей сохранённой модели
model.load_state_dict(torch.load(model_path))  # Загружаем веса
model.eval()

# Устройство выполнения
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

# Преобразования для изображения
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Файл для журнала
log_file = "classification_log.txt"

# Функция классификации
import torch
from torchvision.models import resnet18
from torchvision import transforms
from PIL import Image
from datetime import datetime
import os

# Загрузка модели ResNet18
model = resnet18(pretrained=False)  # Создаём модель
num_classes = 10  # Количество классов в вашей задаче
model.fc = torch.nn.Linear(model.fc.in_features, num_classes)  # Настраиваем последний слой

model_path = 'resnet18_biology.pth'  # Укажите путь к вашей сохранённой модели
model.load_state_dict(torch.load(model_path))  # Загружаем веса
model.eval()

# Устройство выполнения
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model = model.to(device)

# Преобразования для изображения
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
])

# Папка для журнала с изображениями
log_dir = "classification_log"
os.makedirs(log_dir, exist_ok=True)

# Функция классификации
def classify_image(image_path):
    try:
        # Открываем изображение
        image = Image.open(image_path).convert('RGB')

        # Преобразуем изображение
        input_tensor = transform(image).unsqueeze(0).to(device)

        # Классификация
        with torch.no_grad():
            outputs = model(input_tensor)
            _, predicted = torch.max(outputs, 1)
            
        class_names = ["Собака", "Лошадь", "Слон", "Бабочка", "Курица", "Кошка", "Корова", "Овца", "Паук", "Белка"]
        class_name = class_names[predicted.item()]

        # Метка времени
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Сохраняем изображение в журнал
        saved_image_path = os.path.join(log_dir, f"{timestamp}_{class_name}.jpg")
        image.save(saved_image_path)

        # Сохраняем запись в журнал
        with open(os.path.join(log_dir, "log.txt"), "a") as log:
            log.write(f"{timestamp}, {class_name}, {saved_image_path}\n")

        print(f"Изображение сохранено: {saved_image_path}, Класс: {class_name}")
    except Exception as e:
        print(f"Ошибка при обработке изображения: {e}")

# Классифицируем изображение photo.jpg
while True:
    # Получаем изображение
    receive_image(PORT, BAUDRATE, OUTPUT_FILE)
    # Классифицируем изображение
    classify_image(OUTPUT_FILE)
 # Ожидание 3 секунды