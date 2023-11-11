import os

def remove_prefix_recursively(folder_path):
    for foldername, subfolders, filenames in os.walk(folder_path):
        for filename in filenames:
            if '.fbx' in filename:
                new_name = os.path.join(foldername, filename.split('.fbx', 1)[-1])
                old_path = os.path.join(foldername, filename)
                new_path = os.path.join(foldername, new_name)

                os.rename(old_path, new_path)
                print(f'Renamed: {filename} to {new_name}')

# Get the directory where the script is located
script_directory = os.path.dirname(__file__)

# Run the script in the same folder as the script
remove_prefix_recursively(script_directory)
