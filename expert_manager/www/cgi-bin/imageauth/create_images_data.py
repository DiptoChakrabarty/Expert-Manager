import cv2
import numpy as np
import os

f=open('profiles','w')
f.write('')
f.close()

def write_profile_in_file(dir_path):
    f=open('profiles','a')
    f.write('{}.h5\n'.format(dir_path))
    f.close()




no_face=int(input("enter number faces would you want to train in database"))


# Load HAAR face classifier
face_classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


# Load functions

def model(dir_path):
    # pip3 install  opencv-contrib-python
    import cv2
    import numpy as np
    from os import listdir
    from os.path import isfile, join
    # Get the training data we previously made
    data_path = '{}/'.format(dir_path)
    # a=listdir('d:/faces')
    # print(a)
    # """
    onlyfiles = [f for f in listdir(data_path) if isfile(join(data_path, f))]

    # Create arrays for training data and labels
    Training_Data, Labels = [], []

    # Open training images in our datapath
    # Create a numpy array for training data
    for i, files in enumerate(onlyfiles):
        image_path = data_path + onlyfiles[i]
        images = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        Training_Data.append(np.asarray(images, dtype=np.uint8))
        Labels.append(i)
    # 
    # Create a numpy array for both training data and labels
    Labels = np.asarray(Labels, dtype=np.int32)
    model=cv2.face_LBPHFaceRecognizer.create()
    # Initialize facial recognizer
    # model = cv2.face_LBPHFaceRecognizer.create()
    # model=cv2.f
    # NOTE: For OpenCV 3.0 use cv2.face.createLBPHFaceRecognizer()

    # Let's train our model 
    model.train(np.asarray(Training_Data), np.asarray(Labels))
    #    print("Model trained sucessefully")
    model.save('{}.h5'.format(dir_path))


def face_extractor(img):
    # Function detects faces and returns the cropped face
    # If no face detected, it returns the input image
    
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
    
    if faces is ():
        return None
    
    # Crop all faces found
    for (x,y,w,h) in faces:
        cropped_face = img[y:y+h, x:x+w]

    return cropped_face

for i in range(no_face):
    dir_path='profile'+str(i+1)
    os.system("mkdir {}".format(dir_path))
    write_profile_in_file(dir_path)


    # Initialize Webcam
    cap = cv2.VideoCapture(0)
    count = 0

    # Collect 100 samples of your face from webcam input
    while True:

        ret, frame = cap.read()
        if face_extractor(frame) is not None:
            count += 1
            face = cv2.resize(face_extractor(frame), (200, 200))
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)

            # Save file in specified directory with unique name
            file_name_path = '{}/face'.format(dir_path) + str(count) + '.jpg'
            cv2.imwrite(file_name_path, face)

            # Put count on images and display live count
            cv2.putText(face, str(count), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
            cv2.imshow('Face Cropper', face)
            
        else:
            pass

        if cv2.waitKey(1) == 13 or count == 50: #13 is the Enter Key
            break
            
    cap.release()
    cv2.destroyAllWindows() 
    model(dir_path)     
    print("Please train another face it is waiting for 10 seconds")
