import argparse
import json
import os
from pathlib import Path

from tqdm import tqdm


def convert_bbox(x1, y1, w, h, image_w, image_h):
    return [(2 * x1 + w) / (2 * image_w), (2 * y1 + h) / (2 * image_h), w / image_w, h / image_h]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(add_help=True)

    parser.add_argument(
        "--json_dir",
        type=str,
        dest="json_dir",
        help="Путь до директории с аннотациями в формате .json",
    )

    parser.add_argument(
        "--labels_path",
        type=str,
        dest="labels_path",
        help="Путь до директории, в которую будут записаны аннотации",
        default="labels",
    )

    args = parser.parse_args()
    os.makedirs(args.labels_path, exist_ok=True)

    for annot in tqdm(os.listdir(args.json_dir)):
        data = json.load(open(os.path.join(args.json_dir, annot)))

        img_height = data["size"]["height"]
        img_width = data["size"]["width"]

        with open(os.path.join(args.labels_path, Path(annot).with_suffix("").with_suffix(".txt")), "w") as file:
            for object in data["objects"]:

                [x1, y1], [x2, y2] = object["points"]["exterior"]

                h = y2 - y1
                w = x2 - x1

                bbox = convert_bbox(x1, y1, w, h, img_width, img_height)

                file.write(f"0 {' '.join(list(map(str, bbox)))}\n")
