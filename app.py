import os
import time
import tkinter as tk
from tkinter import filedialog
import cv2 as cv
import numpy as np
import tensorflow as tf
from tensorflow import keras

# Open file selection dialog
print("<<<<<<<< Select an Image to Detect Currency >>>>>>>>")
time.sleep(2)

root = tk.Tk()
root.withdraw()
root.attributes('-topmost', True)
file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg;*.png;*.jpeg")])
root.destroy()

if not file_path:
    print("No file selected. Exiting.")
    exit()

print(f"<<<<< Selected Image: {file_path} >>>>>")
time.sleep(2)

# Load pre-trained model
model_path = "fake_currency_detector.h5"

if not os.path.exists(model_path):
    print(f"Error: Model file '{model_path}' not found! Please ensure it's in the correct directory.")
    exit()

try:
    model = keras.models.load_model(model_path, compile=False)
    print("\n<<<<<< Successfully Loaded Trained Model >>>>>> \n")
except Exception as e:
    print(f"Error loading model: {e}")
    exit()

# Process the selected image
print("<<<<<<<<< Processing Image for Prediction >>>>>>>>>>")

img_bgr = cv.imread(file_path)
img_rgb = cv.cvtColor(img_bgr, cv.COLOR_BGR2RGB)
img_resized = cv.resize(img_rgb, (224, 224))
img_array = np.array(img_resized, np.float32) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# Predict
prediction = model.predict(img_array)
predicted_class = np.argmax(prediction)
confidence = np.max(prediction)

# Denomination mapping
denomination_mapping = {
    0: "Rs. 10",
    1: "Rs. 20",
    2: "Rs. 50",
    3: "Rs. 100",
    4: "Rs. 200",
    5: "Rs. 500",
    6: "Rs. 2000",
    7: "Background"
}
denomination = denomination_mapping.get(predicted_class, "Unknown")

# Determine real/fake
if confidence > 0.5:
    label = f"Detected Currency: REAL"
    print(f"\n{label}\n")
    label_color = (0, 0, 0)  # Green
else:
    label = "Detected Currency: FAKE or UNKNOWN"
    print(f"\n{label}\n")
    label_color = (0, 0, 255)  # Red

# Display image with label
display_img = cv.resize(img_bgr, (600, 400))
cv.putText(display_img, label, (10, 40), cv.FONT_HERSHEY_SIMPLEX,
           0.9, label_color, 2, cv.LINE_AA)

cv.imshow("Currency Detection Result", display_img)
cv.waitKey(0)
cv.destroyAllWindows()

print("\n<<<<<< Thank You for using our Currency Recognition System >>>>>>")
