#!/us/bin/python3
"""function to write to a file"""


def write_file(filename="", text=""):
    """" wrtie a string to a utf 8 text file

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        The number of characters written.
    """

    with open(filename, "w", encoding = "utf-8") as f:
        return f.write(text)
