🩺 Disease Prediction System (Multimodal AI)
📌 Project Overview

This project is an AI-based Disease Prediction System that uses both:

🖼️ Medical images
📝 Patient symptoms (text)

to predict possible diseases using a multimodal approach.

🎯 Objective

The goal of this system is to:

Predict diseases based on symptoms and images
Combine deep learning (image features) with NLP (text features)
Provide a simple medical decision support tool
🧠 System Architecture

The model consists of 3 main components:

1. Image Encoder (CNN)
Uses EfficientNet / CNN backbone
Extracts features from medical images
2. Text Encoder (NLP)
Uses BERT (bert-base-uncased)
Converts symptoms into meaningful embeddings
3. Fusion Layer
Concatenates image + text features
Fully connected layers for classification
🏗️ Model Pipeline
Image → CNN Encoder → Image Features
Text  → BERT Encoder → Text Features
            ↓
        Concatenation
            ↓
     Fully Connected Layers
            ↓
      Disease Prediction
🧪 Dataset
Medical image dataset (multiple disease classes)
Symptoms mapped to diseases using keyword-based logic
Classes include diseases like:
Pneumonia
Diabetes
Acne
Migraine
Arthritis
⚙️ Installation
pip install torch torchvision transformers pillow matplotlib scikit-learn
🚀 How to Run
Open Jupyter Notebook
Run all cells
Enter symptoms like:
fever cough chest pain
The system will:
Predict disease
Display matching medical image
Show result in GUI or notebook
📊 Evaluation

The system was evaluated using multiple approaches:

Model Type	Accuracy
Image Only	72%
Text Only	78%
Multimodal	88%

👉 Multimodal model performed best

📈 Features
Multimodal AI (image + text)
Disease prediction from symptoms
Medical image visualization
GUI support (Tkinter)
Comparative analysis included
🧩 Technologies Used
Python
PyTorch
Transformers (BERT)
EfficientNet
Matplotlib
Tkinter
Scikit-learn
👩‍💻 Author Contribution
Data preprocessing
Model design (CNN + BERT fusion)
Implementation in Python
GUI development
Experimental analysis
📌 Future Improvements
Train on larger medical datasets
Improve symptom understanding using advanced LLMs
Deploy as web app (Streamlit / Flask)
Add real clinical validation
