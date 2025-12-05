import cv2
import numpy as np
import math

# Load image
img = cv2.imread("example.jpg")
if img is None:
    print("❌ Image not found!")
    exit()

clone = img.copy()
points = []   # store clicked points
mode = ""      # shape mode

def distance(p1, p2):
    return round(math.dist(p1, p2), 2)

def click_event(event, x, y, flags, param):
    global points, mode, img, clone

    if event == cv2.EVENT_LBUTTONDOWN:
        points.append((x, y))

        # --- Line Measurement ---
        if mode == "line" and len(points) == 2:
            p1, p2 = points
            cv2.line(img, p1, p2, (0,255,0), 2)
            d = distance(p1, p2)
            cv2.putText(img, f"{d}px", p2, cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,0), 2)
            points = []

        # --- Rectangle Measurement ---
        elif mode == "rect" and len(points) == 2:
            p1, p2 = points
            cv2.rectangle(img, p1, p2, (255,0,0), 2)

            w = abs(p2[0] - p1[0])
            h = abs(p2[1] - p1[1])
            area = w * h

            cv2.putText(img, f"W:{w}px H:{h}px", (p1[0], p1[1]-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)
            cv2.putText(img, f"Area:{area}px²", (p1[0], p1[1]-30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255,0,0), 2)

            points = []

        # --- Circle Measurement ---
        elif mode == "circle" and len(points) == 2:
            center = points[0]
            radius = int(distance(points[0], points[1]))

            cv2.circle(img, center, radius, (0,0,255), 2)
            cv2.putText(img, f"R:{radius}px", (center[0]+5, center[1]+5),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,0,255), 2)

            points = []

        # Add a small dot where the user clicks
        cv2.circle(img, (x,y), 3, (255,255,255), -1)

# ---------------- MAIN MENU LOOP ----------------
while True:
    print("\n===== IMAGE ANNOTATION MENU =====")
    print("1. Draw & Measure Line")
    print("2. Draw Rectangle + Area")
    print("3. Draw & Measure Circle")
    print("4. Reset Image")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        mode = "line"
        img = clone.copy()
        print("Click two points to measure line length.")

    elif choice == "2":
        mode = "rect"
        img = clone.copy()
        print("Click two opposite corners to draw rectangle.")

    elif choice == "3":
        mode = "circle"
        img = clone.copy()
        print("Click center point, then radius point.")

    elif choice == "4":
        img = clone.copy()
        print("Image reset.")
        continue

    elif choice == "5":
        print("Exiting...")
        break

    else:
        print("❌ Invalid choice!")
        continue

    # Mouse callback
    cv2.namedWindow("Annotator")
    cv2.setMouseCallback("Annotator", click_event)

    # Display loop
    while True:
        cv2.imshow("Annotator", img)
        key = cv2.waitKey(1)

        if key == ord('q'):
            break

cv2.destroyAllWindows()
