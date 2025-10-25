# Python writing files (.txt, .json, .csv)

txt_data = "I love pizzaaaaaaa"

file_path = "fileStuffs/output.txt" # we can also use absolute file path like C:/Users/Desktop[useing forward slash] (note: use double backslash for escape char or use forward slash for strings)

try:
    with open(file=file_path, mode="x") as file:
        file.write(txt_data)
        print(f"txt file '{file_path}' was created!")
except FileExistsError:
    print("That file already exists!")
    
    
# for text data there are different modes

# w -> write (overrite file)
# x -> write if that file don't exists already if that exists then it will throw an err we can also catch the exception btw if it throws err
# a -> append text
# r -> read
