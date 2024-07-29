import cv2
import os
import time

def take_photo_and_save(counter):
    # Access the camera (0 is usually the default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        return

    # Read a frame from the camera
    ret, frame = cap.read()

    if ret:
        user_profile = os.getenv('USERPROFILE')
        base_name = 'pwn'
        image_path = os.path.join(user_profile, f'{base_name}_{counter}.jpg')

        # Save the frame as an image file
        cv2.imwrite(image_path, frame)

    # Release the camera
    cap.release()

if __name__ == "__main__":
    for i in range(10):
        take_photo_and_save(i + 1)
        time.sleep(1)
