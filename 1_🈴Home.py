import streamlit as st
from PIL import Image

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
    background-image: url("https://w0.peakpx.com/wallpaper/283/832/HD-wallpaper-nfl-team-collage-football-logos-nfl-sports.jpg");
    background-size: cover;
}

.stSidebar {
    background-image: url("https://sportsposterwarehouse.com/cdn/shop/files/nfl-logos-2024-poster-25605_1024x1024.jpg?v=1726256076");
    background-size: cover;
}
</style>
'''

# Apply the custom CSS
st.markdown(page_bg_img, unsafe_allow_html=True)


# Add your Streamlit app content here
st.title("Greetings")
st.write("Welcome to the NFL Predictor, your ultimate destination for all things NFL predictions! Whether you're a seasoned bettor or a casual fan looking to enhance your game-day experience, we've got you covered with our advanced prediction tools and expert analysis.")
st.header("Navigating Our Website")
st.write("Our website is designed to be user-friendly and intuitive. Here's a quick guide to help you navigate through the various sections:")
st.subheader("Simulator")
st.write("Game Simulator: Simulate upcoming NFL matchups and customize your simulations to see different outcomes. This tool allows you to adjust various parameters to get a detailed prediction of each game.")
st.write("Playoff Predictor: Use our advanced playoff predictor to simulate different playoff scenarios and see how the playoff picture changes with each scenario.")
st.subheader("About Us")
st.write("Our Story: Learn about the history and mission of NFL Prediction Central.")
st.write("Our Team: Meet the experts and developers behind our cutting-edge prediction tools.")