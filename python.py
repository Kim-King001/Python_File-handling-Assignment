def main():
    # Ask user for the input filename
    filename = input("Enter the filename to read: ")

    try:
        # Try to open and read the file
        with open(filename, 'r') as infile:
            content = infile.readlines()  # Read lines for easy modification
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
        return
    except IOError:
        print(f"Error: Could not read the file '{filename}'.")
        return

    # Modify the content: Example - convert all lines to uppercase
    modified_content = [line.upper() for line in content]

    # Write the modified content to a new file
    output_filename = "modified_" + filename
    try:
        with open(output_filename, 'w') as outfile:
            outfile.writelines(modified_content)
        print(f"Modified content written to '{output_filename}'.")
    except IOError:
        print(f"Error: Could not write to the file '{output_filename}'.")

if __name__ == "__main__":
    main()
