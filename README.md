# CineMatch - A Streamlit App for Movie Recommendations

![#USER-INTERFACE](https://github.com/arnav-singh-ahlawat/CineMatch/assets/159664776/02686d14-8838-4c79-84c2-0100321873e1)

## Overview:

CineMatch is a Streamlit web application that recommends movies similar to a selected movie from the 'TMDB 5000 Movie Dataset'. Users can either type in the movie name in the search box or select a movie from the drop-down menu to get recommendations.

## Video Demo:

https://github.com/arnav-singh-ahlawat/CineMatch/assets/159664776/3bd16d1b-2154-4843-9b31-9c7871095053

## Features:

**Movie Search:** Search for a movie by typing its name.

**Drop-down Selection:** Select a movie from a drop-down list.

**Recommendations:** Get a list of movies similar to the selected movie.

**Movie Posters:** View posters of recommended movies fetched from TMDB.

## Getting Started:

**Prerequisites:** Ensure you have Python installed on your machine. You'll also need to install the necessary libraries. You can do this by running "pip install -r requirements.txt".

**Cloning the Repository** Clone the repository by using the git command - "git clone https://github.com/arnav-singh-ahlawat/CineMatch.git" in your project directory.

**Downloading and Initializing Large Files** The similarity.pkl file, which is over 100MB in size, needs to be handled with Git Large File Storage (LFS). Initialize Git LFS in your project directory or download the file manually:

1. Initialize Git LFS:

	git lfs install<br>
	git lfs pull

2. Manual Download:

	Download the similarity.pkl file from: https://github.com/arnav-singh-ahlawat/CineMatch/blob/master/similarity.pkl

## Run the App:

Navigate to the project directory in your terminal and execute "streamlit run app.py". This will launch the CineMatch web application in your default browser.

## Usage:

Once the Streamlit app is running, you can access it through your web browser.

**Search for a Movie:** Type the name of a movie in the search box to get recommendations.

**Select from Drop-down:** Choose a movie from the drop-down list to get recommendations.

**View Recommendations:** The app will display a list of movies similar to the selected movie along with their posters.
 
## Data and Model:

**TMDB 5000 Movie Dataset:** Used for movie data and metadata. Can be found at: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

**Pandas:** For data manipulation.

**Scikit-learn:** For creating text-vectors of movie-tags.

**Pickle:** To save and load pre-processed data.

**Requests:** To make API calls to TMDB for fetching movie posters.

**Streamlit:** For designing the user-interface.

## Future Enhancements:

**User Ratings:** Incorporate user ratings to improve recommendation accuracy.

**Genre Filtering:** Add functionality to filter recommendations by genre.

**Enhanced UI:** Improve the user interface for a better user experience.

## Acknowledgements:

**TMDB:** For providing the movie dataset.

**Kaggle:** For hosting the dataset.

**Streamlit:** For the web application framework.

**Scikit-learn:** For machine learning tools.