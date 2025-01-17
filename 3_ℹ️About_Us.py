import streamlit as st

page_bg_img = '''
<style> 
.stApp {
    background-image: url("https://wwwimage-us.pplusstatic.com/base/files/blog/61/65/83/1ee6710b-3a00-4613-aa61-a0af909b5dbd.jpg");
    background-size: cover;
}

.stAppHeader {
    background-color: rgba(0,0,0,0);
}
.stSidebar {
    background-image: url("https://sportsposterwarehouse.com/cdn/shop/files/nfl-logos-2024-poster-25605_1024x1024.jpg?v=1726256076");
    background-size: cover;
}
</style>
'''
team_logos = {
    
    
}
# Apply the custom CSS
st.markdown(page_bg_img, unsafe_allow_html=True)

# Add your Streamlit app content here

st.title("About Us, Our Mission and How It Works!")
st.header("Introduction")
st.write("Welcome to the NFL Prediction Website! Here, you can find predictions and insights for upcoming NFL games.")

# Sub-section header
st.subheader("How It Works")
st.write("Our predictions are based on advanced statistical models and historical data which is then used the . Here's how you can use our app:")
st.write("Just select your team and their opponent to quickly discover the most likely team to win their game!")
# Another section header
st.header("Mission Statement")
st.write("At NFL Predictor, our mission is to provide football fans with accurate, data-driven predictions and insights to enhance their understanding and enjoyment of the NFL. We strive to deliver comprehensive analysis, expert opinions, and up-to-date information to help you stay ahead of the game. Whether you're a seasoned bettor or a casual fan, our goal is to be your go-to resource for all things NFL.")

# Using markdown for headers
st.markdown("## Warning for Betting")
st.write("While we aim to provide the most accurate predictions possible, it's important to remember that sports betting involves a high degree of risk. Our predictions are based on statistical models and historical data, but they are not guarantees of future outcomes. Always bet responsibly and within your means. If you or someone you know has a gambling problem, please seek help from a professional organization.")
