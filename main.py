from flask import Flask, render_template, request
import cv2
import numpy as np

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Get uploaded image
    file = request.files['image']
    if not file:
        return 'No file uploaded', 400

    # Read image
    img = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Convert image to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Reshape the image to 2D array of pixels
    pixels = img_rgb.reshape((-1, 3))

    # Convert to float32
    pixels = np.float32(pixels)

    # Define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
    K = 5
    _, labels, centroids = cv2.kmeans(pixels, K, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Convert centroids back to uint8
    centroids = np.uint8(centroids)

    # Find counts of each label
    label_counts = np.bincount(labels.flatten())

    # Get most common colors
    most_common_colors = centroids[np.argsort(label_counts)[-5:]]

    # Convert colors to hex format
    hex_colors = ['#' + ''.join(f'{c:02x}' for c in color) for color in most_common_colors]

    return render_template('result.html', colors=hex_colors)

if __name__ == '__main__':
    app.run(debug=True)
