import argparse
import os

import cv2
from tqdm import tqdm
from ultralytics import YOLO


def image_detect(model, image_path, conf_thres, iou_thres, output_path):
    image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
    predict = model(image, conf=conf_thres, iou=iou_thres, verbose=False)
    frame = predict[0].plot()

    cv2.imwrite(output_path, frame)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)

    parser.add_argument(
        "--images",
        type=str,
        dest="images",
        help="Изображение для детекции, либо директория с изображениями.",
    )

    parser.add_argument(
        "-m",
        "--model",
        type=str,
        dest="model",
        default="models/garbage.onnx",
        help="Путь до модели",
    )

    parser.add_argument(
        "--conf_thres",
        type=float,
        dest="conf_thres",
        default=0.4,
        help="confidence threshold",
    )

    parser.add_argument(
        "--iou_thres",
        type=float,
        dest="iou_thres",
        default=0.5,
        help="iou threshold",
    )

    parser.add_argument(
        "--save_dir", dest="save_dir", type=str, default="predict", help="Диретория для сохранения результатов."
    )

    args = parser.parse_args()
    os.makedirs(args.save_dir, exist_ok=True)

    model = YOLO(args.model, task="detect")

    if os.path.isdir(args.images):
        for image_name in tqdm(os.listdir(args.images), leave=False):
            image_detect(
                model=model,
                image_path=os.path.join(args.images, image_name),
                conf_thres=args.conf_thres,
                iou_thres=args.iou_thres,
                output_path=os.path.join(args.save_dir, image_name),
            )

    else:
        image_detect(
            model=model,
            image_path=args.images,
            conf_thres=args.conf_thres,
            iou_thres=args.iou_thres,
            output_path=os.path.join(args.save_dir, os.path.basename(args.images)),
        )
