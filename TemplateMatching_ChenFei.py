import numpy as np
import cv2

def TemplateMatching(src, temp, stepsize): # src: source image, temp: template image, stepsize: the step size for sliding the template
    mean_t = np.uint64(0)
    var_t = np.uint64(0)
    location = [0, 0]
    # Calculate the mean and variance of template pixel values
    # ------------------ Put your code below ------------------
    sumSquare = np.uint64(0)
    squareSum = np.uint64(0)
    Sum = np.uint64(0)
    N = temp.size
    for i in np.arange(0, temp.shape[0]):
        for j in np.arange(0, temp.shape[1]):
            Sum += temp[i,j]
            squareSum += (temp[i,j])**2
    mean_t = Sum / N
    var_t = (squareSum - Sum**2 / N)/N

    max_corr = 0;
    # Slide window in source image and find the maximum correlation
    for i in np.arange(0, src.shape[0] - temp.shape[0], stepsize):
        for j in np.arange(0, src.shape[1] - temp.shape[1], stepsize):
            print ((i,j))
            mean_s =  np.uint64(0)
            var_s =  np.uint64(0)
            corr =  np.uint64(0)
            # Calculate the mean and variance of source image pixel values inside window
            # ------------------ Put your code below ------------------
            sumSquare =  np.uint64(0)
            squareSum =  np.uint64(0)
            Sum = np.uint64(0)
            for n in np.arange(0, temp.shape[0]):
                for m in np.arange(0, temp.shape[1]):
                    Sum += src[n+i,m+j]
                    squareSum += (src[n+i,m+j])**2
            mean_s = Sum / N
            var_s = (squareSum - Sum**2 / N)/N
            
            # Calculate normalized correlation coefficient (NCC) between source and template
            # ------------------ Put your code below ------------------ 
            for n in np.arange(0, temp.shape[0]):
                for m in np.arange(0, temp.shape[1]):
                    corr += (src[n+i,m+j] - mean_s) * (temp[n,m] - mean_t)
            corr = corr / (N * var_t * var_s)
            print("corr = " + str(corr))
            if corr > max_corr:
                max_corr = corr;
                location = [i, j];
                print("Max corr = " + str(corr))
    return location

def main():
    # load source and template images
    source_img = cv2.imread('source_img.jpg',0) # read image in grayscale
    print(source_img.shape)
    temp = cv2.imread('template.jpg',0) # read image in grayscale
    print(temp.shape)
    location = TemplateMatching(source_img, temp, 50);
    print(location)
    match_img = cv2.cvtColor(source_img, cv2.COLOR_GRAY2RGB)

    # Draw a red rectangle on match_img to show the template matching result
    # ------------------ Put your code below ------------------
    (x, y) = location
    (w, h) = temp.shape
    cv2.rectangle(match_img,(x,y),(x+w,y+h),(255,0,0),3)

        
    # Save the template matching result image (match_img)
    # ------------------ Put your code below ------------------ 
    cv2.imwrite('MyTemplateMatching', match_img)


    # Display the template image and the matching result
    cv2.namedWindow('TemplateImage', cv2.WINDOW_NORMAL)
    cv2.namedWindow('MyTemplateMatching', cv2.WINDOW_NORMAL)
    cv2.imshow('TemplateImage', temp)
    cv2.imshow('MyTemplateMatching', match_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
