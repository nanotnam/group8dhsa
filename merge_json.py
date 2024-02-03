import json

def merge_json_files(file_paths):
    merged_data = []
    for file_path in file_paths:
        with open(file_path, 'r') as file:
            data = json.load(file)
            merged_data.extend(data)
    return merged_data

def write_merged_json(merged_data, output_file):
    with open(output_file, 'w') as file:
        json.dump(merged_data, file, indent=4)

if __name__ == "__main__":
    # List of paths to the JSON files to merge
    file_paths = ["/Users/hoangnamvu/Documents/projects/data_web_sthsth/json_final/wave1_2023_long_final.json", "/Users/hoangnamvu/Documents/projects/data_web_sthsth/json_final/wave2_2023_long_final.json", "/Users/hoangnamvu/Documents/projects/data_web_sthsth/json_final/wave3_2023_long_final.json", "/Users/hoangnamvu/Documents/projects/data_web_sthsth/json_final/wave4_2023_long_final.json"]

    # Merge JSON files
    merged_data = merge_json_files(file_paths)

    # Write merged JSON data to an output file
    output_file = "/Users/hoangnamvu/Documents/projects/data_web_sthsth/json_final/survey_2023_final.json"
    write_merged_json(merged_data, output_file)