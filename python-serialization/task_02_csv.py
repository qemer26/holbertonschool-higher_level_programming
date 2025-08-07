import csv
import json

def convert_csv_to_json(csv_filename):
    """
    Convert a CSV file to a JSON file.
    
    Parameters:
    csv_filename (str): The name of the CSV file to convert.
    
    Returns:
    bool: True if conversion is successful, False if there's an error.
    """
    try:
        # Open the CSV file for reading
        with open(csv_filename, mode='r') as csv_file:
            # Read the CSV file using DictReader to convert each row to a dictionary
            csv_reader = csv.DictReader(csv_file)
            
            # Convert the rows into a list of dictionaries
            rows = list(csv_reader)
        
        # Write the data to a JSON file
        with open("data.json", mode='w') as json_file:
            json.dump(rows, json_file, indent=4)
        
        return True  # Conversion successful
    
    except FileNotFoundError:
        print(f"Error: The file '{csv_filename}' was not found.")
        return False  # File not found
    
    except Exception as e:
        print(f"Error: {e}")
        return False  # General exception handling

