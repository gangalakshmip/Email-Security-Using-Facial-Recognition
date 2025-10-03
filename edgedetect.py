import cv2

# Open the default camera
cap = cv2.VideoCapture(0)  # Use 0 for the default camera, or replace with a video file path

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open the camera.")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If the frame was not captured properly, break the loop
    if not ret:
        print("Error: Failed to capture frame.")
        break

    # Convert the frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply the Canny edge detection algorithm
    edges = cv2.Canny(gray_frame, 100, 200)

    # Display the original frame
    cv2.imshow("Original Video", frame)

    # Display the edges
    cv2.imshow("Edge Detection", edges)

    # Exit the loop when the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
