from pathlib import Path

# pathlib module

# file = open('characters.txt','r')

def create_path():
    script_dir = Path(__file__).parent
    print(script_dir.parent)

    path = script_dir / 'characters'
    path.mkdir(parents=True, exist_ok=True)

    path = path / 'zelda.txt'

    file = path.open('w')

    file.write("Ganon")

    file.close()

    # path.write_text("Xyz")
    content= path.read_text()
    print(content)
    return

def main():
    create_path()

if __name__ == "__main__":
    main()