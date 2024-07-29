import os  # Import the os module to interact with the operating system

def list_directory_contents(directory):
    """
    Print the contents of the specified directory.
    
    Args:
        directory (str): The path to the directory to list contents of.
    """
    try:
        # Get the list of items in the specified directory
        contents = os.listdir(directory)
        print(f"Contents of '{directory}':")
        
        # Iterate over the items and print each one
        for item in contents:
            print(item)
    except FileNotFoundError:
        # Handle the case where the directory does not exist
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        # Handle the case where permission is denied to access the directory
        print(f"Permission denied to access the directory '{directory}'.")

# Example usage:
# List the contents of the current directory
list_directory_contents('.')
