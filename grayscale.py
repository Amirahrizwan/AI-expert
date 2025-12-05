import cv2

# Load the RGB image
image = cv2.imread("example.jpg")

if image is None:
    print("❌ Image not found!")
    exit()

# Convert to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Show images
cv2.imshow("Original RGB Image", image)
cv2.imshow("Grayscale Image", gray_image)

# Save grayscale image
cv2.imwrite("grayscale_output.jpg", gray_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
