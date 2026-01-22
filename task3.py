# Simple Recommendation System
# Based on user interest (content-based filtering)

movies = {
    "Avengers": ["action", "superhero"],
    "Titanic": ["romance", "drama"],
    "Inception": ["action", "sci-fi"],
    "Notebook": ["romance", "drama"],
    "Interstellar": ["sci-fi", "space"],
    "Jumanji": ["adventure", "comedy"]
}

def recommend_movie(user_likes):
    recommendations = []

    for movie in movies:
        movie_tags = movies[movie]

        match_count = 0

        for tag in user_likes:
            if tag in movie_tags:
                match_count = match_count + 1

        if match_count > 0:
            recommendations.append(movie)

    return recommendations


print("MOVIE RECOMMENDATION SYSTEM")
print("Available interests: action, romance, drama, sci-fi, space, comedy, adventure")

user_input = input("Enter your interests (comma separated): ")
user_interests = user_input.split(",")

for i in range(len(user_interests)):
    user_interests[i] = user_interests[i].strip().lower()

result = recommend_movie(user_interests)

print("\nRecommended Movies:")
if len(result) == 0:
    print("No recommendation found.")
else:
    for movie in result:
        print("-", movie)
