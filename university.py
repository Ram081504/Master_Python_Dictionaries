University_list1 = {
 "Name": "University of the Philippines Diliman", 
 "President": "Angelo Jimenez",
 "Location": "Quezon City",
 "Status": "Public",
 "Date": 1908,

}

University_list2 = {
 "Name": "Ateneo de Manila University", 
 "President": "Roberto Yap",
 "Location": "Quezon City",
 "Status": "Private",
 "Date": 1859,

}

University_list3 = {
 "Name": "Philippine Normal University", 
 "President": "Bert J. Tuga",
 "Location": "Manila",
 "Status": "Public",
 "Date": 1901,

}

University_list4 = {
 "Name": "De La Salle University Manila", 
 "President": "Br. Bernard S. Oca FSC",
 "Location": "Manila",
 "Status": "Private",
 "Date": 1911,

}

University_list5 = {
 "Name": "Polytechnic University of the Philippines",
 "President": "Manuel Muhi",
 "Location": "Manila",
 "Status": "Public",
 "Date": 1904,

}

for University in [University_list1, University_list2, University_list3, University_list4, University_list5]:
   print (f"Name: {University.get('Name')}, President: {University.get('President')}, Location: {University.get('Location')}, Status: {University.get('Status')}, Date: {University.get('Date')}")