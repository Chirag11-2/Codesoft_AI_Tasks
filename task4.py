def recommend_items_content_based(user_preferences, all_items):
    """
    A very basic content-based recommendation system that suggests items
    based on matching genres.

    Args:
        user_preferences (list): A list of genres the user likes.
        all_items (dict): A dictionary where keys are item names and
                          values are lists of their genres.

    Returns:
        list: A list of recommended items.
    """
    recommendations = []
    for item, genres in all_items.items():
        # Check if any of the user's preferred genres are in the item's genres
        if any(pref_genre in genres for pref_genre in user_preferences):
            recommendations.append(item)
    return recommendations

# --- Example Usage ---

# Sample data: Movies with their genres
movies_data = {
    "IN THE SKY": ["Action", "Sci-Fi"],
    "HERA FERI": ["Comedy", "Romance"],
    "TOWARDS THE FUTURE": ["Sci-Fi", "Thriller"],
    "JUMANJI": ["Action", "Adventure"],
    "FIDAA": ["Romance", "Drama"],
    "FAMILY STAR": ["Comedy", "Family"]
}

# User 1's preferences
user1_likes = ["Sci-Fi", "Action"]

# Get recommendations for User 1
recommended_movies_user1 = recommend_items_content_based(user1_likes, movies_data)
print(f"Movies recommended for User 1 (likes {user1_likes}): {recommended_movies_user1}")

# User 2's preferences
user2_likes = ["Comedy"]

# Get recommendations for User 2
recommended_movies_user2 = recommend_items_content_based(user2_likes, movies_data)
print(f"Movies recommended for User 2 (likes {user2_likes}): {recommended_movies_user2}")

# User 3's preferences (no direct match in this simple model)
user3_likes = ["Horror"]
recommended_movies_user3 = recommend_items_content_based(user3_likes, movies_data)
print(f"Movies recommended for User 3 (likes {user3_likes}): {recommended_movies_user3}")
