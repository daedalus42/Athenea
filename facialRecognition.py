
class FacialRecognition:
    modelo = None
    names= ["miriam","pol","willy"]
    dir_img= 'faces'
    face_cascade = cv2.CascadeClassifier(classifier)
    facePoints =()
    prediction=[]
    img=None

    def entrenarModelo(self):
        images = []
        labels = []
        label = 0
        for dir in os.listdir(self.dir_img):
            self.names.append(dir)
            pathTemporal = self.dir_img+"/"+dir
            for file in os.listdir(self.dir_img+"/"+dir):
                    path_img = pathTemporal+"/"+file
                    img = cv2.imread(path_img,0)
                    images.append(img)
                    labels.append(int(label))
            label = label+1
        (images, labels) = [np.array(lis) for lis in [images, labels]]

        self.modelo = cv2.face.LBPHFaceRecognizer_create()
        self.modelo.train(images, labels)
        self.model.save("model.xml")

    def saveModel(self):
        self.modelo =  cv2.face.LBPHFaceRecognizer_create()
        self.modelo.read("model.xml")

    def detecionFacial(self,img):
        self.img=img
        self.facePoints = self.face_cascade.detectMultiScale(img, 1.3, 5)
        return self.facePoints !=()

    def reconocimientoFacial_(self):
        self.prediction =[]
        for points in self.facePoints:
            (x, y, w, h) = [v for v in points]
            face = self.img[y:y + h, x:x + w]
            self.prediction.append(self.modelo.predict(face))

    def reconocimientoFacial(self,im):
        self.prediction =[]
        #for points in self.facePoints:
        #(x, y, w, h) = [v for v in self.facePoints[i]]
        #face = self.img[y:y + h, x:x + w]
        return self.modelo.predict(im)

    def getName(self ,id):
        return '%s' % (self.names[id])

