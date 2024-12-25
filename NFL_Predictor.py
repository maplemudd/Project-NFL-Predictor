import streamlit as st
from streamlit_option_menu import option_menu


st.set_page_config(page_title="Dipping In the Pool", layout="wide")


    
# Custom CSS to set the background image
page_bg_img = '''
<style> 
.stApp {
    background-image: url("https://wwwimage-us.pplusstatic.com/base/files/blog/61/65/83/1ee6710b-3a00-4613-aa61-a0af909b5dbd.jpg");
    background-size: cover;
}

.stAppHeader {
    background-color: rgba(0,0,0,0);
}

.stToolbar {
    right: 2rem;
}

.stSidebar {
    background-image: url("https://w0.peakpx.com/wallpaper/283/832/HD-wallpaper-nfl-team-collage-football-logos-nfl-sports.jpg");
    background-size: cover;
}
</style>
'''

# Apply the custom CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Add your Streamlit app content here
