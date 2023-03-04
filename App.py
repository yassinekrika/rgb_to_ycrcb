import cv2
import matplotlib.pyplot as plt

class App():
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = cv2.imread(image_path)
        self.yrccb_image  = self.convert_image_to_YCrCb(self.image)
        self.ycrcb_to_rgb(self.yrccb_image)

    def convert_image_to_YCrCb(self, image):

        # Img to YCrCb
        R, G, B = cv2.split(image)

        Y = 0.299 * R + 0.587 * G + 0.114 * B
        Cb = 128 + (-0.169 * R - 0.331 * G + 0.5 * B)
        Cr = 128 + (0.5 * R - 0.419 * G - 0.081 * B)

        ycrcb_image = cv2.merge((Y, Cr, Cb))
        

        cv2.imwrite("/home/yassg4mer/Project/tp_tmn/echentillonnage/YcrCb.bmp", ycrcb_image)

        # show figure
        plt.figure(figsize=(10,10))
        plt.subplot(131)
        plt.imshow(Y)
        plt.title('Y')
        plt.subplot(132)
        plt.imshow(Cr)
        plt.title('Cr')
        plt.subplot(133)
        plt.imshow(Cb)
        plt.title('Cb')
        plt.show()

        return ycrcb_image
    
    def ycrcb_to_rgb(self, image):
        # image = cv2.imread(image_path)
        # Split the YCrCb channels
        Y, Cr, Cb = cv2.split(image)

        # Calculate the R, G, and B channels
        R = Y + 1.403 * (Cr - 128)
        G = Y - 0.344 * (Cb - 128) - 0.714 * (Cr - 128)
        B = Y + 1.773 * (Cb - 128)

        # Stack the R, G, and B channels to form the RGB image
        rgb_image = cv2.merge((R, G, B))

        cv2.imwrite("/home/yassg4mer/Project/tp_tmn/echentillonnage/RGB.bmp", rgb_image)



if __name__=="__main__":
    image_path = '/home/yassg4mer/Project/tp_tmn/echentillonnage/original_image.bmp'
    App(image_path)