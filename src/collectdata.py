import cv2
import os

directory = r'C:\Users\xxcbj\Desktop\Sign_language_detection\Data'
print(f"Current working directory: {os.getcwd()}")

# Create main directory if it doesn't exist
if not os.path.exists(directory):
    os.mkdir(directory)
    print(f"Created main directory: {directory}")

# Create subdirectories if they don't exist
subdirectories = ['sample_variable_bg'] + [chr(i) for i in range(65, 91)]
for subdir in subdirectories:
    subdir_path = os.path.join(directory, subdir)
    if not os.path.exists(subdir_path):
        os.mkdir(subdir_path)
        print(f"Created subdirectory: {subdir_path}")

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Camera not opened")
else:
    print("Camera successfully opened")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: Failed to capture frame")
        break
    
    count = {subdir: len(os.listdir(os.path.join(directory, subdir))) for subdir in subdirectories}
    
    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame, (0, 40), (300, 300), (255, 255, 255), 2)
    cv2.imshow("data", frame)
    roi_frame = frame[40:300, 0:300]
    cv2.imshow("ROI", roi_frame)
    gray_frame = cv2.cvtColor(roi_frame, cv2.COLOR_BGR2GRAY)
    resized_frame = cv2.resize(gray_frame, (48, 48))
    interrupt = cv2.waitKey(10)
    
    # Save the frame when a corresponding key is pressed
    for subdir in subdirectories:
        if len(subdir) == 1:  # Handle only single character subdirectories
            if interrupt & 0xFF == ord(subdir.lower()):
                file_path = os.path.join(directory, subdir, f'{count[subdir]}.jpg')
                cv2.imwrite(file_path, resized_frame)
                print(f"Saved image to {file_path}")
    
    # Save sample variable background frame
    if interrupt & 0xFF == ord('.'):
        file_path = os.path.join(directory, 'sample_variable_bg', f'{count["sample_variable_bg"]}.jpg')
        cv2.imwrite(file_path, resized_frame)
        print(f"Saved sample variable background image to {file_path}")
    
    # Exit on '7' key press
    if interrupt & 0xFF == ord('7'):
        print("Exiting...")
        break

cap.release()
cv2.destroyAllWindows()
