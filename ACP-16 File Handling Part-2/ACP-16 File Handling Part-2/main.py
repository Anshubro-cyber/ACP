import os
def check_file_exists(file_path):
  """Checks if a file exists at the given path."""
  return os.path.isfile(file_path)
def create_file_and_folder(file_name, folder_name):
  """Creates a new file and folder with the given names."""
  try:
    os.makedirs(folder_name, exist_ok=True)  # Create folder if it doesn't exist
    file_path = os.path.join(folder_name, file_name)
    with open(file_path, "w") as file:
      print(f"Created new file: {file_path}")
  except Exception as e:
    print(f"Error creating file and folder: {e}")
def delete_file(file_path):
  """Deletes the file at the given path."""
  try:
    os.remove(file_path)
    print(f"File deleted: {file_path}")
  except FileNotFoundError:
    print(f"File not found: {file_path}")
  except Exception as e:
    print(f"Error deleting file: {e}")
def split_characters(text):
  """Splits a string into a list of characters."""
  return list(text)
# Example usage
file_name = "my_file.txt"
folder_name = "my_folder"
file_path = os.path.join(folder_name, file_name)
if check_file_exists(file_path):
  print(f"File '{file_name}' exists in folder '{folder_name}'.")
else:
  create_file_and_folder(file_name, folder_name)
# Delete the file (optional)
delete_file(file_path)
# Split characters
my_string = "Hello, world!"
characters = split_characters(my_string)
print(f"Characters: {characters}")