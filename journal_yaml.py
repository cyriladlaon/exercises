import yaml
# xRead from an input file
    # xAdd entry to journal
    # xView entries
    # xSearch entries
    # Edit entries
    # Delete entries
    # xExport entries
class Journal(object):
    """docstring for ClassName"""
    def __init__(self):
        self.birthdays_id=1
        self.entries =[]

    def read_input(self):
        data = []
        with open("birthdays.yaml", 'r') as stream:
            try:
                data=yaml.load(stream)
                for lines in data['birthdays']:
                    date = lines['date']
                    name = lines['name']
                    self.add_entry(date, name)
            except yaml.YAMLError as exc:
                print(exc)

                return data

    def add_entry(self, date, name):
        self.entries.append({
            'date': date,
            'name': name
        })
    def view_entries(self):
        print('Date\t\t  | Name')
        print('---' * 16)
        for entry in self.entries:
            date, name = entry.values()
            print(date, "\t  ", name)

    def search_entry(self, query=''):
        query= input("Enter name that you want to search: ")
        matched_entries = [entry for entry in self.entries if query in entry['name'].lower()]
        print(matched_entries)
        return query

    def delete_entry(self):
        print("\n")
        target_index = int (input("Enter index that you want to delete: "))
        print("Deleted Info: ",self.entries[target_index])
        self.entries.pop(target_index)

        print("\n")
        self.view_entries()
        return self.entries


    def edit_entry(self):
        print("\n")
        specific_index = int (input("Enter index that you want to edit: "))
        specific_element_to_change = input("Press (n) for name and (d) for date: ")
        if specific_element_to_change == 'n':
            new_name = input("New Name: ")
            self.entries[specific_index]['name'] = new_name
        elif specific_element_to_change == 'd':
            new_date = input("New Date: ")
            self.entries[specific_index]["date"] = new_date
        else:
            print("Invalid input!")

        print("\n")
        self.view_entries()

    def export_entries(self, file_name):
        with open(file_name, 'w') as f:
            f.writelines([
                '{date}|{name}\n'.format_map(entry)
                for entry in self.entries
                ])

journal = Journal()
journal.read_input()
print("birthdays")
journal.view_entries()
journal.search_entry(query='')
journal.delete_entry()
journal.edit_entry()
journal.export_entries(file_name='birthdays_backup.yaml')
