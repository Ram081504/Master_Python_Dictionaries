Employee_list1 = {
 "Name": "Kisseraskley Endonela", 
 "Job": "Web Designer",
 "Number": "00015019",
 "Age": 20,
 "Email": "Endonela@gmail.com",

}

Employee_list2 = {
 "Name": "Mat Gabriel Sevella",
 "Job": "SQL Developer",
 "Number": "00015150",
 "Age": 19,
 "Email": "Sevella@gmail.com",

}

Employee_list3 = {
 "Name": "John Denson Inao",
 "Job": "Web Developer",
 "Number": "00015456",
 "Age": 21,
 "Email": "Inao@gmail.com",

}

Employee_list4 = {
 "Name": "Christian Toribio",
 "Job": "Software Engineer",
 "Number": "00015605",
 "Age": 20,
 "Email": "Toribio@gmail.com",

}

Employee_list5 = {
 "Name": "Ram Louise Capilitan", 
 "Job": "IT Professional",
 "Number": "00015607",
 "Age": 20,
 "Email": "Capilitan@gmail.com",

}

for Employee in [Employee_list1, Employee_list2, Employee_list3, Employee_list4, Employee_list5]:
   print(f"Name: {Employee.get('Name')}, Job: {Employee.get('Job')}, Number: {Employee.get('Number')}, Age: {Employee.get('Age')}, Email: {Employee.get('Email')}") 