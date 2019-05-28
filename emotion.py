class Emotion:
    emo = ['Angry', 'Surprised','Sad', 'Happy', "Under Exposed", "Blurred", "Headwear"]
    likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                        'LIKELY', 'VERY_LIKELY')
    vision_client = vision.ImageAnnotatorClient()

    def anotatios(self,img):
        response = self.vision_client.face_detection(image=img)
        self.faces =response.face_annotations
        return self.faces

    def getSentiment(self,face):
        sentiment = [self.likelihood_name[face.anger_likelihood], self.likelihood_name[face.surprise_likelihood],
                     self.likelihood_name[face.sorrow_likelihood], self.likelihood_name[face.joy_likelihood],
                     self.likelihood_name[face.under_exposed_likelihood],
                     self.likelihood_name[face.blurred_likelihood],
                     self.likelihood_name[face.headwear_likelihood]]

        for item, item2 in zip(self.emo, sentiment):
            string = 'No sentiment'

            if not (all(item == 'VERY_UNLIKELY' for item in sentiment)):
                if any(item == 'VERY_LIKELY' for item in sentiment):
                    state = sentiment.index(
                        'VERY_LIKELY')  # 'LIKELY', 'POSSIBLE', 'UNKNOWN', 'UNLIKELY', 'VERY_LIKELY', 'VERY_UNLIKELY'
                else:
                    state = np.argmin(sentiment)

                string = self.emo[state]

            return string



