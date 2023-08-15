import os
import json

def read_and_write_files():
    output_file = 'output.jsonl'
    directory_to_read = 'repos'

    with open(output_file, 'w') as outfile:
        for subdir, _, files in os.walk(directory_to_read):
            for file_name in files:
                if file_name.endswith('.rs') or file_name.endswith('.md'):
                    file_path = os.path.join(subdir, file_name)
                    with open(file_path, 'r', encoding='utf-8') as file:
                        content = file.read()
                        json_line = json.dumps({"text": content})
                        outfile.write(json_line + '\n')

    print(f"Content from .rs and .md files in {directory_to_read} has been written to {output_file}")

if __name__ == "__main__":
    read_and_write_files()