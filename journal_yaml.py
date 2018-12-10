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
                for key, value in data.items():
                    for x in range(4):
                        # print (yaml.dump(value[x]))
                        temp_data_storage =yaml.dump(value[x])
                        date, name = temp_data_storage.split(',')
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
            print(date, '|', end=' ')
            print(name)

    def search_entry(self, query=''):
        query= input("Enter name that you want to search: ")
        matched_entries = [entry for entry in self.entries if query in entry['name'].lower()]
        print(matched_entries)
        return query

    def delete_entry(self, query=''):
        delete_target= input("Enter name that you want to delete: ")
        matched_entries = [entry for entry in self.entries if query in entry['name'].lower()]
        if matched_entries in self.entries: self.entries.remove(matched_entries)
        return self.entries

    def export_entries(self, file_name):
        with open(file_name, 'w') as f:
            f.writelines([
                '{date}|{name}'.format_map(entry)
                for entry in self.entries
                ])

journal = Journal()
journal.read_input()
print("birthdays")
journal.view_entries()
journal.search_entry(query='')
journal.delete_entry(query='')
journal.export_entries(file_name='birthdays_backup.yaml')
