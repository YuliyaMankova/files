import os

path = r'D:\pythonProject\books\books'
a = input("Enter the line:")
print(a)
for root, dirs, files in os.walk(path):
    print(root)
    print(dirs)
    print(files)
    for file in files:
        iter_path = os.path.join(root, file)
        with open(iter_path) as book:
            try:
                text_from_book = book.read()
                if a in text_from_book:
                    print(text_from_book)
                    print(file)
            except Exception as e:
                print('File is broken:', file, e)
                continue

