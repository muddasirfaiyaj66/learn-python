# appending to a file

more_characters = ["Diddy Kong", "Donkey Kong", "Wario"]

def write_characters_to_file(filename):
    # open file
    # file = open(f"FileSystem/{filename}","a") # only append
    file = open(f"FileSystem/{filename}","a+") # append + read 

    for c in more_characters:
        file.write(c + "\n")
    
    # read file
    file.seek(0,0)
    content = file.read()
    print(content)

    file.close()

    return

def main():
    write_characters_to_file('characters.txt')

if __name__ == "__main__":
    main()