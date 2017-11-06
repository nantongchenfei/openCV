import cv2

def main():
    filename = "./cat.jpg"
    src = cv2.imread(filename,cv2.IMREAD_COLOR)
    b,g,r = cv2.split(src)
    ycrcb_image = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
    y,cb,cr = cv2.split(ycrcb_image)
    hsv_image = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    h,s,v = cv2.split(hsv_image)
    
    cv2.imshow("Original image",src)
    cv2.imshow("Y",y)
    cv2.imshow("Cb",cb)
    cv2.imshow("Cr",cr)
    cv2.imshow("Hue",h)
    cv2.imshow("Red",r)
    cv2.imshow("Green",g)
    cv2.imshow("Blue",b)
    cv2.imshow("Value",v) 
    cv2.imshow("Saturation",s)
  
    
    cv2.waitKey(0)
    cv2.imwrite("./Pics_write/Red.jpg",r)
    cv2.imwrite("./Pics_write/Y.jpg",y)
    cv2.imwrite("./Pics_write/Cb.jpg",cb)
    cv2.imwrite("./Pics_write/Cr.jpg",cr)
    cv2.imwrite("./Pics_write/Hue.jpg",h)
    cv2.imwrite("./Pics_write/Green.jpg",g)
    cv2.imwrite("./Pics_write/Blue.jpg",b)
    cv2.imwrite("./Pics_write/Value.jpg",v)
    cv2.imwrite("./Pics_write/Saturation.jpg",s)
   
    exit()
    
if __name__ == "__main__":
    main()
