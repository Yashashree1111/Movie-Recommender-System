# Movie-Recommender-System
The Movie Recommender project is an machine learning project that leverages the IMDB 5000 movies dataset to provide personalized movie recommendations to users.
By analyzing movie attributes such as distribution, actors, and genres, the project utilizes advanced techniques like bag of words for vectorization and cosine distances to create a similarity matrix for each movie, enabling accurate movie-to-movie comparisons.

The project begins by extracting relevant information from the IMDB 5000 movies dataset, including details about movie distribution, actors, and genres. These attributes are then transformed into tags, representing the characteristics that define each movie. The bag of words approach is applied to convert these tags into numerical vectors, enabling efficient mathematical calculations and comparisons.

To determine the similarity between movies, the project employs cosine distances. By measuring the angle between two movie vectors, the cosine distance provides a numerical representation of their similarity. Using this technique, the project constructs a similarity matrix that captures the pairwise similarities between every movie in the dataset.

The website interface of the project allows users to input a movie of their choice. Upon receiving the input, the system computes the cosine distances between the selected movie and all other movies in the dataset. Based on the calculated distances, the project identifies the most similar movies and presents them as recommendations to the user. These recommendations are tailored to the user's preferences, providing a personalized movie discovery experience.
