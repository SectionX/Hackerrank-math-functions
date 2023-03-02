import time
from PIL import Image
import os

class TimeProfiler():
    pass



def function_timer(func, *args, **kwargs):

    kw = {
            'return':1,
            'functionalities' :0
    }
    try:
        kw['return'] = kwargs['return']
    except: pass


    start = time.perf_counter()
    result = func(*args, **kwargs)
    print(time.perf_counter() - start)
    if kw['return'] == 1:
        return result
    return None


if __name__ == '__main__':
    print(function_timer(pow, 3, 2))



# def transparentbackground(imagepath, colortochange):
#     try:
#         img = Image.open(imagepath)
#         rgba = img.convert("RGBA")
#         for i in range(rgba.width):
#             for y in range(rgba.height):
#                 pixel = rgba.getpixel((i, y))
#                 if pixel[0] == colortochange[0] and pixel[1] == colortochange[1] and pixel[2] == colortochange[2]:
#                     rgba.putpixel((i,y), (255,255,255,0))
#         # rgba.putdata(pixels)
#         rgba.save(imagepath.split(".")[0]+"_transparent.png", 'PNG')
#         name = imagepath.split(".")[0] + "_transparent.png"
#         os.startfile(name)
#         print("Saved to " + name)
#     except Exception as e:
#         print(e)
#     input()


from statistics import mode
class BackgroundRemover:

    __precision = 100

    def __init__(self, color=(255,255,255)):
        self.color = color


    def setPrecision(self, num):
        if num > 100:
            print("Warning: Input must be an integer between 0 and 100. Setting Precision to 100")
            self.__precision = 100
        elif num < 0:
            print("Warning: Input must be an integer between 0 and 100. Setting Precision to 0")
            self.__precision = 0
        else:
            self.__precision = num



    def showConfig(self):
        print(f"Color = {self.color} \nPrecision = {self.__precision}")


    def guess(self, imagepath):
        pos = []
        image = Image.open(imagepath)

        pos.append(image.getpixel((0,0)))
        pos.append(image.getpixel((image.width-1,0)))
        pos.append(image.getpixel((0,image.height-1)))
        pos.append(image.getpixel((image.width-1,image.height-1)))
        return mode(pos)



    def remove(self, imagepath, *args):
        try:
            self.color = args[0](imagepath)

        except: pass
        try:
            img = Image.open(imagepath)
            rgba = img.convert("RGBA")
            for i in range(rgba.width):
                for y in range(rgba.height):
                    pixel = rgba.getpixel((i, y))
                    if pixel[0] + pixel[1] + pixel[2] >= sum(self.color[0:3])-self.__precision:
                        rgba.putpixel((i,y), (255,255,255,0))
            rgba.save(imagepath.split(".")[0]+"_transparent.png", 'PNG')
            name = imagepath.split(".")[0] + "_transparent.png"
            os.startfile(name)
            print("Saved to " + name)
        except Exception as e:
            print(e)
        time.sleep(3)

br = BackgroundRemover()
