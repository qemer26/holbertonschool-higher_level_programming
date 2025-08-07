import xml.etree.ElementTree as ET

def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary to an XML file.

    Parameters:
    dictionary (dict): The dictionary to serialize.
    filename (str): The name of the XML file to save the data.
    
    Returns:
    None
    """
    try:
        # Create the root element
        root = ET.Element("data")

        # Iterate through the dictionary and add each key-value pair as child elements
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)  # Ensure the value is a string
        
        # Create an ElementTree object from the root element and write it to the file
        tree = ET.ElementTree(root)
        tree.write(filename)

        print(f"Dictionary serialized to {filename}")
    except Exception as e:
        print(f"Error while serializing to XML: {e}")

def deserialize_from_xml(filename):
    """
    Deserialize an XML file to a Python dictionary.

    Parameters:
    filename (str): The name of the XML file to load.
    
    Returns:
    dict: The deserialized dictionary or None if an error occurs.
    """
    try:
        # Parse the XML file
        tree = ET.parse(filename)
        root = tree.getroot()

        # Create a dictionary from the XML data
        data = {}
        for child in root:
            # Use the tag of each element as the dictionary key
            # Convert the text to string and store in dictionary
            data[child.tag] = child.text
        
        return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return None
    except ET.ParseError:
        print(f"Error: Malformed XML in '{filename}'.")
        return None
    except Exception as e:
        print(f"Error while deserializing from XML: {e}")
        return None

