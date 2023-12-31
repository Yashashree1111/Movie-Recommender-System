# Movie-Recommender-System
The Movie Recommender project is an machine learning project that leverages the IMDB 5000 movies dataset to provide personalized movie recommendations to users.
By analyzing movie attributes such as distribution, actors, and genres, the project utilizes advanced techniques like bag of words for vectorization and cosine distances to create a similarity matrix for each movie, enabling accurate movie-to-movie comparisons.

The project begins by extracting relevant information from the IMDB 5000 movies dataset, including details about movie distribution, actors, and genres. These attributes are then transformed into tags, representing the characteristics that define each movie. The bag of words approach is applied to convert these tags into numerical vectors, enabling efficient mathematical calculations and comparisons.

To determine the similarity between movies, the project employs cosine distances. By measuring the angle between two movie vectors, the cosine distance provides a numerical representation of their similarity. Using this technique, the project constructs a similarity matrix that captures the pairwise similarities between every movie in the dataset.
libraries used :

streamlit==0.87.0
pandas==1.3.3
requests==2.26.0

***** The code i have provided uses the TMDb API to fetch movie poster images*****
steps to get your own API key

Create a TMDb Account:
If you don't have a TMDb account, go to the TMDb website (https://www.themoviedb.org/) and sign up for a free account.

Log In:
Log in to your TMDb account using your credentials.

Request an API Key:
Once logged in, navigate to your account settings. Under the "API" section, you'll find a link to request an API key. Click on the link.

Read and Agree to Terms:
Read and understand TMDb's API terms of use. Make sure you comply with their usage policies.

Provide Information:
TMDb may ask for information about your intended use of the API. Fill out the required information accurately.

Generate API Key:
After providing the necessary information, you'll be issued an API key. This key is unique to your account and is required to make requests to the TMDb API.

### Running the App

To start the Streamlit app, run the following command:
$ streamlit run app.py

This will launch a local server and open the app in your default web browser.

OUTPUT
![Screenshot (783)](https://github.com/Yashashree1111/Movie-Recommender-System/assets/106982749/146a3241-1bc9-4225-b84d-5bd9b6e80909)

![Screenshot (784)](https://github.com/Yashashree1111/Movie-Recommender-System/assets/106982749/68a966a2-3309-4d18-b176-0e2f7c93465b)

