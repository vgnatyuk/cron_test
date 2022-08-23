import os
import shutil
import sys
from datetime import datetime

from config import RESIZE, WATERMARK, DATE, PICTURE_EXTENSIONS, ERROR_LOG


class PictureHandler:

    def __init__(
            self,
            source: str,
            destination: str,
            resize: bool,
            watermark: bool,
            date: bool,
            extensions: list,
    ):
        self.source = source
        self.destination = destination
        self.resize = resize
        self.watermark = watermark
        self.date = date
        self.extensions = extensions
        if not os.path.exists(self.destination):
            os.mkdir(self.destination)

    def do_resize(self, image_path: str):
        if self.resize:
            pass  # do resize

    def add_watermark(self, image_path: str):
        if self.watermark:
            pass  # add watermark

    def add_date(self, image_path: str):
        if self.date:
            pass  # add date

    def move_to(self, image_path: str):
        full_path_from = os.path.join(self.source, image_path)
        full_path_to = os.path.join(self.destination, image_path)
        os.path.isdir(full_path_from)
        shutil.move(full_path_from, full_path_to)

    def parse_folder(self) -> list:
        for _, _, filenames in tuple(os.walk(self.source)):
            return [
                filename for filename in filenames
                if filename.split('.')[-1] in self.extensions
            ]

    def run(self):
        images = self.parse_folder()
        for image in images:
            self.do_resize(image)
            self.add_watermark(image)
            self.add_date(image)
            self.move_to(image)


def main():
    # error_path = os.path.dirname(sys.argv[0])
    # path_from = sys.argv[1]
    # path_to = sys.argv[2]

    error_path = 'error.log'
    path_from = 'unhandled'
    path_to = 'processed'

    picture_handler = PictureHandler(
        source=path_from,
        destination=path_to,
        resize=RESIZE,
        watermark=WATERMARK,
        date=DATE,
        extensions=PICTURE_EXTENSIONS,
    )
    try:
        picture_handler.run()
    except Exception as exc:
        with open(os.path.join(error_path, ERROR_LOG), 'a') as log:
            now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            log.write(f'[{now}] {exc} - {exc.args}\n')


if __name__ == '__main__':
    main()
