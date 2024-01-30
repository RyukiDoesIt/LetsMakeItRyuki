name = input("File name: ")
ext = name.rsplit('.', 1)[-1].lower()

if ext in ("gif", "png", "jpeg"):
    print(f'image/{ext}')
elif ext == "jpg":
    print('image/jpeg')
elif ext in ("pdf", "zip"):
    print(f'application/{ext}')
elif ext == "txt":
    print("text/plain")
else: 
    print("application/octet-stream")
