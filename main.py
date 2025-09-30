import cv2
from cartoonize import caart

choice = input("Choose input source:\n1 - Image\n2 - Webcam\nEnter 1 or 2: ")

if choice == '1':
    image_path = input("Enter the path of the image: ")
    img = cv2.imread(image_path)
    if img is None:
        print(f"Error: Image '{image_path}' not found.")
        exit()
    cartoon_img = caart(img)
    cv2.imshow("Cartoon", cartoon_img)
    print("Press any key to exit.")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

elif choice == '2':
    videoCaptureObject = cv2.VideoCapture(0)
    if not videoCaptureObject.isOpened():
        print("Error: Could not open webcam.")
        exit()
    print("Press ESC to stop.")

    while True:
        ret, img = videoCaptureObject.read()
        if not ret:
            break
        cartoon_img = caart(img)
        cv2.imshow("Cartoon", cartoon_img)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC key
            break

    videoCaptureObject.release()
    cv2.destroyAllWindows()

else:
    print("Invalid choice. Please enter 1 for Image or 2 for Webcam.")
