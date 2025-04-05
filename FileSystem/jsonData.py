from pathlib import Path
import json 

path = Path(__file__).parent / 'characters.json'

characters = {
    "characters":[
        {"Name": "Mario", "age":25},
        {"Name": "Luigi", "age":26},
        {"Name": "Peach", "age":27},
        {"Name": "Age", "age":28},
        {"Name": "John", "age":29},
    ]
}

def write_json():

    with path.open('w') as file:
        json.dump(characters,file,indent=2)

    return

def read_json():
    with path.open('r') as file:
        data = json.load(file)
        
    return

def main():
    write_json()
    data = read_json()
    print(data)

if __name__ == "__main__":
    main()