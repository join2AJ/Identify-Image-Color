import streamlit as st
from collections import Counter
from sklearn.cluster import KMeans
from matplotlib import colors
import matplotlib.pyplot as plt
import cv2

st.title("Image Color Analysis")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    path = "uploaded_image.jpg"
    with open(path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    image = cv2.imread(path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    def rgb_to_hex(rgb_color):
        hex_color = "#"
        for i in rgb_color:
            i = int(i)
            hex_color += ("{:02x}".format(i))
        return hex_color

    def prep_image(raw_img):
        modified_img = cv2.resize(raw_img, (900, 600), interpolation = cv2.INTER_AREA)
        modified_img = modified_img.reshape(modified_img.shape[0]*modified_img.shape[1], 3)
        return modified_img

    def color_analysis(img,b=0):
        clf = KMeans(n_clusters = 6)
        labels = clf.fit_predict(img)
        center_colors = clf.cluster_centers_
        counts = Counter(labels)
        total_pixels = sum(counts.values())
        ordered_colors = [center_colors[i] for i in counts.keys()]
        hex_colors = [rgb_to_hex(ordered_colors[i]) for i in counts.keys()]
        color_percentages = [(count/total_pixels)*100 for count in counts.values()]
        color_data = list(zip(hex_colors, color_percentages))
        color_data.sort(key=lambda x: x[1], reverse=True)
        st.write("Top colors used in the image:")
        for i, (color, percentage) in enumerate(color_data[:10]):
            color_name = colors.rgb2hex(colors.hex2color(color)).upper()
            st.write(f"{i+1}. {color_name} ({color}, {percentage:.2f}%)")


        fig, ax = plt.subplots(figsize = (12, 8))
        ax.pie(counts.values(), labels = hex_colors, colors = hex_colors)
        st.pyplot(fig)

    modified_image = prep_image(image)
    color_analysis(modified_image)
    
st.set_option('deprecation.showPyplotGlobalUse', False)
