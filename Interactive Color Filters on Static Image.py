import cv2
import numpy as np

# Load image
img = cv2.imread("example.jpg")
if img is None:
    print("❌ Image not found!")
    exit()

original = img.copy()

# ----------- Filter Functions -----------

def to_gray(img):
    return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def to_sepia(img):
    kernel = np.array([[0.272, 0.534, 0.131],
                       [0.349, 0.686, 0.168],
                       [0.393, 0.769, 0.189]])
    return cv2.transform(img, kernel)

def to_negative(img):
    return 255 - img

def to_blur(img):
    return cv2.GaussianBlur(img, (15, 15), 0)

def to_edges(img):
    gray = to_gray(img)
    edges = cv2.Canny(gray, 80, 150)
    return cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

# ----------- Instructions -----------
print("""
========= INTERACTIVE FILTER CONTROLS =========
g → Grayscale
s → Sepia
n → Negative
b → Blur
e → Edge Detection
r → Reset to Original
q → Quit
===============================================
""")

img_display = img.copy()

# ----------- Main Loop -----------
while True:
    cv2.imshow("Interactive Color Filters", img_display)
    key = cv2.waitKey(0) & 0xFF

    if key == ord('g'):
        img_display = to_gray(img)
        img_display = cv2.cvtColor(img_display, cv2.COLOR_GRAY2BGR)

    elif key == ord('s'):
        img_display = to_sepia(img)

    elif key == ord('n'):
        img_display = to_negative(img)

    elif key == ord('b'):
        img_display = to_blur(img)

    elif key == ord('e'):
        img_display = to_edges(img)

    elif key == ord('r'):
        img_display = original.copy()

    elif key == ord('q'):
        break

cv2.destroyAllWindows()
