Restaurant_list1 = {
 "Name": "Sarsa Kitchen + Bar", 
 "Phone": "0915 721 4190",
 "Ratings": 4.4, 
 "Location": "Makati",
 "Hours": "11 AM to 10 PM",

}

Restaurant_list2 = {
 "Name": "Provenciano",
 "Phone": "0915 721 4190",
 "Ratings": 4.6, 
 "Location": "Quezon",
 "Hours": "11 AM to 10 PM",

}

Restaurant_list3 = {
 "Name": "Pamana Restaurant",
 "Phone": "046 413 2461",
 "Ratings": 4.5, 
 "Location": "Tagaytay", 
 "Hours": "10:30 AM to 9 PM",

}

Restaurant_list4 = {
 "Name": "Barbara Heritage Restaurant",
 "Phone": "02 8527 4083",
 "Ratings": 4.4, 
 "Location": "Intramuros",
 "Hours": "9 AM to 10 PM",

}

Restaurant_list5 = {
 "Name": "Café Adriatico", 
 "Phone": "0917 808 5184",
 "Ratings": 4.5, 
 "Location": "Malate",
 "Hours": "7 AM to 12 AM",

}

for Restaurant in [Restaurant_list1, Restaurant_list2, Restaurant_list3, Restaurant_list4, Restaurant_list5]:
   print(f"Name: {Restaurant.get('Name')}, Phone: {Restaurant.get('Phone')}, Ratings: {Restaurant.get('Ratings')}, Location: {Restaurant.get('Location')}, Hours: {Restaurant.get('Hours')}")
