import csv
import os
import os.path

dir_path = os.path.join(os.getcwd(), "data")
# Data
users = [
    {"name": "Josiah Cornuau", "user": "jcornuau0", "department": "Services"},
    {"name": "Wenona McChesney", "user": "wmcchesney1", "department": "Sales"},
    {"name": "Gerardo MacKeogh", "user": "gmackeogh2", "department": "Engineering"},
    {"name": "Wynn Turri", "user": "wturri3", "department": "Engineering"},
    {"name": "Anastasia Illsley", "user": "aillsley4", "department": "Accounting"},
    {"name": "Audra LAbbet", "user": "alabbet5", "department": "Product Management"},
    {"name": "Ebenezer Maclaine", "user": "emaclaine6", "department": "Accounting"},
    {"name": "Kiel Wozencroft", "user": "kwozencroft7", "department": "Training"},
    {"name": "Burk Lissandri", "user": "blissandri8", "department": "Sales"},
    {"name": "Blakelee Crolly", "user": "bcrolly9", "department": "Human Resources"},
]


# Read csv file
def read_csv_file():
    path_data = os.path.join(os.getcwd(), "data\\data.txt")
    f = open(path_data)
    csv_f = csv.reader(f)
    for row in csv_f:
        id, first_name, last_name, email, phone, department = row
        print(f"Id {id} fullName {first_name} {last_name}")
    f.close()


def write_csv_file():
    host = [["workstation.local", "192.168.25.46"], ["webserver.cloud", "10.2.5.6"]]
    with open(os.path.join(dir_path, "host.csv"), "w", newline="") as host_cvs:
        write = csv.writer(host_cvs)
        write.writerows(host)


def write_csv_file_with_dict():
    keys = ["name", "user", "department"]
    with open(
        os.path.join(dir_path, "by_deparment.csv"), "w", newline=""
    ) as by_department:
        writer = csv.DictWriter(by_department, fieldnames=keys)
        writer.writeheader()
        writer.writerows(users)


# Create a file with data in it
def create_file(filename):
    with open(os.path.join(dir_path, filename), "w") as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,perennial\n")
        file.write("iris,blue,perennial\n")
        file.write("poinsettia,red,perennial\n")
        file.write("sunflower,yellow,annual\n")


# Read the file contents and format the information about each row
def contents_of_file(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(os.path.join(dir_path, filename), "r", newline="") as file:
        # Read the rows of the file into a dictionary
        column = ["name", "color", "type"]
        rows = csv.DictReader(file, fieldnames=column)

        # Process each item of the dictionary
        for row in rows:
            return_string += "a {} {} is {}\n".format(
                row["color"], row["name"], row["type"]
            )
    return return_string


# Read the file contents and format the information about each row
def contents_of_file2(filename):
    return_string = ""

    # Call the function to create the file
    create_file(filename)

    # Open the file
    with open(os.path.join(dir_path, filename), "r", newline="") as file:
        # Read the rows of the file into a dictionary
        rows = csv.reader(file)

        # Process each item of the dictionary
        for i, row in enumerate(rows):
            if i == 0:
                continue
            name, color, types = row

            return_string += "a {} {} is {}\n".format(color, name, types)
    return return_string


def main():
    # read_csv_file()
    # write_csv_file()
    # write_csv_file_with_dict()
    # Call the function
    print(contents_of_file2("flowers.csv"))
    print("ok")


if __name__ == "__main__":
    main()
