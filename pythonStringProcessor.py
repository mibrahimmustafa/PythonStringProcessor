class StringListManager:
    def __init__(self, input_data):
        if isinstance(input_data, str):
            self.data = [input_data]
        elif isinstance(input_data, list):
            self.data = self.check_list(input_data)
        else:
            raise ValueError("Input must be a string or a list of strings")
    
    def check_list(self, input_list):
        if not all(isinstance(item, str) for item in input_list):
            raise ValueError("All items in the list must be strings")
        if not all(self.is_ascii(item) for item in input_list):
            raise ValueError("All strings must be ASCII-compliant")
        return input_list
    
    def is_ascii(self, s):
        return all(ord(c) < 128 for c in s)
    
    def append(self, new_data):
        if isinstance(new_data, str):
            if not self.is_ascii(new_data):
                raise ValueError("String must be ASCII-compliant")
            self.data.append(new_data)
        elif isinstance(new_data, list):
            checked_list = self.check_list(new_data)
            self.data.extend(checked_list)
        else:
            raise ValueError("Input must be a string or a list of strings")
    
    def save_to_file(self, file_path):
        with open(file_path, 'a') as f:
            for item in self.data:
                f.write("%s\n" % item)
    
# Example usage
try:
    manager = StringListManager(["hello", "world"])
    manager.append("test")
    manager.append(["another", "list"])
    manager.save_to_file("output.txt")
except ValueError as e:
    print(f"Error: {e}")
    
try:
    manager = StringListManager(["hello%", "world#"])
    manager.append("test")
    manager.append(["another", "list"])
    manager.save_to_file("output.txt")
except ValueError as e:
    print(f"Error: {e}")

try:
    manager = StringListManager("1231" )
    manager.append("test")
    manager.append(["another", "list"])
    manager.save_to_file("output.txt")
except ValueError as e:
    print(f"Error: {e}")

try:
    manager = StringListManager(22 )
    manager.save_to_file("output.txt")
except ValueError as e:
    print(f"Error: {e}")