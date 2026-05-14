# Note: Code 1 must be run locally to allow webcam access for face detection. It requires: pip install opencv-python

# import cv2

# def detect_faces():
#     face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#     video_capture = cv2.VideoCapture(0)

#     print("Press 'q' to quit.")

#     while True:
#         ret, frame = video_capture.read()
#         if not ret: 
#             break

#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#             cv2.putText(frame, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

#         cv2.imshow('Face Detection', frame)

#         if cv2.waitKey(1) & 0xFF == ord('q'):
#             break

#     video_capture.release()
#     cv2.destroyAllWindows()

# if __name__ == "__main__":
#     detect_faces()



#Code 2
import cv2

def detect_faces_in_image(image_path):
    # Load the pre-trained Haar Cascade
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Read the image
    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image at '{image_path}'. Make sure the file exists.")
        return

    # Convert to grayscale for detection
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(image, 'Face', (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # Save the output image
    output_filename = 'output_faces.jpg'
    cv2.imwrite(output_filename, image)
    print(f"Success! Found {len(faces)} face(s). The result has been saved as '{output_filename}'.")

if __name__ == "__main__":
    path = input("Enter the path to an image with faces (e.g., photo.jpg): ")
    detect_faces_in_image(path)