import face_recognition as fr
import os
import pickle

def get_encoded_faces():
    """
    looks through the faces folder and encodes all
    the faces

    :return: dict of (name, image encoded)
    """
    sPath = "Image Dataset/"
    encoded = {}

    # for dirpath, dnames, fnames in os.walk("./faces"):
    #     for f in fnames:
    #         if f.endswith(".jpg") or f.endswith(".png"):
    #             face = fr.load_image_file("faces/f{dnames}/" + f)
    #             encoding = fr.face_encodings(face)[0]
    #             encoded[f.split(".")[0]] = encoding
    # print(encoded)

    alldir = os.listdir(sPath)
    for name in alldir:
        afile = os.listdir(sPath + name + "/")
        for nfile in afile:
            print(nfile)
            try:
                face = fr.load_image_file(sPath + name + "/" + nfile)
                encoding = fr.face_encodings(face)[0]
                encoded[name] = encoding
            except:
                continue

    print(encoded)
    return encoded
def store_data(encoded):
    file = open("data.pkl", "wb")
    pickle.dump(encoded, file)
    file.close()

def test_load_data():
    file = open("data.pkl", "rb")
    output = pickle.load(file)
    print(output)
    file.close()

store_data(get_encoded_faces())
# get_encoded_faces()
