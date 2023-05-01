import csv, shutil

file_name = "cities_worked_2023.csv"
backup_copy = "backup_file.csv"


#copy csv file to backup before changing
shutil.copyfile(file_name, backup_copy)


#Used to start file
#with open('cities_worked_2023.csv', mode='w') as csv_file:
#    fieldnames = ['address','city','date', 'amount', 'client']
#    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#    writer.writeheader()

while True:
    quit = input("Press enter to continue or q to quit:")
    if quit == "q":
        break
    
    else:
        address = input("Enter stage address: ")
        city = input("Enter the city the stage was in: ")
        date = input("Enter date of stage (mm/dd/yyyy): ")
        amount = float(input("Cost of install: "))
        name = input("Name of the client: ")

    try:
        with open(file_name, mode='a+') as csv_file:
            fieldnames = ['address', 'city', 'date', 'amount', 'client']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writerow({'address': address, 'city': city, 'date': date, 'amount': amount, 'client': name})
    except Exception as e:
        print(e)
        break
        
	
