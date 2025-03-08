import os
import shutil

class DirectoryHandler:
    @staticmethod
    def create_directory(path):
        os.mkdir(path)

    @staticmethod
    def remove_directory(path):
        shutil.rmtree(path)