import csv
import sys

def read_csv_file(file_path):
    data = []
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

def print_selected_columns(buffer, column_indices):
    for row_index, row in enumerate(buffer):
        for col_index in column_indices:
            if col_index < len(row):
                print(f"({row_index}, {col_index}): {row[col_index]}", end='')
        print()

def write_selected_columns_to_csv(buffer, column_indices, output_file_path):
    with open(output_file_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        for row in buffer:
            selected_row = [row[col_index] for col_index in column_indices if col_index < len(row)]
            writer.writerow(selected_row)

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Usage: python script.py <csv_file_path> <output_csv_file_path> <column_index_1> [<column_index_2> ...]")
        sys.exit(1)

    input_file_path = sys.argv[1]
    output_file_path = sys.argv[2]
    column_indices = [int(arg) for arg in sys.argv[3:]]
    buffer = read_csv_file(input_file_path)
    print_selected_columns(buffer, column_indices)
    write_selected_columns_to_csv(buffer, column_indices, output_file_path)
