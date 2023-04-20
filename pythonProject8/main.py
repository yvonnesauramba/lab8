import cv2

# Load the image
img = cv2.imread('images/variant-10.jpg')

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# Apply adaptive threshold
thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY, 11, 2)

# Show the binary image
cv2.imshow('Binary image', thresh)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Open the camera
cap = cv2.VideoCapture(0)

# Loop over frames
while True:
    # Read a frame
    ret, frame = cap.read()

    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # Apply adaptive threshold
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)


    # Show the frame
    cv2.imshow('Frame', frame)

    # Check if the label falls into a 150x150 square in the center of the frame
    height, width, _ = frame.shape
    x = int((width - 150) / 2)
    y = int((height - 150) / 2)
    if thresh[y:y+150, x:x+150].sum() == 0:
        # Flip the frame
        frame = cv2.flip(frame, 1)

    # Wait for a key press
    key = cv2.waitKey(1) & 0xFF

    # Exit if the 'q' key is pressed
    if key == ord('q'):
        break


# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
