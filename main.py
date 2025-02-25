import cv2
import numpy as np
from decorators import decorator


@decorator
def color_mask(img):
    hsv_image = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    cv2.imshow("grayscale", gray_image)
    cv2.imshow("hsv", hsv_image)

    lower_bound = np.array([0, 0, 0])
    upper_bound = np.array([10, 255, 255])

    mask = cv2.inRange(hsv_image, lower_bound, upper_bound)

    filtered_image = cv2.bitwise_and(img, img, mask=mask)

    cv2.imshow("mask", mask)
    cv2.imshow("filtered image", filtered_image)

    return "contours", img


@decorator
def contours(img):
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding
    _, binary = cv2.threshold(grayscale, 127, 255, cv2.THRESH_BINARY)
    cv2.imshow("binary", binary)

    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw contours
    cv2.drawContours(
        image=img, contours=contours, contourIdx=-1, color=(0, 255, 0), thickness=2
    )

    return "contours", img


@decorator
def sobel(img):

    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img, (3, 3), sigmaX=0, sigmaY=0)
    grayscale = cv2.cvtColor(img_blur, cv2.COLOR_BGR2GRAY)

    grad_x = cv2.Sobel(grayscale, cv2.CV_64F, 1, 0, ksize=3)
    grad_y = cv2.Sobel(grayscale, cv2.CV_64F, 0, 1, ksize=3)

    abs_grad_x = cv2.convertScaleAbs(grad_x)
    abs_grad_y = cv2.convertScaleAbs(grad_y)

    grad = cv2.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)

    cv2.imshow("sobel_vertical", grad_x)
    cv2.imshow("sobel_horizontal", grad_y)
    return "sobel_filter", grad


@decorator
def laplacian(img):
    grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    laplacian = cv2.Laplacian(grayscale, cv2.CV_64F)
    return "laplacian", laplacian


"""main function to run computer vision functions"""


def main():
    # color_mask()
    # contours()
    # grayscale()
    sobel()
    # laplacian()


if __name__ == "__main__":
    main()
