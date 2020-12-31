import os
from valkyrie.common.constants import PROJECT_PATH, IMG_PATH
from PIL import Image, ImageDraw
import face_recognition

def run():   
    print("Running Face Detection Demo")

    input_file = os.path.join('', *[PROJECT_PATH, IMG_PATH, "portrait_profil.JPG"])
    print(input_file)

    image = face_recognition.load_image_file(input_file)

    # # Find all facial features in all the faces in the image
    # face_landmarks_list = face_recognition.face_landmarks(image)

    # print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

    # # Create a PIL imagedraw object so we can draw on the picture
    # pil_image = Image.fromarray(image)
    # d = ImageDraw.Draw(pil_image)

    # for face_landmarks in face_landmarks_list:

    #     # Print the location of each facial feature in this image
    #     for facial_feature in face_landmarks.keys():
    #         print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

    #     # Let's trace out each facial feature in the image with a line!
    #     for facial_feature in face_landmarks.keys():
    #         d.line(face_landmarks[facial_feature], width=5)

    # # Show the picture
    # pil_image.show()
    


    # Find all the faces in the image using the default HOG-based model.
    # This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
    # See also: find_faces_in_picture_cnn.py
    face_locations = face_recognition.face_locations(image)

    print("I found {} face(s) in this photograph.".format(len(face_locations)))

    for face_location in face_locations:

        # Print the location of each face in this image
        top, right, bottom, left = face_location
        print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        # You can access the actual face itself like this:
        face_image = image[top:bottom, left:right]
        pil_image = Image.fromarray(face_image)
        pil_image.show()