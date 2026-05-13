import os
import tkinter as tk
from PIL import Image, ImageTk

# =========================================================
# DATA
# =========================================================

folder = r"C:\Users\karen\OneDrive\Desktop\6th semester\New folder\data\images"

disease_map = {
    "Pneumonia": ["fever", "cough", "chest", "pain", "breath"],
    "Diabetes": ["sugar", "thirst", "fatigue"],
    "Acne": ["skin", "rash", "itch"],
    "Migraine": ["headache", "nausea"],
    "Arthritis": ["joint", "pain", "swelling"]
}

# =========================================================
# MODEL LOGIC
# =========================================================

def predict(symptoms):
    symptoms = symptoms.lower().split()

    best_disease = None
    best_score = -1

    for disease, keywords in disease_map.items():
        score = sum(1 for k in keywords if k in symptoms)

        if score > best_score:
            best_score = score
            best_disease = disease

    return best_disease


def get_image(disease):
    images = os.listdir(folder)

    for img in images:
        if disease.lower() in img.lower():
            return os.path.join(folder, img)

    return os.path.join(folder, images[0])


# =========================================================
# GUI LOGIC
# =========================================================

def run_prediction():
    symptoms = entry.get()

    disease = predict(symptoms)
    img_path = get_image(disease)

    result_label.config(text=f"Predicted Disease: {disease}")

    # load image
    img = Image.open(img_path).resize((300, 300))
    img = ImageTk.PhotoImage(img)

    image_label.config(image=img)
    image_label.image = img


# =========================================================
# WINDOW
# =========================================================

window = tk.Tk()
window.title("Disease Predictor")
window.geometry("500x600")

# input
entry = tk.Entry(window, width=40)
entry.pack(pady=10)

# button
btn = tk.Button(window, text="Predict", command=run_prediction)
btn.pack(pady=10)

# result
result_label = tk.Label(window, text="", font=("Arial", 14))
result_label.pack(pady=10)

# image
image_label = tk.Label(window)
image_label.pack()

window.mainloop()