"""
2.  Build a mini movie recommendation app using Streamlit that shows 5 trending Bollywood movies
   (hardcoded list) with their posters and a short description, then upload your project files to
    Hugging Face Spaces and deploy your app online.<br><br><em><strong>Hint:</strong> Use st.image()
    and st.write() in Streamlit to display images and text.</em>
"""
import streamlit as st

st.set_page_config(
    page_title="Bollywood Movie Recommendations",
    page_icon=""
)

st.title("Bollywood Movie Recommendations")

st.write("Here are 5 popular Bollywood movies you can watch:")

movies = [
    {
        "name": "3 Idiots",
        "poster": "https://upload.wikimedia.org/wikipedia/en/d/df/3_idiots_poster.jpg",
        "description": "A comedy-drama about friendship, college life and following your dreams."
    },
    {
        "name": "Dangal",
        "poster": "https://upload.wikimedia.org/wikipedia/en/9/99/Dangal_Poster.jpg",
        "description": "A sports drama based on a father training his daughters to become wrestlers."
    },
    {
        "name": "Zindagi Na Milegi Dobara",
        "poster": "https://upload.wikimedia.org/wikipedia/en/1/17/Zindagi_Na_Milegi_Dobara.jpg",
        "description": "Three friends go on a road trip and learn important lessons about life."
    },
    {
        "name": "Queen",
        "poster": "https://upload.wikimedia.org/wikipedia/en/4/45/QueenMoviePoster7thMarch.jpg",
        "description": "A young woman discovers confidence and independence during a solo trip."
    },
    {
        "name": "Taare Zameen Par",
        "poster": "https://upload.wikimedia.org/wikipedia/en/b/b6/Like_Stars_on_Earth_poster.jpg",
        "description": "A teacher helps a child understand his unique abilities and potential."
    }
]

for movie in movies:
    st.subheader(movie["name"])

    st.image(movie["poster"], width=200)

    st.write(movie["description"])

    st.divider()