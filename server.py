from flask import Flask, render_template, Response
from keras.models import model_from_json  
from keras.preprocessing import image  
import numpy as np
import cv2

app = Flask(__name__)

source = "http://192.168.43.1:8080/video" # This is for video streaming from another device
#source = 0 # Uncomment this for streaming from your own pc


#load model  
model = model_from_json(open("fer.json", "r").read())  
#load weights  
model.load_weights('fer.h5')  
  
  
face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')  
  
camera = cv2.VideoCapture(source)  # use 0 for web camera
#  for cctv camera use rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' instead of camera
# for local webcam use cv2.VideoCapture(0)

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            gray_img= cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
            faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)  
        
        
            for (x,y,w,h) in faces_detected:  
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),thickness=7)  
                roi_gray=gray_img[y:y+w,x:x+h]#cropping region of interest i.e. face area from  image  
                roi_gray=cv2.resize(roi_gray,(48,48))  
                img_pixels = image.img_to_array(roi_gray)  
                img_pixels = np.expand_dims(img_pixels, axis = 0)  
                img_pixels /= 255  
        
                predictions = model.predict(img_pixels)  
        
                #find max indexed array  
                max_index = np.argmax(predictions[0])  
        
                emotions = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')  
                predicted_emotion = emotions[max_index]  
        
                cv2.putText(frame, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)  
        
            #resized_img = cv2.resize(test_img, (1000, 700))
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


@app.route('/video_feed')
def video_feed():
    #Video streaming route. Put this in the src attribute of an img tag
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host="127.0.0.1",port=1325)
