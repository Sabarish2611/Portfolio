# ---- Importing Required Packages ----

from PIL import Image
import streamlit as st
from pathlib import Path
from streamlit_option_menu import option_menu
from streamlit_lottie import st_lottie


# ---- Path Settings ----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
print(current_dir)
css_file_path = current_dir / "styles" / "main.css"
resume_file_path = current_dir / "assets" / "Sabarishwaran's_Resume.pdf"
profile_pic_path = current_dir / "assets" / "pp.JPG"
sum_path = current_dir / "assets" / "sum.jpg"

# ---- General Settings ----
page_title = 'Digital Resume | Sabarishwaran G'
name = 'Sabarishwaran G'
description = 'Data Scientist, Trellix'
email = 'sabarish261101@gmail.com'
social_media = {
    'LinkedIn': 'https://www.linkedin.com/in/sabarish2611/',
    'GitHub': 'https://github.com/Sabarish2611',
    'Kaggle': 'https://www.kaggle.com/sabarish2611'
}
profile_pic = Image.open(profile_pic_path)
site_under_maintenance = Image.open(sum_path)

with open(resume_file_path, 'rb') as file:
    pdf_byte = file.read()

st.set_page_config(page_title, layout='wide')

# ---- Loading Assets ----
with open(css_file_path) as css_file:
    st.markdown("<style>{}<style>".format(
        css_file.read()), unsafe_allow_html=True)

# ---- Header Section ----
with st.container():
    col1, col2 = st.columns(2, vertical_alignment='center')

    with col1:
        with st.container():
            st.html(
                '<div style="text-align: left"> <h3> Sabarishwaran G </h3> </div>')

    with col2:
        with st.container():
            selected = option_menu(
                menu_title=None,
                options=["About", "Experience", "Projects", "Contact"],
                icons=["person", "journal-code", "code-slash", "person-add"],
                orientation="horizontal"
            )

st.markdown("#")

if selected == 'About':

    # ---- Main Section ----
    with st.container():
        col1, col2, col3, col4 = st.columns(
            [1, 2, 2, 1], gap='large', vertical_alignment='center')

    with col2:
        with st.container():
            st.image(profile_pic)

    with col3:
        with st.container():

            with st.container():
                st.html("<div style='text-align: center'> Hello, I'm </div>")
                st.html(
                    '<div style="text-align: center"> <h2> Sabarishwaran G </h2> </div>')
                st.html(
                    '<div style="text-align: center"> Data Scientist, Trellix </div>')

            st.markdown("####")

            with st.container():
                scol1, scol2, scol3, scol4 = st.columns(
                    [1, 2, 2, 1], gap='small', vertical_alignment='center')

                with scol2:
                    st.download_button(label='Download CV', data=pdf_byte,
                                       file_name=resume_file_path.name, mime='application/octet-stream')

                with scol3:
                    st.button("Contact Info")

        # links for social media
    st.markdown('#')

    # ---- About Section ----
    with st.container():
        st.html('<div style="text-align: center"> Get to know more </div>')
        st.html('<div style="text-align: center"> <h2> About Me </h2> </div>')

    st.markdown('#')

    with st.container():
        st.html('<div style="text-align: center"> As a recent BTech graduate in Artificial Intelligence from Amrita Vishwa Vidyapeetham, my journey has evolved into a Data Scientist role at Trellix, where I apply my academic knowledge to real-world cybersecurity challenges. At Trellix, my core competencies in Python and data science empower our team to innovate malware detection, analysis, and classification solutions. My tenure at Trellix has been marked by my dedication to leveraging advanced analytics and machine learning techniques to address and mitigate cyber threats. The skills honed during my time as a Graduate Technical Intern and Data Science Intern have been instrumental in contributing to the cybersecurity landscape. </div>')

    st.markdown('#')

    # ---- Education ----
    with st.container():
        st.html('<div style="text-align: center"> Explore my </div>')
        st.html('<div style="text-align: center"> <h2> Education </h2> </div>')

    st.markdown('#')

    with st.container():
        st.html('<div style="text-align: left"> ⟣ B.Tech in Artificial Intelligence, Amrita Vishwa Vidyapeetham, Coimbatore. </div>')
        st.html(
            '<div style="text-align: left"> ⟣ XII, Kamala Niketan Montessori School, Trichy. </div>')
        st.html(
            '<div style="text-align: left"> ⟣ X, kamla Niketan Montessori School, Trichy. </div>')

    st.markdown('#')

    # ---- Skills ----
    with st.container():
        st.html('<div style="text-align: center"> Explore my </div>')
        st.html('<div style="text-align: center"> <h2> Skills </h2> </div>')

    st.markdown('#')

    with st.container():
        st.html(
            '<div style="text-align: left"> ⟣ ⌨️ Programming : Python, SQL, MATLAB </div>')
        st.html(
            '<div style="text-align: left"> ⟣ 📉 Data Analysis : PowerBi, MySQL, Tableu </div>')
        st.html('<div style="text-align: left"> ⟣ ☁️ Cloud : AWS </div>')
        st.html('<div style="text-align: left"> ⟣ 📚 Statistical Analysis')
        st.html(
            '<div style="text-align: left"> ⟣ 🤖️ Artificial Intelligence : Machine Learning, Deep Learning')

    st.markdown('#')

elif selected == 'Experience':

    with st.container():

        # ---- Experience ----
        with st.container():
            st.html('<div style="text-align: center"> Explore my </div>')
            st.html('<div style="text-align: center"> <h2> Experience </h2> </div>')

        st.markdown('#')

        with st.container():
            st.html('<div style="text-align: left"> Data Scientist at Trellix </div>')
            st.html('<div style="text-align: left"> 06/2023 --> present </div>')

        st.markdown('#')

        with st.container():
            st.html(
                '<div style="text-align: left"> Data Science Intern at Trellix </div>')
            st.html('<div style="text-align: left"> 03/2023 --> 06/2023 </div>')

        st.markdown('#')

        with st.container():
            st.html(
                '<div style="text-align: left"> Software Development Engineer Intern at Trellix </div>')
            st.html('<div style="text-align: left"> 01/2023 --> 03/2023 </div>')

        st.markdown('#')

        with st.container():
            st.html(
                '<div style="text-align: left"> Computational Linguist at PanLingua </div>')
            st.html('<div style="text-align: left"> 05/2021 --> 08/2021 </div>')

        st.markdown('#')

elif selected == 'Projects':

    with st.container():

        col1, col2, col3 = st.columns(
            [1, 2, 1], vertical_alignment='center', gap='large')

        with col2:
            with st.container():
                st.image(site_under_maintenance, use_column_width=True)

elif selected == 'Contact':

    with st.container():

        col1, col2, col3 = st.columns(
            [1, 2, 1], vertical_alignment='center', gap='large')

        with col2:
            with st.container():
                st.image(site_under_maintenance, use_column_width=True)
