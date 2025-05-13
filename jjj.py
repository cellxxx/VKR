#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
convert_png_to_jpg.py

Рекурсивно обходит папку src_dir, находит все .png-файлы,
конвертирует их в .jpg, сохраняя ту же структуру каталогов.
"""

import os
from PIL import Image

# Папка с исходными PNG
src_dir = 'src_dir'
# Куда сохранять JPG; если равен src_dir — перезаписываем рядом
dest_dir = 'srsc_dir'
# Качество сохраняемых JPG (0–100)
quality = 95

def convert_png_to_jpg():
    src_dir_abs = os.path.abspath(src_dir)
    dest_dir_abs = os.path.abspath(dest_dir)

    for root, _, files in os.walk(src_dir_abs):
        # относительный путь от src_dir
        rel_root = os.path.relpath(root, src_dir_abs)
        target_root = os.path.join(dest_dir_abs, rel_root)
        os.makedirs(target_root, exist_ok=True)

        for fname in files:
            if not fname.lower().endswith('.png'):
                continue

            png_path = os.path.join(root, fname)
            jpg_name = os.path.splitext(fname)[0] + '.jpg'
            jpg_path = os.path.join(target_root, jpg_name)

            try:
                with Image.open(png_path) as im:
                    rgb = im.convert('RGB')
                    rgb.save(jpg_path, 'JPEG', quality=quality)
                print(f"Converted: {png_path} → {jpg_path}")
            except Exception as e:
                print(f"Error converting {png_path}: {e}")

if __name__ == '__main__':
    convert_png_to_jpg()
