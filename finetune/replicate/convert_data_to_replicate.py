import json

input_file_path = 'output.jsonl'
output_file_path = 'output_rep.jsonl'

with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    for line in infile:
        # Parse the line as JSON
        data = json.loads(line.strip())
        
        # Replace the "text" key with "prompt"
        data["prompt"] = data.pop("text")
        
        # Add "completion": ""
        data["completion"] = ""
        
        # Write the updated JSON object to the output file
        outfile.write(json.dumps(data) + '\n')

print(f'Transformation complete. Output written to {output_file_path}.')
