import os

class FileHandler:
    @staticmethod
    def copy_file(source, destination):
        if os.path.isdir(destination):
            filename = os.path.basename(source)  
            destination = os.path.join(destination, filename) 
        with open(source, 'rb') as file:
            with open(destination, 'wb') as new_file:
                new_file.write(file.read())

        print(f"File copied successfully to {destination}")

    @staticmethod
    def move_file(source, destination):
        if os.path.isdir(destination):
            filename = os.path.basename(source)  
            destination = os.path.join(destination, filename) 
        with open(source, 'rb') as file:
            with open(destination, 'wb') as new_file:
                new_file.write(file.read())

        os.remove(source)
        print(f"File moved successfully to {destination}")

    @staticmethod
    def delete_file(file):
        os.remove(file)
        print(f"File deleted successfully")
