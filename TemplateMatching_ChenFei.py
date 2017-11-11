import numpy as np
import cv2

def TemplateMatching(src, temp, stepsize): # src: source image, temp: template image, stepsize: the step size for sliding the template
    src_data = np.uint64(src)
    temp_data = np.uint64(temp)
    mean_t = 0.0
    var_t = 0.0
    location = [0, 0]
    (H , W) = temp.shape
    # Calculate the mean and variance of template pixel values
    N = H * W
    mean_t = sum(sum(temp_data)) / N
    var_t = sum(sum((temp_data - mean_t)**2)) / N

    # Slide window in source image and find the maximum correlation
    max_corr = 0;
    for i in range(0, src.shape[0] - temp.shape[0], stepsize):
        for j in range(0, src.shape[1] - temp.shape[1], stepsize):
            mean_s =  0.0
            var_s =  0.0
            corr =  0.0
            # Calculate the mean and variance of source image pixel values inside window
            mean_s = sum(sum(src_data[i:i+H , j:j+W])) / N
            var_s = (sum(sum((src_data[i:i+H , j:j+W] - mean_s)**2))) / N
            
            # Calculate normalized correlation coefficient (NCC) between source and template
            corr = sum(sum((src_data[i:i+H , j:j+W] - mean_s) * (temp_data - mean_t))) / (N * var_t * var_s)
            if corr > max_corr:
                max_corr = corr;
                location = [i, j];
    return location

def main():
    # load source and template images
    source_img = cv2.imread('source_img2.jpg',0) # read image in grayscale
    temp = cv2.imread('template2.jpg',0) # read image in grayscale
    
    location = TemplateMatching(source_img, temp, 20);
    match_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)

    # Draw a red rectangle on match_img to show the template matching result
    # ------------------ Put your code below ------------------
    (y, x) = location
    (h, w) = temp.shape
    cv2.rectangle(match_img,(x,y),(x+w,y+h),(0,0,255),2)

        
    # Save the template matching result image (match_img)
    # ------------------ Put your code below ------------------ 
    cv2.imwrite('MyTemplateMatching.jpg', match_img)
##    cv2.imwrite('TemplateImage.jpg', temp)


    # Display the template image and the matching result
    cv2.imshow('sourceImage', source_img)
    cv2.imshow('TemplateImage', temp)
    cv2.imshow('MyTemplateMatching', match_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
