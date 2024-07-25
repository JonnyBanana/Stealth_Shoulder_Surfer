import cv2
import os
import time

def record_video_and_save():
    # Access the camera (0 is usually the default camera)
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        return

    # Get the user's home directory
    user_profile = os.getenv('USERPROFILE')
    base_name = 'ciak'
    video_path = os.path.join(user_profile, f'{base_name}.avi')

    # Check if the file already exists and find a unique name
    counter = 1
    while os.path.exists(video_path):
        video_path = os.path.join(user_profile, f'{base_name}_{counter}.avi')
        counter += 1

    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(video_path, fourcc, 20.0, (640, 480))

    start_time = time.time()
    duration = 30  # seconds

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        out.write(frame)
        elapsed_time = time.time() - start_time
        if elapsed_time > duration:
            break

    # Release everything if job is finished
    cap.release()
    out.release()

if __name__ == "__main__":
    record_video_and_save()


