import streamlit as st
import util

def app():
    st.image('./Untitled design (1).gif', use_column_width=True)
    st.write("Upload a Picture to see if it is a fake or real face.")
    st.markdown('*Need an image to test? Visit this [link]("https://www.kaggle.com/datasets/awsaf49/artifact-dataset")*')
    file_uploaded = st.file_uploader("Choose the Image File", type=["jpg", "png", "jpeg"])
    if file_uploaded is not None:
        res = util.classify_image(file_uploaded)
        c1, buff, c2, c3 = st.columns([2, 0.5, 2, 2])
        c1.image(file_uploaded, use_column_width=True)
        c2.subheader("Classification Result")
        c2.write("The image is classified as **{}**.".format(res['label'].title()))
        c3.subheader("Probability")
        c3.write("Probability of being **{}**: {:.2f}%".format(res['label'].title(), res['probability']))

if __name__ == "__main__":
    app()
st.write("""
    ### About this App
    This web application uses a machine learning model to classify images as fake or real. It's part of a project aimed at detecting manipulated or generated images to combat misinformation.

    Feel free to navigate between pages, upload images, and explore the app!
""")
# Display footer image
footer_image_path = './images.png'
st.image(footer_image_path, caption="scit", width=1000)

# Add the footer to your app with an image
footer_content = """
<div class="footer">Your footer content goes here</div>

"""
st.markdown(footer_content, unsafe_allow_html=True)
