# <div align="center">Garbage detection</div>


<p align="center">
  <img src="https://github.com/HerrPhoton/Garbage_detection/blob/main/doc/images/logo.jpg">
</p>

---

<img src = "https://img.shields.io/badge/Python 3.10-006C6B?style=for-the-badge&color=3a3b3a&labelColor=%3a3b3a&logo=python&logoColor=FFFFFF">  <img src ='https://img.shields.io/github/repo-size/HerrPhoton/Garbage_detection?style=for-the-badge&color=FABB22&labelColor=%96CEB4&logo=weightsandbiases&logoColor=96CEB4'>

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1)](https://pycqa.github.io/isort/)
[![Formatter: docformatter](https://img.shields.io/badge/%20formatter-docformatter-fedcba.svg)](https://github.com/PyCQA/docformatter/tree/master)


<details open>
<summary><h1>Описание задачи</h1></summary>

С каждым днём всё больше распространяется проблема загрезнения окружающей среды различным мусором. В городах уборкой улиц от мусора занимаются городские службы, однако осмотр большой территории может занимать очень много времени, поэтому было бы гораздо эффективней использовать беспилотные летательные аппараты, которые стали очень распространены. Дроны могли бы обнаруживать мусор на улицах города и отмечать его на карте.

Для реализации данной идеи необходимо обучить нейронную сеть, способную определять разные виды мусора с высоты 2-10м.

</details>

---
<details open>
<summary><h1>Решение задачи</h1></summary>

Для решения поставленной задачи была выбрана модель YOLOv8n. Данная архитектура обладает хорошой точностью и быстрой скоростью работы, что позволяет использовать её без наличия GPU и, соответственно, на дроне.

<p align="center">
  <img src="https://github.com/HerrPhoton/Garbage_detection/blob/main/doc/images/ultralytics_yolov8_image.png" width = 800px height = 400px>
</p>

</details>

---
<details open>
<summary><h1>Датасет</h1></summary>

Модель была обучена на датасете, состоящего из 16 262 тренировочных изображений.

Тренировочные изображения взяты из нескольких разных датасетов, найденных в интернете. Эти изображения содержат различные виды мусора (бутылки, пакеты, органика), которые находятся на различном фоне (трава, асфальт, плитка).

<p align="center">
  <img src="https://github.com/HerrPhoton/Garbage_detection/blob/main/doc/images/train1.jpeg" width = 302px height = 403px> <img src="https://github.com/HerrPhoton/Garbage_detection/blob/main/doc/images/train2.jpeg" width = 302px height = 403px> <img src="https://github.com/HerrPhoton/Garbage_detection/blob/main/doc/images/train3.jpg" width = 302px height = 403px>
</p>

В датасете имеются синтетические изображения с окурками (~6% от всего датасета).

<p align="center">
  <img src="https://github.com/HerrPhoton/Garbage_detection/blob/main/doc/images/cigarettes1.jpg" width = 320px height = 320px> <img src="https://github.com/HerrPhoton/Garbage_detection/blob/main/doc/images/cigarettes2.jpg" width = 320px height = 320px> <img src="https://github.com/HerrPhoton/Garbage_detection/blob/main/doc/images/cigarettes3.jpg" width = 320px height = 320px>
</p>

Также для уменьшения ложно-положительных результатов модели в тренировочный датасет были добавлены изображения, которые не содержат мусора. (~30% от всего датасета).

<p align="center">
  <img src="https://github.com/HerrPhoton/Garbage_detection/blob/main/doc/images/background1.jpg" width = 320px height = 320px> <img src="https://github.com/HerrPhoton/Garbage_detection/blob/main/doc/images/background2.jpg" width = 320px height = 320px>
</p>

Перед обучением весь датасет был проверен на дубликаты и протечки, путем создания эмбеддингов и определения косинусного расстояния между ними (порог косинусного расстояния - 0.99).

<p align="center">
  <img src="https://github.com/HerrPhoton/Garbage_detection/blob/main/doc/images/duplicates.png">
</p>

</details>

---
<details open>
<summary><h1>Результат обучения</h1></summary>

<p align="center">
  <img src="https://github.com/HerrPhoton/Garbage_detection/blob/main/doc/images/results.png">
</p>

## Результат запуска модели на тестовом датасете:

| Images | Instances | Box(P | R    | mAP50 | mAP50-95) |
|--------|-----------|-------|------|-------|-----------|
| 368    | 1867      | 0.816 | 0.28 | 0.541 | 0.34      |

<p align="center">
  <img src="https://github.com/HerrPhoton/Garbage_detection/blob/main/doc/images/test1.jpg" width = 960px height = 458px>
</p>

---

В результате, модель способна, в основном, определять мусор с небольшой высоты, так как в датасете изображения с мусором сняты с высоты ~2м. Помимо этого, модель, в основном, способна определять отдельные объекты, а не большую кучу сразу, так как в датасете нет соответствующих примеров. Также из тестового видео заметно, что модель ложно определяет мусором некоторые городские урашения, что говорит о необходимости добавления соответствующих примеров в тренировочный датасет.

## Результат запуска модели на тестовом видео:

<p align="center">
  <img src="https://github.com/HerrPhoton/Garbage_detection/blob/main/doc/gif/test_predict.gif" width = 732px height = 412px>
</p>

</details>

---

# Документация

<details open>
<summary><h2>Установка</h2></summary>

Склонируйте репозиторий и установите все необходимые зависимости.

```bash
git clone https://github.com/HerrPhoton/Garbage_detection.git
pip install -r requirements.txt
```

</details>

<details open>
<summary><h2>Использование</h2></summary>

Для запуска на изображении или на директории с изображениями используйте image_inference.py, который находится в директории inference

```bash
python .\inference\image_inference.py --images <path/to/image> -m .\models\garbage.onnx
```

Для запуска на видео или на директории с видео используйте video_inference.py, который находится в директории inference

```bash
python .\inference\video_inference.py --videos <path/to/video> -m .\models\garbage.onnx
```

Дополнительные параметры можно посмотреть, добавив --help.

```bash
python .\inference\image_inference.py --help
```
```bash
python .\inference\video_inference.py --help
```

</details>

<details open>
<summary><h2>Обучение</h2></summary>

## CLI

```bash
yolo detect train data=datasets/garbage_dataset/data.yaml model=yolov8n.yaml pretrained=yolov8n.pt epochs=150 imgsz=640 batch=64 patience=50
```
## Python

```Python
from ultralytics import YOLO

model = YOLO('yolov8n.pt')
results = model.train(data='datasets/garbage_dataset/data.yaml', epochs=150, imgsz=640, batch=64, patience=50)
```

</details>
