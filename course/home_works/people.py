try:
    with open('people.txt', 'r') as file:
        lines = file.read().split('\n')
        people = []

        for i in range(0, len(lines), 4):
            name = lines[i].strip()
            phone = lines[i + 1].strip()
            address = lines[i + 2].strip()
            email = lines[i + 3].strip()

            person_info = {
                'Name': name,
                'Phone': phone,
                'Address': address,
                'Email': email
            }
            people.append(person_info)

        print("People's Information:")
        for person in people:
            print(f"Name: {person['Name']}")
            print(f"Phone: {person['Phone']}")
            print(f"Address: {person['Address']}")
            print(f"Email: {person['Email']}\n")
except FileNotFoundError:
    print("File 'people.txt' not found. Make sure the file exists and is in the correct location.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
