import cv2
import numpy as np

# Load image
img = cv2.imread("example.jpg")

if img is None:
    print("❌ Image not found!")
    exit()

# ---------- COLOR CONVERSIONS ----------
def to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def to_hsv(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

def to_binary(img):
    gray = to_gray(img)
    _, binary = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)
    return binary

# ---------- CROPPING ----------
def crop_image(img):
    print("\nEnter cropping coordinates:")
    x1 = int(input("x1: "))
    y1 = int(input("y1: "))
    x2 = int(input("x2: "))
    y2 = int(input("y2: "))

    cropped = img[y1:y2, x1:x2]
    return cropped

# ---------- MENU LOOP ----------
while True:
    print("\n===== IMAGE PROCESSING MENU =====")
    print("1. Show Original Image")
    print("2. Convert to Grayscale")
    print("3. Convert to HSV")
    print("4. Convert to Binary")
    print("5. Crop Image")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cv2.imshow("Original", img)

    elif choice == "2":
        gray = to_gray(img)
        cv2.imshow("Grayscale", gray)

    elif choice == "3":
        hsv = to_hsv(img)
        cv2.imshow("HSV Image", hsv)

    elif choice == "4":
        binary = to_binary(img)
        cv2.imshow("Binary Image", binary)

    elif choice == "5":
        cropped = crop_image(img)
        cv2.imshow("Cropped Image", cropped)

    elif choice == "6":
        print("Exiting...")
        break

    else:
        print("❌ Invalid choice")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
