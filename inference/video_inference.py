import argparse
import os

import cv2
from tqdm import tqdm
from ultralytics import YOLO


def image_detect(model, image, conf_thres, iou_thres):
    predict = model(image, conf=conf_thres, iou=iou_thres, verbose=False)
    return predict[0].plot()


def video_detect(model, video_path, conf_thres, iou_thres, output_path):
    cap = cv2.VideoCapture(video_path)

    writer = cv2.VideoWriter(
        filename=str(output_path),
        fourcc=0x7634706D,
        fps=cap.get(cv2.CAP_PROP_FPS),
        frameSize=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))),
    )

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        result = image_detect(model, frame, conf_thres, iou_thres)
        writer.write(result)

    cap.release()
    writer.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)

    parser.add_argument(
        "--videos",
        type=str,
        dest="videos",
        help="Видео для детекции, либо директория с видео.",
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

    if os.path.isdir(args.videos):
        for video_name in tqdm(os.listdir(args.videos), leave=False):
            video_detect(
                model=model,
                video_path=os.path.join(args.videos, video_name),
                conf_thres=args.conf_thres,
                iou_thres=args.iou_thres,
                output_path=os.path.join(args.save_dir, video_name),
            )

    else:
        video_detect(
            model=model,
            video_path=args.videos,
            conf_thres=args.conf_thres,
            iou_thres=args.iou_thres,
            output_path=os.path.join(args.save_dir, os.path.basename(args.videos)),
        )
