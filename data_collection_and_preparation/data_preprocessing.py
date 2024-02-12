import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from PIL import Image
import os

# Function to preprocess textual descriptions
def preprocess_text(text):
    # Tokenize text
    tokens = word_tokenize(text)
    # Remove stopwords
    stopwords_list = set(stopwords.words('english'))
    filtered_tokens = [token.lower() for token in tokens if token.isalnum() and token.lower() not in stopwords_list]
    return ' '.join(filtered_tokens)

# Function to preprocess images
def preprocess_image(image_path):
    # Load image
    img = Image.open(image_path)
    # Resize image
    img = img.resize((224, 224))  # Example size for input to pre-trained CNN models
    # Convert image to numpy array
    img_array = np.array(img)
    # Normalize pixel values
    img_array = img_array / 255.0
    return img_array

if __name__ == "__main__":
    # Load scraped data from CSV file
    data = pd.read_csv('scraped_data.csv')

    # Preprocess textual descriptions
    data['clean_description'] = data['description'].apply(preprocess_text)

    # Preprocess images
    image_folder = 'image_data'
    os.makedirs(image_folder, exist_ok=True)
    for i, row in data.iterrows():
        image_path = os.path.join(image_folder, f'image_{i}.jpg')
        img = Image.open(requests.get(row['image_url'], stream=True).raw)
        img.save(image_path)
        data.at[i, 'image_path'] = image_path
        preprocessed_image = preprocess_image(image_path)
        np.save(f'image_{i}.npy', preprocessed_image)

    # Save preprocessed data
    data.to_csv('preprocessed_data.csv', index=False)
