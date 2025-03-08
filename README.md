# File-Manager-CLI

# File Manager CLI

A command-line file management application that allows users to perform various file and directory operations such as copying, moving, deleting, searching, compressing, and retrieving metadata.

## Features
- Copy, move, and delete files
- Search for files by name or extension
- Create and delete directories
- List files in a directory
- Retrieve file metadata (size, creation date, last modified date)
- Compress and extract files using ZIP

## Installation
### Prerequisites
- Python 3.x installed

### Clone the Repository
```sh
git clone https://github.com/yourusername/file-manager-cli.git
cd file-manager-cli
```

### Install Dependencies
Ensure you have all required dependencies installed. If any additional modules are needed, install them using:
```sh
pip install -r requirements.txt
```

## Usage
Run the script using the command line:
```sh
python file_manager.py <command> [options]
```

### Available Commands

#### File Operations
- Copy a file:
  ```sh
  python file_manager.py copy <source> <destination>
  ```
- Move or rename a file:
  ```sh
  python file_manager.py move <source> <destination>
  ```
- Delete a file:
  ```sh
  python file_manager.py delete <file>
  ```

#### Search
- Search for files:
  ```sh
  python file_manager.py search --path <directory> [--name <filename>] [--ext <extension>] [-d]
  ```
  - `--name`: Search by filename
  - `--ext`: Search by file extension (e.g., .txt, .jpg)
  - `-d`: Enable deep search

#### Directory Operations
- Create a directory:
  ```sh
  python file_manager.py create-dir <path>
  ```
- Delete a directory:
  ```sh
  python file_manager.py delete-dir <path>
  ```
- List files in a directory:
  ```sh
  python file_manager.py list <path>
  ```

#### Metadata Retrieval
- Get file size:
  ```sh
  python file_manager.py size <path>
  ```
- Get file creation date:
  ```sh
  python file_manager.py created <path>
  ```
- Get last modified date:
  ```sh
  python file_manager.py modified <path>
  ```

#### Compression
- Compress a file into a ZIP archive:
  ```sh
  python file_manager.py zip <file_path> <zip_name>
  ```
- Extract a ZIP file:
  ```sh
  python file_manager.py unzip <zip_name> [--extract_path <path>]
  ```

## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! Feel free to submit a pull request or open an issue.

## Contact
For any inquiries, please contact [your email or GitHub profile].

