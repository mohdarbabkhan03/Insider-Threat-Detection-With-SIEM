#!/usr/bin/python3

import os
import time

# Define the directory where you want to create the files
target_directory = "/home/ubuntu/important_files"

def create_files(directory, num_files):
    try:
        os.makedirs(directory, exist_ok=True)
        for i in range(1, num_files + 1):
            file_name = f"file{i}.txt"
            file_path = os.path.join(directory, file_name)

            # Use 'w' mode to create a new file or overwrite an existing one
            with open(file_path, 'w') as file:
                # You can write content to the file here if needed
                pass  # Nothing to write in this example

            print(f"Created {file_name} at {directory}")
    except Exception as e:
        print(f"An error occurred while creating the files: {str(e)}")

def delete_files(directory, num_files):
    try:
        for i in range(1, num_files + 1):
            file_name = f"file{i}.txt"
            file_path = os.path.join(directory, file_name)
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"Deleted {file_name} at {directory}")
            else:
                print(f"File {file_name} not found.")
    except Exception as e:
        print(f"An error occurred while deleting the files: {str(e)}")

if __name__ == "__main__":
    num_files_to_create = 20

    create_files(target_directory, num_files_to_create)
    time.sleep(2)
    delete_files(target_directory, num_files_to_create)

    print("All files have been created and deleted.")