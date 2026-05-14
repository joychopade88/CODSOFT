from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

data = {
    'Title': ['The Matrix', 'Inception', 'Interstellar', 'The Notebook', 'Titanic'],
    'Genre': ['Action Sci-Fi', 'Action Sci-Fi Thriller', 'Adventure Sci-Fi Drama', 'Romance Drama', 'Romance Drama']
}
df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(df['Genre'])
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_recommendations(title, cosine_sim=cosine_sim):
    if title not in df['Title'].values:
        return "Movie not found in database."

    idx = df.index[df['Title'] == title].tolist()[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:3] 

    movie_indices = [i[0] for i in sim_scores]
    return df['Title'].iloc[movie_indices].tolist()

if __name__ == "__main__":
    print("Available movies:", ", ".join(df['Title'].tolist()))
    user_movie = input("Enter a movie from the list above to get recommendations: ")
    print(f"\nBecause you liked '{user_movie}', you might also like:")
    recommendations = get_recommendations(user_movie)
    
    if isinstance(recommendations, str):
        print(recommendations)
    else:
        for movie in recommendations:
            print(f"- {movie}")