from fastapi import FastAPI, File, UploadFile, middleware
import uvicorn
import tensorflow as tf
import numpy as np
from io import BytesIO
from PIL import Image
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost:3000",
]

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)

@app.get('/')
def welcome():
    return "Api is working"

def image_array(data)-> np.array:
    return np.array(Image.open(BytesIO(data)))

classifier = tf.keras.models.load_model(r"E:\Projects\Potato_Diesease\saved_models\potatoes.h5")
class_names = ["Early Blight", "Late Blight", "Healthy"]

@app.post('/predict')
async def predict(file: UploadFile = File(...)):
        image = image_array(await file.read())
        image_batch = np.expand_dims(image,0)
        prediction = classifier.predict(image_batch)
        class_name = class_names[np.argmax(prediction[0])]
        class_probability = np.max(prediction[0])
        return {
        'class': class_name,
        'confidence': float(class_probability)
    }

if __name__ == "__main__":
    uvicorn.run(app, host = 'localhost', port = 8000)

#uvicorn app:app --reload 