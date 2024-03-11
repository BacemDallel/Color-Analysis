# Image Colour Palette

This is a web application built with Flask that analyzes uploaded images and finds the most common colors in them. It uses the k-means clustering algorithm for color analysis.

## Installation

1. Clone the repository to your local machine:
git clone <repository_url>

css
Copy code

2. Navigate to the project directory:
cd Image_Colour_Palette

arduino
Copy code

3. Install the required dependencies using pip:
pip install -r requirements.txt

markdown
Copy code

## Usage

1. Run the Flask application:
python main.py

markdown
Copy code

2. Open your web browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).

3. Upload an image using the provided form and click "Upload Image".

4. The application will analyze the image and display the most common colors found in it.

5. You can upload another image by clicking "Upload Another Image".

## Dependencies

- Flask==2.0.2
- opencv-python==4.5.3.56
- numpy==1.21.2
