import cv2
import numpy as np

# Load Image
img = cv2.imread("example.jpg")
if img is None:
    print("❌ Image not found!")
    exit()

def rotate(img, angle):
    h, w = img.shape[:2]
    center = (w // 2, h // 2)
    matrix = cv2.getRotationMatrix2D(center, angle, 1)
    return cv2.warpAffine(img, matrix, (w, h))

def adjust_brightness(img, value):
    return cv2.convertScaleAbs(img, alpha=1, beta=value)

while True:
    print("\n===== IMAGE ROTATION & BRIGHTNESS MENU =====")
    print("1. Show Original Image")
    print("2. Rotate Left 90°")
    print("3. Rotate Right 90°")
    print("4. Rotate Custom Angle")
    print("5. Increase Brightness")
    print("6. Decrease Brightness")
    print("7. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        cv2.imshow("Original", img)

    elif choice == "2":
        rotated = rotate(img, 90)
        cv2.imshow("Rotated Left 90°", rotated)

    elif choice == "3":
        rotated = rotate(img, -90)
        cv2.imshow("Rotated Right 90°", rotated)

    elif choice == "4":
        angle = float(input("Enter angle to rotate: "))
        rotated = rotate(img, angle)
        cv2.imshow(f"Rotated {angle}°", rotated)

    elif choice == "5":
        value = int(input("Brightness increase (0–100): "))
        bright = adjust_brightness(img, value)
        cv2.imshow("Increased Brightness", bright)

    elif choice == "6":
        value = int(input("Brightness decrease (0–100): "))
        bright = adjust_brightness(img, -abs(value))
        cv2.imshow("Decreased Brightness", bright)

    elif choice == "7":
        print("Exiting…")
        break

    else:
        print("❌ Invalid choice")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
