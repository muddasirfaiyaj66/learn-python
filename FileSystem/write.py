# writing data to files

characters = ["Mario","Lungi","Peach","Yoshi","Browser","Toad"]

def write_characters_to_file(filename):
    # file = open(f'FileSystem/{filename}','w') # only write
    file = open(f'FileSystem/{filename}','w+') # write + read

    for character in characters:
        file.write(character + "\n")
#  read file also
    file.seek(0,0)
    content = file.read()
    print(content)


    file.close()
    return

def main():
    write_characters_to_file("characters.txt")

if __name__ == "__main__":
    main()