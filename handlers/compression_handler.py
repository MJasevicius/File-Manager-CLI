import shutil
import os

class CompressionHandler:
    @staticmethod
    def compress_directory(args):
        path = args.file_path
        file_name = args.zip_name
        shutil.make_archive(file_name, 'zip', path)

    @staticmethod
    def decompress_direcotry(zip_path, extract_to=None):
        if extract_to is None:
            extract_to = os.path.splitext(zip_path)[0]
    
        shutil.unpack_archive(zip_path, extract_to)