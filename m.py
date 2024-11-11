import pandas as pd  # Import the pandas library for data manipulation and analysis

# Load the books dataset
books_df = pd.read_csv('books.csv')  # Read the CSV file 'books.csv' into a DataFrame called books_df

def get_book_recommendations(title, num_recommendations=3):
    """
    This function takes a book title as input and returns a DataFrame of recommended books
    based on the title or author. It returns a maximum of num_recommendations.
    """
    # Find books that contain the title in their title or author
    recommendations = books_df[books_df['Book-Title'].str.contains(title, case=False, na=False) |
                                books_df['Book-Author'].str.contains(title, case=False, na=False)]
    
    # If no recommendations found, return None
    if recommendations.empty:
        return None
    
    # Return the top N recommendations
    return recommendations[['Book-Title', 'Book-Author']].head(num_recommendations)

def main():
    """
    The main function that runs the book recommendation system.
    It handles user input and displays recommendations.
    """
    print("Welcome to the Library Book Recommendation System!")  # Print a welcome message
    
    while True:  # Start an infinite loop for user interaction
        title = input("\nEnter the title of a book (or 'exit' to quit): ")  # Prompt for book title
        if title.lower() == 'exit':  # Check if the user wants to exit
            print("Thank you for using the Library Book Recommendation System. Goodbye!")  # Goodbye message
            break  # Exit the loop
        
        recommendations = get_book_recommendations(title)  # Get book recommendations based on user input
        if recommendations is None:  # Check if no recommendations were found
            print(f"No books found with the title or author containing '{title}'.")  # Inform the user
        else:  # If recommendations are found
            print(f"\nTop recommendations for '{title}':")  # Print header for recommendations
            for index, row in recommendations.iterrows():  # Iterate through the recommendations
                print(f"{index + 1}: {row['Book-Title']} by {row['Book-Author']}")  # Print each recommendation
            
            # Display the number of recommendations
            num_recommendations = len(recommendations)  # Count the number of recommendations
            print(f"\nYou have {num_recommendations} recommendations available.")  # Inform the user
            
            # Ask the user to select a book
            try:
                selection = int(input(f"Select a book by entering a number (1 to {num_recommendations}, or 0 to skip): "))  # Prompt for selection
                if selection == 0:  # Check if the user wants to skip
                    print("You chose to skip. Thank you for using the Library Book Recommendation System. Goodbye!")  # Goodbye message
                    break  # Exit the loop
                elif 1 <= selection <= num_recommendations:  # Check if the selection is valid
                    selected_book = recommendations.iloc[selection - 1]  # Get the selected book
                    print(f"\nYou selected: '{selected_book['Book-Title']}' by {selected_book['Book-Author']}")  # Print the selected book
                else:  # If the selection is invalid
                    print("Invalid selection. Please try again.")  # Inform the user
            except ValueError:  # Handle non-integer input
                print("Invalid input. Please enter a number.")  # Inform the user

if __name__ == "__main__":  # Check if the script is being run directly
    main()  # Call the main function to run the program