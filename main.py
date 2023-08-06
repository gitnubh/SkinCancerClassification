# import required libraries
from flask import Flask,render_template,request,session
from datetime import timedelta
from load import skicc_model
from tensorflow.keras.preprocessing import image
from PIL import ImageFile,Image
import os
import numpy as np

# import the model
model = skicc_model
UPLOAD_FOLDER = 'path/to/upload/folder'

app = Flask(__name__)
app.secret_key = "D6d?Cl@czfn"
app.permanent_session_lifetime = timedelta(days = 7)

# homepage
@app.route("/")
def home():
    return render_template("index.html")

# trying model page
@app.route("/tryitout" , methods = ["GET","POST"])
def tryitout():
    if request.method == "POST":
       imgfile = request.files['skicc']
        #  save the uploaded image
       if imgfile:
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        img_location = os.path.join(UPLOAD_FOLDER,imgfile.filename)
        imgfile.save(img_location)

        # Convert the file to an image array
       img = image.load_img(img_location, target_size=(299, 299))
       img = np.array(img)
       img = np.expand_dims(img, axis=0)

        # Use the model to make a prediction
       result = model.predict(img)
       predicted_class_index = np.argmax(result, axis=-1)[0]

        # Get the label name corresponding to the predicted class
       label_names = ['Benign', 'Malignant']
       predicted_label = str(label_names[predicted_class_index])
        # pass the label onto the page
       return render_template("result.html",prediction=predicted_label)
    return render_template("tryitout.html") #,prediction='Unclassified'

# run the app
if __name__=="__main__":
    app.run(debug= True)
