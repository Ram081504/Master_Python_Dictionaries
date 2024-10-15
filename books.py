Books_list1 = {
 "Name": "The Great Gatsby", 
 "Author": "F. Scott Fitzgerald",
 "Genre": "Tragedy",
 "Date": 1925,
 "Ratings": 3.9,

}

Books_list2 = {
 "Name": "Ulysses", 
 "Author": "James Joyce",
 "Genre": "Modernist novel",
 "Date": 1920,
 "Ratings": 3.8,

}


Books_list3 = {
 "Name": "In Search of Lost Time", 
 "Author": "Marcel Proust",
 "Genre": "Philosophical fiction",
 "Date": 1913,
 "Ratings": 4.3,

}


Books_list4 = {
 "Name": "One Hundred Years of Solitude", 
 "Author": "Gabriel García Márquez",
 "Genre": "Novel",
 "Date": 1967,
 "Ratings": 4.1,

}

Books_list5 = {
 "Name": "The Catcher in the Rye", 
 "Author": "J. D. Salinger",
 "Genre": "Realistic fiction",
 "Date": 1951,
 "Ratings": 3.8,

}

for Book in [Books_list1, Books_list2, Books_list3, Books_list4, Books_list5]:
   print(f"Name: {Book.get('Name')}, Author: {Book.get('Author')}, Genre: {Book.get('Genre')}, Date: {Book.get('Date')}, Ratings: {Book.get('Ratings')}")