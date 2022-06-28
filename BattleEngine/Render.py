import PIL
from PIL import Image, ImageDraw, ImageColor, ImageTk


class Render:

    @staticmethod
    def draw_grid(color: str = None):
        if color is None:
            color = 'green'

        img = Image.new(mode="RGB", size=(612, 612), color='black')

        image = ImageDraw.Draw(img)

        
        for i in range(1, 5):
            x, y = 123 * i, 123 * i
            image.line((x-2, 0, x-2, 612), width=3, fill=ImageColor.getrgb(color))
            image.line((0, y-2, 612, y-2), width=3, fill=ImageColor.getrgb(color))

        return img

    @staticmethod
    def render_unit(img, x: int, y: int):
        img.paste(Image.open("./assets/test.png"), (x,y))
        return img