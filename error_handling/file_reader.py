def safe_file_reader():
    """
    Asks user for a filename and handles potential errors gracefully.
    """
    while True:
        filename = input("Enter the filename you want to read: ")
        
        try:
            with open(filename, 'r') as file:
                content = file.read()
                print("\nFile content:")
                print(content)
                break
        
        except FileNotFoundError:
            print(f"Error: The file '{filename}' doesn't exist. Please try again.")
        except PermissionError:
            print(f"Error: You don't have permission to read '{filename}'. Try another file.")
        except UnicodeDecodeError:
            print(f"Error: Couldn't decode '{filename}'. It might be a binary file.")
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

# Example usage:
safe_file_reader()