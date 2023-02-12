# Image Color Analysis App

This is a Python Streamlit app that takes an image as input from the user, analyzes the colors in the image, and displays the results.

## Usage

1. Choose an image file to upload using the file upload widget.
2. Click the "Analyze" button to perform color analysis on the image.
3. The app will display the top colors used in the image, along with the percentage of each color used and the color name.

## Program

The program uses the following Python packages:

- `collections`
- `sklearn.cluster`
- `matplotlib.colors`
- `matplotlib.pyplot`
- `cv2`

The program consists of the following steps:

1. Load the image from the specified file path.
2. Convert the image from BGR to RGB color space.
3. Resize and reshape the image to prepare it for color analysis.
4. Perform color analysis using KMeans clustering.
5. Determine the top colors used in the image and their percentage of usage.
6. Display the top colors used in the image, along with their percentage of usage and color name.

## Future Improvements

In the future, we might consider adding the ability to save the color analysis report as a PDF or image file. We might also explore more sophisticated methods for color analysis, such as deep learning models that can detect subtle variations in color and texture.

<a href="https://www.buymeacoffee.com/join2aj" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 60px !important;width: 217px !important;" ></a>
