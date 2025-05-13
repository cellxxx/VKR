#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Скрипт для разбиения датасета AgeDB по трем возрастным группам
(child, adult, elderly) и деления на train/valid (80/20).

Исходники: файлы вида НомерФото_ИмяЧеловека_Возраст_Пол.jpg
(например, 001_ivanpavlov_34_M.jpg)

Результат:
 data/
   train/
     child/ adult/ elderly/
   valid/
     child/ adult/ elderly/
"""

import os
import shutil
import random

# === ПАРАМЕТРЫ ===

SRC_DIR     = "AgeDB"   # папка с вашими файлами
OUTPUT_DIR  = "data"
TRAIN_RATIO = 0.8

AGE_GROUPS = [
    ( 0,  12, "child"),
    (13,  59, "adult"),
    (60, 200, "elderly"),
]


# === УТИЛИТЫ ===

def parse_age(filename: str) -> int:
    """
    Извлекает возраст из имени файла вида:
      Номер_Имя_Возраст_Пол.ext
    """
    base = os.path.basename(filename)
    name, _ext = os.path.splitext(base)
    parts = name.split("_")
    if len(parts) < 3:
        raise ValueError(f"Невалидное имя файла: {base}")
    age_str = parts[2]
    return int(age_str)


def ensure_output_dirs():
    """Создает структуру data/train|valid / child|adult|elderly."""
    for split in ("train", "valid"):
        for _lo, _hi, grp in AGE_GROUPS:
            os.makedirs(os.path.join(OUTPUT_DIR, split, grp), exist_ok=True)


# === ГЛАВНАЯ ЛОГИКА ===

def main():
    random.seed(42)

    # 1) Собираем все записи (путь + группа)
    entries = []
    for fname in os.listdir(SRC_DIR):
        if not fname.lower().endswith((".jpg", ".jpeg", ".png")):
            continue
        try:
            age = parse_age(fname)
        except ValueError:
            continue

        # определяем группу по возрасту
        grp = None
        for lo, hi, name in AGE_GROUPS:
            if lo <= age <= hi:
                grp = name
                break
        if grp is None:
            continue

        src_path = os.path.join(SRC_DIR, fname)
        entries.append((src_path, grp))

    if not entries:
        print("❌ Не найдено ни одного файла подходящего формата в", SRC_DIR)
        return

    print(f"Найдено {len(entries)} файлов, разбиваем на train/valid…")
    random.shuffle(entries)
    split_idx = int(len(entries) * TRAIN_RATIO)
    train_entries = entries[:split_idx]
    valid_entries = entries[split_idx:]

    # 2) Создаем каталоги
    ensure_output_dirs()

    # 3) Копируем файлы
    for split_name, split_list in (("train", train_entries), ("valid", valid_entries)):
        print(f"Копирую {len(split_list)} файлов → {split_name}/")
        for src, grp in split_list:
            dst = os.path.join(OUTPUT_DIR, split_name, grp, os.path.basename(src))
            shutil.copyfile(src, dst)

    # 4) Итоги
    print("\n✅ Готово. Итоговое распределение:")
    for split_name in ("train", "valid"):
        print(f" {split_name.upper()}:")
        for _lo, _hi, grp in AGE_GROUPS:
            cnt = len(os.listdir(os.path.join(OUTPUT_DIR, split_name, grp)))
            print(f"   {grp:7s}: {cnt}")

if __name__ == "__main__":
    main()
