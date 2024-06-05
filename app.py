import streamlit as st  # Importing Streamlit for building the web apps
import pandas as pd  # Importing pandas for data manipulation
import requests  # Importing requests to make API calls
import pickle  # Importing pickle to load pre-saved data


# Function to recommend movies based on similarity
def recommend(movie):
    # Get the index of the movie from the DataFrame
    movie_index = movies[movies['title'] == movie].index[0]
    # Get the similarity distances for the selected movie
    distances = similarity[movie_index]
    # Sort movies based on similarity scores in descending order and select the top 5
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []  # List to store recommended movie titles
    recommended_movies_posters = []  # List to store URLs of the recommended movie posters

    for i in movies_list:
        # Get the movie ID for each recommended movie
        movie_id = movies.iloc[i[0]].movie_id
        # Append the movie title to the list of recommended movies
        recommended_movies.append(movies.iloc[i[0]].title)
        # Append the movie poster URL to the list of recommended movie posters
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters  # Return the lists of movie titles and posters


# Function to fetch movie poster using The Movie Database (TMDb) API
def fetch_poster(movie_id):
    # Make a GET request to TMDb API to get movie details
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(
            movie_id))
    # Parse the response JSON to get the poster path
    data = response.json()
    # Return the complete URL to the movie poster
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


# Load the movies dictionary from a pickle file
movies_dict = pickle.load(open('movies.pkl', 'rb'))
# Convert the dictionary to a DataFrame
movies = pd.DataFrame(movies_dict)

# Load the similarity matrix from a pickle file
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit app title
st.title('CineMatch 🎥')
# Streamlit app subtitle
st.subheader('Get recommendations for your favourite movies')

# Dropdown menu for selecting a movie
selected_movie_name = st.selectbox('🔍 Please type or select from the dropbox', movies['title'].values)

# Button to show recommendations
if st.button('Show Recommendations'):
    # Get the recommended movie titles and posters
    names, posters = recommend(selected_movie_name)

    # Create 5 columns to display the recommended movies and their posters
    col1, col2, col3, col4, col5 = st.columns(5)

    # Display the first recommended movie in the first column
    with col1:
        st.image(posters[0])
        st.write(names[0])

    # Display the second recommended movie in the second column
    with col2:
        st.image(posters[1])
        st.write(names[1])

    # Display the third recommended movie in the third column
    with col3:
        st.image(posters[2])
        st.write(names[2])

    # Display the fourth recommended movie in the fourth column
    with col4:
        st.image(posters[3])
        st.write(names[3])

    # Display the fifth recommended movie in the fifth column
    with col5:
        st.image(posters[4])
        st.write(names[4])