def process_files():
    try:
        with open('input.txt', 'r') as input_file:
            content = input_file.read()
        modified_content = content.upper()
        with open('output.txt', 'w') as output_file:
            output_file.write(modified_content)
        print("Success! The content has been processed and written to output.txt.")
    except FileNotFoundError:
        print("Error: 'input.txt' does not exist. Please create the file and try again.")
    except IOError:
        print("Error: Unable to read or write the files. Please check file permissions.")

process_files()
