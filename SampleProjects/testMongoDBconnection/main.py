# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import src.mongodb_setup as mongodb

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

    collections = mongodb.createCollections()
    print(f"Initial Stage of mongo db: {collections.count_documents({})}")

    mongodb.insert_collections(collections)
    print(f"After Inserting records in mongo db: {collections.count_documents({})}")

    records = collections.find({})
    collection_records = []
    for x in records:
        collection_records.append(x)
    print(f"Fetching records from mongo db: {collection_records}")

    mongodb.delete_collections(collections)
    print(f"After Deleting records in mongo db: {collections.count_documents({})}")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
