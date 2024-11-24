import streamlit as st
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie
from PIL import Image, ImageDraw
import io
import base64
from io import BytesIO
import requests

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

st.set_page_config(layout= 'wide')

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coder_animation = load_lottieurl("https://lottie.host/9acb081d-cb9d-4373-a1c5-b8ffe4b310d3/u2rBdboGcy.json")
lottie_mlproject_animation = load_lottieurl("https://lottie.host/13a741a1-6640-465d-b730-a70323beaf93/jZqqavkjOm.json")
lottie_proj2_animation = load_lottieurl("https://lottie.host/0e508301-8d56-49a7-a452-64e73c2d425f/3xzY6hi2bY.json")
lottie_ocr_animation = load_lottieurl("https://lottie.host/5d50cd8c-bad2-446b-813f-a33bc4d0eaef/lYRRWEobWh.json")

with st.container():
    col1, col2 = st.columns(2)
    
    with col1:
        st.write("##")
        st.title("Tanay's Portfolio")
        st.subheader("Hey guys!")

        st.write("""Greetings, Earthlings! I'm Tanay, your friendly neighborhood data scientist, embarking on a journey through the realms of Data Science, Machine Learning, Natural Language Processing, Computer Vision, and Deep Learning.
                 Seeking out challenges that are as thrilling as a roller coaster ride through a quantum wormhole, I'm here to contribute my skills to the ever-expanding universe of knowledge.""")
    
    with col2:
        def round_image(image_path, size=100):
            image = Image.open(image_path)
            image = image.resize((size, size))
            mask = Image.new("L", (size, size), 0)
            draw = ImageDraw.Draw(mask)
            draw.ellipse((0, 0, size, size), fill=255)
    
            image.putalpha(mask)
    
            # Display the image with HTML/CSS for right alignment
            st.markdown(
            f'<div style="float: right; margin-left: 10px; margin-right: 100px;"><img src="data:image/png;base64,{image_to_base64(image)}"></div>',
            unsafe_allow_html=True
            )
    
        image_path = "images/Profile_Image.jpg"
        round_image(image_path, size=300)

with st.container():
    selected = option_menu(
        menu_title= None,
        options= ["About", "Projects", "Contact"],
        icons= ['person', 'code-slash', 'chat-left-text-fill'],
        orientation= 'horizontal'
    )

if selected == "About":
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.write("##")
                st.subheader("You must be wondering, 'Who is this handsome man !?'")
                st.title("I'm a Graduate Student at Stony Brook University")
                text = '<span style="color: #663399; font-weight: bold;">But do not let the macho countenance distract you!<br>My brain\'s even more fascinating 😉</span>'
                st.markdown(text, unsafe_allow_html=True)
                st.subheader("Education")
                st.write(
                    "\n:books: MS in Data Science\n"
                    "\n:school: SUNY Stony Brook University\n"
                    "\n:clock1: Expected May 2026\n"
                )
                # Add a line break using markdown
                st.markdown("<br>", unsafe_allow_html=True)
                st.write(
                    "\n\n:books: B.Tech in Computer Science and Engineering\n"
                    "\n:school: Charotar University of Science and Technology\n"
                    "\n:clock1: June 2020 - May 2024\n"
                    "\n:mortar_board: CGPA: 9.69/10"
                )
                
            with col2:
                # Check if lottie_coder_animation is not None before using it
                if lottie_coder_animation is not None:
                    st_lottie(lottie_coder_animation)
                else:
                    st.write("Error loading Lottie animation.")
        st.write("---")

        with st.container():
            col3, col4 = st.columns(2)
            with col3:
                st.subheader("EXPERIENCE\n")
                st.subheader("""
        **3Fit Pvt. Ltd.**\n
        ~ Duration: May'22 - June'22\n
        ~ Role: Backend Developer Intern\n
        ~ Responsibilities:\n
            1. Designed a web portal using wagtail CMS (Content Management System) 
               and PostgreSQL database to make web pages extraordinarily dynamic.
            2. Simplified the process of changing the content that appears on web pages 
               with only a few clicks and the appropriate responsibilities and permissions.
    """)
            with col4:
                st.subheader("""
                    IT By Design\n
                    ~ Duration: June'23 - December'23\n
                    ~ Role: Software Developer Intern\n
                    ~ Responsibilities:\n
                             1. Played a pivotal role in the development of an innovative chatbot by leveraging the OpenAI API. 
                           This initiative not only showcased my technical expertise but also underscored my ability to 
                           implement cutting-edge solutions to enhance user experiences.
                        2. Demonstrated strong problem-solving skills by enhancing security and user experience through 
                           the manipulation of the backend system. Successfully limited access to the chatbot to authorized 
                           users with specific roles and responsibilities, ensuring data integrity and privacy.
                        3. Played a vital role in the comprehensive testing process encompassing production, test, and 
                           development stages during the critical phase of product launch. My contributions were instrumental 
                           in ensuring the product's quality and performance, reinforcing its success in the market.
                    """)
                
