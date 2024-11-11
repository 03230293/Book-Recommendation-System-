import pandas as pd

# Load the books dataset
books_df = pd.read_csv('books.csv')  # Ensure this file exists

def get_book_recommendations(title, num_recommendations=3):
    # Find books that contain the title in their title or author
    recommendations = books_df[books_df['Book-Title'].str.contains(title, case=False, na=False) |
                                books_df['Book-Author'].str.contains(title, case=False, na=False)]
    
    # If no recommendations found, return None
    if recommendations.empty:
        return None
    
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
        if recommendations is None:
            print(f"No books found with the title or author containing '{title}'.")
        else:
            print(f"\nTop recommendations for '{title}':")
            for index, row in recommendations.iterrows():
                print(f"{index + 1}: {row['Book-Title']} by {row['Book-Author']}")
            
            # Display the number of recommendations
            num_recommendations = len(recommendations)
            print(f"\nYou have {num_recommendations} recommendations available.")
            
            # Ask the user to select a book
            try:
                selection = int(input(f"Select a book by entering a number (1 to {num_recommendations}, or 0 to skip): "))
                if selection == 0:
                    print("You chose to skip. Thank you for using the Library Book Recommendation System. Goodbye!")
                    break  # End the conversation
                elif 1 <= selection <= num_recommendations:
                    selected_book = recommendations.iloc[selection - 1]
                    print(f"\nYou selected: '{selected_book['Book-Title']}' by {selected_book['Book-Author']}")
                else:
                    print("Invalid selection. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
    