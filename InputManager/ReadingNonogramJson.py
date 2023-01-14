import json
import main


def process_json_from_file(filepath):
    with open(filepath, "r") as file:
        json_string = file.read()
        try:
            data = json.loads(json_string)
            for nonogram in data['nonograms']:
                row_clues = nonogram["row_clues"]
                col_clues = nonogram["col_clues"]
                if len(row_clues) != len(col_clues):
                    print("The number of rows and columns in the matrix are not equal.")
                    return
                print("Row clues:", row_clues)
                print("Column clues:", col_clues)
                main.main(row_clues, col_clues)
        except json.decoder.JSONDecodeError as e:
            print(f'Error: {e}')


if __name__ == '__main__':
    filepath1 = "InputManager/nonogram_clues.json"
    process_json_from_file(filepath1)
