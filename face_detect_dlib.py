import dlib
from PIL import Image
from PIL.ExifTags import TAGS

from skimage import io


def detect_faces(image):

    # Create a face detector
    face_detector = dlib.get_frontal_face_detector()

    # Run detector and get bounding boxes of the faces on image.
    detected_faces = face_detector(image, 1)
    face_frames = [(x.left(), x.top(),
                    x.right(), x.bottom()) for x in detected_faces]

    return face_frames


def save_faces(faces, image, filepath):
    """
    Generates a new image file for each face detected in the original image
    :param faces: list of coordinates for detected faces in image
    :param image: original image
    :param filepath: original image filepath
    :return: True if all faces successfully saved to new files
    """
    print('{} faces detected! Saving now...'.format(len(faces)))

    for n, face_rect in enumerate(faces):
        face = Image.fromarray(image).crop(face_rect)

        file_type = filepath[-4:]
        new_filepath = filepath[:-4] + "_" + str(n) + file_type
        io.imsave(new_filepath, face)

        print('Saved face to {}'.format(new_filepath))

    return True


# Load image
img_path = 'static/lotza_faces.jpg'
image = io.imread(img_path)

# Detect faces
detected_faces = detect_faces(image)

# Save cropped face files
save_faces(detected_faces, image, img_path)

for (k,v) in Image.open('static/backpage_test.jpg')._getexif().items():
        print('%s = %s' % (TAGS.get(k), v))
