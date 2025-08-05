def modify_and_write_file(input_file, output_file):
    """
    Reads an input file, modifies its content, and writes to an output file.
    Example modification: convert text to uppercase.
    """
    try:
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Successfully processed {input_file} and saved to {output_file}")
    
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except IOError:
        print(f"Error: Could not read {input_file} or write to {output_file}")

# Example usage:
modify_and_write_file('original.txt', 'modified.txt')