if selected == "Projects":
    with st.container():
        col5, col6 = st.columns(2)
        with col5:
            st.subheader("""Rectangular Transform Neural Network (RTNN)""")
            st.markdown("""
Conducted innovative research in the field of machine learning and deep learning, focusing on developing an optimized neural network architecture named Rectangular Transform Neural Network (RTNN). This project aimed to address inefficiencies in conventional convolutional neural networks (CNNs), particularly in high-dimensional data processing.<br>
<br>Key contributions and outcomes include:<br>
1.	Pioneering the RTNN Architecture:<br>
-	Designed and implemented RTNN to significantly accelerate convolution operations while preserving the integrity of feature extraction.<br>
-	Leveraged advanced mathematical concepts, including calculus and matrix transformations, to enhance the model’s efficiency and scalability.<br>
2.	Groundbreaking Performance Improvements:<br>
-	Achieved a remarkable 7x reduction in processing time for analyzing 87,000 ECG samples from the MIT-BiH dataset.<br>
-	Optimized processing time from 37.7 seconds to just 5.6 seconds, demonstrating exceptional efficiency gains in computational performance.<br>
""",unsafe_allow_html=True)
        with col6:
            # Check if lottie_coder_animation is not None before using it
                if lottie_coder_animation is not None:
                    st_lottie(lottie_mlproject_animation)
                else:
                    st.write("Error loading Lottie animation.")
        col7, col8 = st.columns(2)
        with col7:
            # Check if lottie_coder_animation is not None before using it
                if lottie_coder_animation is not None:
                    st_lottie(lottie_proj2_animation)
                else:
                    st.write("Error loading Lottie animation.")
        with col8:
            st.subheader("Fake News Detection using RoBERTa and LSTM Model")
            st.markdown("""
Engineered a sophisticated text classification model tailored for discerning between authentic and misleading news articles. 
Harnessing state-of-the-art Natural Language Processing (NLP) techniques, our solution ensures unparalleled accuracy and precision.

Key Achievements:
- Deployed Long Short-Term Memory (LSTM) layers, coupled with advanced word embedding, to enable nuanced and context-aware text analysis.
- Delivered an exceptional 91% accuracy in the identification of deceptive news articles, showcasing our commitment to precision.
- Evaluated model efficacy using industry-standard metrics, including the LSTM model's accuracy and F1 score.
- Conducted extensive training on a meticulously curated dataset of labeled news articles, fine-tuning our model for real-world scenarios.
- Uncovered intricate linguistic patterns, empowering our model to excel in classifying nuanced textual cues.

""", unsafe_allow_html=True)
        
        col9, col10 = st.columns(2)
        with col9:
            st.subheader("Smart Marksheet Scanner using OCR for ACPDC")
            st.markdown("""
Led the development of a cutting-edge OCR (Optical Character Recognition) Model 
for ACPDC Department, focused on extracting student marks from digital mark sheets.

Key Achievements:
- Secured 4th place in the prestigious National level Azadi ka Amrit Mahotsav Hackathon.
- Deployed a state-of-the-art OCR system, complemented by Regex and trained on an extensive 
    dataset of actual marksheets, achieving a remarkable 100% accuracy.
- Implemented a sophisticated 3-step verification algorithm to ensure precise extraction of 
    marks from mark sheets, demonstrating a commitment to data accuracy.
- Employed Dash for in-depth analysis post-scanning, providing academic counsellors with detailed 
    insights to guide students and facilitate academic improvement.

Our innovative solution seamlessly combines OCR technology, regex, and advanced algorithms, delivering
 unparalleled accuracy and actionable insights for academic counseling.
""", unsafe_allow_html=True)
        with col10:
            # Check if lottie_coder_animation is not None before using it
                if lottie_coder_animation is not None:
                    st_lottie(lottie_ocr_animation)
                else:
                    st.write("Error loading Lottie animation.")

if selected == "Contact":
     st.header("Get in touch and let\'s collaborate! :handshake:")
     st.write("##")
     st.write("##")

     st.markdown("""
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background-color: #f4f4f4;
        }

        form {
            max-width: 400px;
            margin: 50px auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 10px;
            box-shadow: 0px 0px 10px 0px rgba(0, 0, 0, 0.1);
        }

        input,
        textarea {
            width: 100%;
            margin-bottom: 15px;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 5px;
            display: block; /* Align elements vertically */
        }

        textarea {
            resize: vertical; /* Allow vertical resizing of the textarea */
        }

        button {
            background-color: #3498db;
            color: #fff;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            cursor: pointer;
            box-shadow: 0px 0px 5px 0px rgba(0, 0, 0, 0.3);
        }

        button:hover {
            background-color: #267bb6;
        }
    </style>
    <form action="https://formsubmit.co/tanaydeo2403@gmail.com" method="POST" style="background-color: #121212; color: #ffffff; padding: 20px; border-radius: 10px; font-family: Arial, sans-serif;">
    <input type="hidden" name="_captcha" value="false">

    <label for="name" style="display: block; margin-bottom: 5px;">Your Name</label>
    <input type="text" id="name" name="name" required style="width: 100%; padding: 10px; margin-bottom: 15px; background-color: #1e1e1e; color: #ffffff; border: 1px solid #333; border-radius: 5px;">

    <label for="email" style="display: block; margin-bottom: 5px;">Your Email</label>
    <input type="email" id="email" name="email" required style="width: 100%; padding: 10px; margin-bottom: 15px; background-color: #1e1e1e; color: #ffffff; border: 1px solid #333; border-radius: 5px;">

    <label for="message" style="display: block; margin-bottom: 5px;">Your Message</label>
    <textarea id="message" name="message" placeholder="Your message" required style="width: 100%; padding: 10px; margin-bottom: 15px; background-color: #1e1e1e; color: #ffffff; border: 1px solid #333; border-radius: 5px;"></textarea>

    <button type="submit" style="background-color: #333; color: #ffffff; padding: 10px 15px; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">Send</button>
    </form>
""", unsafe_allow_html=True)