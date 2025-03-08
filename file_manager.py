import argparse
import utils

from handlers.file_handler import FileHandler
from handlers.search_handler import SearchHandler
from handlers.directory_handler import DirectoryHandler
from handlers.metadata_handler import MetadataHandler
from handlers.compression_handler import CompressionHandler

parser = argparse.ArgumentParser(description='File manager application')
subparsers = parser.add_subparsers(dest="command")

def copy_file(args):
    FileHandler.copy_file(args.source, args.destination)

def move_file(args):
    FileHandler.move_file(args.source, args.destination)

def delete_file(args):
    FileHandler.delete_file(args.file)

def search_file(args):
    SearchHandler.search_for_file(args)

def create_directory(args):
    DirectoryHandler.create_directory(args.path)

def delete_directory(args):
    DirectoryHandler.remove_directory(args.path)

def list_directory(args):
    SearchHandler.search_for_file(args)

def get_file_size(args):
    MetadataHandler.get_file_size(args.path)

def get_file_creation_date(args):
    MetadataHandler.get_creation_date(args.path)

def get_last_modified_date(args):
    MetadataHandler.get_modification_date(args.path)

def zip_file(args):
    CompressionHandler.compress_directory(args)

def unzip_file(args):
    CompressionHandler.decompress_direcotry(args.zip_name, args.extract_path)

#-----------------------------------------------------------------------------------
# FILE COMMANDS
#-----------------------------------------------------------------------------------

# COPY COMMAND
copy_parser = subparsers.add_parser("copy", help="Copy a file to a new location")
copy_parser.add_argument("source", type=utils.get_absolute_path, help="Source file path")
copy_parser.add_argument("destination", type=utils.get_absolute_path, help="Destination path")
copy_parser.set_defaults(func=copy_file)

# MOVE COMMAND
move_parser = subparsers.add_parser("move", help="Move or rename a file")
move_parser.add_argument("source", type=utils.get_absolute_path, help="Source file path")
move_parser.add_argument("destination", type=utils.get_absolute_path, help="Destination path")
move_parser.set_defaults(func=move_file)

# DELETE COMMAND
delete_parser = subparsers.add_parser("delete", help="Delete a file")
delete_parser.add_argument("file", type=utils.get_absolute_path, help="File path to delete")
delete_parser.set_defaults(func=delete_file)

#-----------------------------------------------------------------------------------
# SEARCH COMMANDS
#-----------------------------------------------------------------------------------

# SEARCH COMMAND
search_parser = subparsers.add_parser("search", help="Search for files")
search_parser.add_argument("--name", type=str, help="Filename to search")
search_parser.add_argument("--ext", type=str, help="Search by file extension (e.g., .txt, .jpg)")
search_parser.add_argument("--path", type=utils.get_absolute_path, required=True, help="Directory to search in")
search_parser.add_argument("-d", "--deep", action='store_true', help="Search the directories inside of path directory")
search_parser.set_defaults(func=search_file)

#-----------------------------------------------------------------------------------
# DIRECTORY COMMANDS
#-----------------------------------------------------------------------------------

# Create Directory
create_dir_parser = subparsers.add_parser("create-dir", help="Create a new directory")
create_dir_parser.add_argument("path", type=utils.get_absolute_path, help="Path to create the directory")
create_dir_parser.set_defaults(func=create_directory)

# Delete Directory
delete_dir_parser = subparsers.add_parser("delete-dir", help="Delete a directory")
delete_dir_parser.add_argument("path", type=utils.get_absolute_path, help="Path to the directory to delete")
delete_dir_parser.set_defaults(func=delete_directory)

# LIST COMMAND
list_parser = subparsers.add_parser("list", help="List all files in a directory")
list_parser.add_argument("path", type=utils.get_absolute_path, help="Directory path to list files")
list_parser.set_defaults(func=list_directory)

#-----------------------------------------------------------------------------------
# METADATA COMMANDS
#-----------------------------------------------------------------------------------

# Get File Size
size_parser = subparsers.add_parser("size", help="Get the size of a file")
size_parser.add_argument("path", type=utils.get_absolute_path, help="File path to check size")
size_parser.set_defaults(func=get_file_size)

# Get File Creation Date
created_parser = subparsers.add_parser("created", help="Get the creation date of a file")
created_parser.add_argument("path", type=utils.get_absolute_path, help="File path to check creation date")
created_parser.set_defaults(func=get_file_creation_date)

# Get Last Modified Date
modified_parser = subparsers.add_parser("modified", help="Get the last modified date of a file")
modified_parser.add_argument("path", type=utils.get_absolute_path, help="File path to check last modified date")
modified_parser.set_defaults(func=get_last_modified_date)

#-----------------------------------------------------------------------------------
# COMPRESSION COMMANDS
#-----------------------------------------------------------------------------------

# Zip File
zip_parser = subparsers.add_parser("zip", help="Compress a file into a .zip archive")
zip_parser.add_argument("file_path", type=utils.get_absolute_path, help="File path to compress")
zip_parser.add_argument("zip_name", type=str, help="Output zip file name")
zip_parser.set_defaults(func=zip_file)

# Unzip File
unzip_parser = subparsers.add_parser("unzip", help="Extract a .zip file")
unzip_parser.add_argument("zip_name", type=utils.get_absolute_path, help="Zip file to extract")
unzip_parser.add_argument("--extract_path", type=utils.get_absolute_path, help="Path to extract files to")
unzip_parser.set_defaults(func=unzip_file)

args = parser.parse_args()

if hasattr(args, "func"):
    args.func(args)
else:
    parser.print_help()