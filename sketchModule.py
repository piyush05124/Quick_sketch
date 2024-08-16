from PIL import Image 
import cv2

def convertto_watercolorsketch(inp_img,sigma_style): 

    img_1 = cv2.edgePreservingFilter(inp_img, flags=2, sigma_s=5, sigma_r=0.8) 

    img_water_color = cv2.stylization(img_1, sigma_s=sigma_style, sigma_r=0.085) 

    return(img_water_color) 

  
# function to convert an image to a pencil sketch 

def pencilSketch(inp_img,sigma_s,sigma_r,shade_factor): 

    img_pencil_sketch, pencil_color_sketch = cv2.pencilSketch( 
        inp_img, sigma_s=sigma_s, sigma_r=sigma_r, shade_factor=shade_factor) #0.0825

        # inp_img, sigma_s=150, sigma_r=0.095, shade_factor=0.095) #0.0825

    return(img_pencil_sketch) 

  
# function to load an image 

def load_an_image(image): 

    img = Image.open(image) 

    return img 

def percentageResize(n,percent,flag = 'dec'):
    if flag.lower() == 'dec':
        return int(n-(n*(percent/100)))
    else:
        return int(n+(n*(percent/100)))




    
