import pickle

class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the object's attributes."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """
        Serialize the current instance and save it to the given file.
        """
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
            print(f"Object serialized and saved to {filename}.")
        except Exception as e:
            print(f"Error while serializing object: {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize an object from the given file.
        """
        try:
            with open(filename, 'rb') as file:
                obj = pickle.load(file)
            return obj
        except FileNotFoundError:
            print(f"Error: File '{filename}' not found.")
        except pickle.UnpicklingError:
            print("Error: Malformed file or invalid pickle data.")
        except Exception as e:
            print(f"Error while deserializing object: {e}")
        return None

