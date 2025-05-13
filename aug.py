# import torch
# import torchvision.transforms as transforms
# from torchvision.datasets import ImageFolder
# from torch.utils.data import DataLoader
# import matplotlib.pyplot as plt
# import numpy as np

# def imshow(img, title="Augmented Image"):
#     """ Функция для отображения изображения """
#     img = img.numpy().transpose((1, 2, 0))
#     mean = np.array([0.485, 0.456, 0.406])
#     std = np.array([0.229, 0.224, 0.225])
#     img = img * std + mean  # Деинормализация
#     img = np.clip(img, 0, 1)
#     plt.imshow(img)
#     plt.title(title)
#     plt.axis('off')
#     plt.show()

# def get_dataloaders(train_dir, batch_size=8):
#     # Аугментация данных
#     train_transforms = transforms.Compose([
#         transforms.RandomResizedCrop(224),
#         transforms.RandomHorizontalFlip(),
#         transforms.RandomRotation(20),
#         transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
#         transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),
#         transforms.RandomPerspective(distortion_scale=0.2, p=0.5),
#         transforms.ToTensor(),
#         transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
#     ])

#     train_dataset = ImageFolder(root=train_dir, transform=train_transforms)

#     train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=0)

#     return train_loader

# if __name__ == '__main__':
#     train_dir = "dataset/train"  # Укажи путь к тренировочным данным
#     train_loader = get_dataloaders(train_dir)

#     # Визуализация первых нескольких изображений после аугментации
#     data_iter = iter(train_loader)
#     images, labels = next(data_iter)

#     for i in range(min(5, len(images))):  # Отобразим 5 изображений
#         imshow(images[i])

import os
import glob
from PIL import Image
import torchvision.transforms as transforms

# Папки с исходными и аугментированными изображениями
input_dir = "dataset2/train/elderly"
output_dir = "dataset2/train/elderly"

# Расширения, по которым ищем
extensions = ("*.jpg", "*.jpeg", "*.png")

# Создаем выходную папку, если её нет
os.makedirs(output_dir, exist_ok=True)

# Аугментации
augmentations = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(20),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.1),
    transforms.RandomAffine(degrees=0, translate=(0.1, 0.1)),
    transforms.RandomPerspective(distortion_scale=0.2, p=0.5),
    transforms.ToTensor(),
    transforms.ToPILImage()
])

# Проходим по всем подпапкам
for root, dirs, files in os.walk(input_dir):
    # Определяем относительный путь (для воспроизведения структуры папок)
    rel_path = os.path.relpath(root, input_dir)
    target_subdir = os.path.join(output_dir, rel_path)
    os.makedirs(target_subdir, exist_ok=True)

    # Ищем файлы по расширениям
    for ext in extensions:
        for img_path in glob.glob(os.path.join(root, ext)):
            try:
                img = Image.open(img_path).convert("RGB")
            except Exception as e:
                print(f"Не удалось открыть {img_path}: {e}")
                continue

            base_name = os.path.splitext(os.path.basename(img_path))[0]
            # Генерируем 5 аугментированных копий
            for i in range(5):
                aug = augmentations(img)
                out_name = f"{base_name}_aug_{i}.jpg"
                out_path = os.path.join(target_subdir, out_name)
                aug.save(out_path)

print("Аугментированные изображения сохранены в:", output_dir)
