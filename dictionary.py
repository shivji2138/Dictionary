import mysql.connector

# Connection to the Database
conn = mysql.connector.connect(
    host="localhost",        
    user="root",
    password="shivusql",
    database="dictionary" 
)

# Function to add a new recipe
def add_word():
    word = input("Enter word: ")
    meaning = input("Enter its meaning: ")
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO dictionary (word, meaning) VALUES (%s, %s)", (word,meaning))
    conn.commit()
    print("Meaning added successfully!")
    print()

# Function to search for existing recipes by title
def search_word():
    word = input("Enter the word to search for: ")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dictionary WHERE word = %s", (word,))
    word = cursor.fetchone()
    if word:
        print("Found Recipe:")
        print(f"Word: {word[1]}")
        print(f"Meaning: {word[2]}")
        print()
    else:
        print("No recipes found with that title.")

# Display menu options
def display_menu():
    print("Choose an option:")
    print("1. Add a new word")
    print("2. Search for existing word")
    print("3.Exit")
    choice = input("Enter your choice (1 or 2 or 3): ")
    if choice == "1":
        add_word()
        return True  
    elif choice == "2":
        search_word()
        return True  
    elif choice == "3":
        return False
    else:
        print("Invalid choice!")
        return True  

# Usage: Call the display_menu() function in a loop
while True:
    if not display_menu():
        break 
