Laptop_products_list1 = {
    "Name": "Microsoft Surface Laptop", 
    "Processor": "Qualcomm Snapdragon X Elite",
    "Screensize": "14-inch / 15-inch",
    "Ram": 64,
    "Storage": "1TB",
}

Laptop_products_list2 = {
    "Name": "Lenovo IdeaPad Duet 5 OLED Chromebook",
    "Processor": "Qualcomm Snapdragon 7c Gen2",
    "Screensize": "13.3-inch",
    "Ram": 8,
    "Storage": "128GB", 
}

Laptop_products_list3 = {
    "Name":"Apple MacBook Air M3",
    "Processor": "Apple M3",
    "Screensize": "13.6-inch",
    "Ram": 24,
    "Storage": "2TB",
}

Laptop_products_list4 = {
    "Name": "Dell XPS 13 2024",
    "Processor": "Qualcomm Snapdragon X Elite",
    "Screensize": "13.4-inch",
    "Ram": 16,
    "Storage": "512GB",
}

Laptop_products_list5 = {
    "Name": "Acer Aspire 5",
    "Processor": "Intel Core i5",
    "Screensize": "14-inch",
    "Ram": 8,
    "Storage": "512GB", 
}
 

for Laptop in [Laptop_products_list1, Laptop_products_list2, Laptop_products_list3, Laptop_products_list4, Laptop_products_list5]:
    print(f"Name: {Laptop.get('Name')}, Processor: {Laptop.get('Processor')}, Screensize: {Laptop.get('Screensize')}, Ram: {Laptop.get('Ram')}, Storage: {Laptop.get('Storage')}")