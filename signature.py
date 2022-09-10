import cv2
from PIL import Image
from PIL import ImageFilter
from skimage.metrics import structural_similarity as ssim

def match(path1, path2):
    img1 = cv2.imread(path1)
    img2 = cv2.imread(path2)
    img1= imageObject.filter(ImageFilter.SHARPEN);
    img1= img1.filter(ImageFilter.SHARPEN);
    img2= imageObject.filter(ImageFilter.SHARPEN);
    img2= img2.filter(ImageFilter.SHARPEN);
    img1= cv2.filter2D(src=img1, ddepth=-1, kernel=kernel1)
    img2= cv2.filter2D(src=img2, ddepth=-1, kernel=kernel1)
    img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    img1 = cv2.resize(img1, (300, 300))
    img2 = cv2.resize(img2, (300, 300))
    
   
    similarity_value = "{:.2f}".format(ssim(img1, img2)*100)
    
    return float(similarity_value)


