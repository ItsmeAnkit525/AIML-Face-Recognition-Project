import cv2
import dlib

def count_faces(image_path):
    # Load the pre-trained face detector from dlib
    detector = dlib.get_frontal_face_detector()

    # Load the image using OpenCV
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale image
    faces = detector(gray)

    # Count the number of faces detected
    num_faces = len(faces)

    # Draw rectangles around the detected faces
    for face in faces:
        x, y, w, h = face.left(), face.top(), face.width(), face.height()
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Display the image with the detected faces
    cv2.imshow("Faces", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return num_faces

# Path to the image you want to analyze
image_path = "fivepeople.jpg" 

# Call the count_faces function
face_count = count_faces(image_path)

print("Number of faces detected:", face_count)
