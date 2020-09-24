# First part of problem - file reading
import csv
with open("list_for_csv.txt", "r", encoding = "utf-16") as f:
    fields = ["First_name", "Age", "Occupation"]
    reader = csv.DictReader(f, fields, delimiter = ";")
    for row in reader:
        print(row)

# Second part of problem - file writing

clients_list = [{'First_name': 'Masha', 'Age': 25, "Occupation": 'Scientist'}, 
        {"First_name": 'Misha', 'Age': 8, "Occupation": 'Programmer'}, 
        {"First_name": "Vasia", 'Age': 48, "Occupation": 'Big boss'},
        {"First_name": "Sasha", 'Age': 38, "Occupation": 'Teacher'},
        {"First_name": "Vania", 'Age': 30, "Occupation": 'Receptionist'},
        {"First_name": "Marina", 'Age': 28, "Occupation": 'Sales manager'}]


with open("table_csv.csv", "w", encoding="utf-8", newline='') as f:
    fields = ["First_name", "Age", "Occupation"]
    writer = csv.DictWriter(f, fields, delimiter=";")
    writer.writeheader()
    for client in clients_list:
        writer.writerow(client)


#with open("list_for_csv.txt", "r", encoding = "utf-8") as text_file:
    #with open("table_csv.csv", "w", encoding="utf-8", newline='') as csv_file:
        #fields = ["First_name", "Age", "Occupation"]
        #writer = csv.DictWriter(csv_file, fields, delimiter=";")
        #writer.writeheader()
        #for row in text_file:
            #print(row)
            
            #writer.writerow(row)
        #for row in reader:
            