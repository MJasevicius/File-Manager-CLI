import os
import time

class MetadataHandler:
    @staticmethod
    def get_file_size(path):
        original_size = os.path.getsize(path)
        file_size = original_size
        level = 1

        while file_size >= 1024:
            file_size = file_size / 1024
            level += 1

        match level:
            case 1:
                unit_name = "B"
            case 2:
                unit_name = "KB"
            case 3:
                unit_name = "MB"
            case 4:
                unit_name = "GB"
            case 5:
                unit_name = "TB"

        if level > 1:
            print(f"{round(file_size, 2)}{unit_name}({original_size}B)")
        else:
            print(f"{original_size}B")

    @staticmethod
    def get_creation_date(path):
        creation_time = os.path.getctime(path)
        creation_timestamp = time.ctime(creation_time)
        print(creation_timestamp)

    @staticmethod
    def get_modification_date(path):
        modification_time = os.path.getmtime(path)
        modification_timestamp = time.ctime(modification_time)
        print(modification_timestamp)
