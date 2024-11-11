import pandas as pd

# Load the books dataset
books_df = pd.read_csv('books.csv')  # Ensure this file exists

def get_book_recommendations(title, num_recommendations=3):
    # Find books that contain the title in their title or author
    recommendations = books_df[books_df['Book-Title'].str.contains(title, case=False, na=False) |
                                books_df['Book-Author'].str.contains(title, case=False, na=False)]
    
    # If no recommendations found, return a message
    if recommendations.empty:
        return f"No books found with the title or author containing '{title}'."
    
    # Return the top N recommendations
    return recommendations[['Book-Title', 'Book-Author']].head(num_recommendations)

def main():
    print("Welcome to the Library Book Recommendation System!")
    
    while True:
        title = input("\nEnter the title of a book (or 'exit' to quit): ")
        if title.lower() == 'exit':
            print("Thank you for using the Library Book Recommendation System. Goodbye!")
            break
        
        recommendations = get_book_recommendations(title)
        if isinstance(recommendations, str):
            print(recommendations)
        else:
            print(f"\nTop recommendations for '{title}':")
            for index, row in recommendations.iterrows():
                print(f"{row['Book-Title']} by {row['Book-Author']}")

if __name__ == "__main__":
    main()