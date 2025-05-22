import os
import shutil
import logging 
from datetime import datetime
from colorama import Fore
import mysql.connector

# To store user activities
logging.basicConfig(filename="file_organizer_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# Dictionary for different files
file_categories = {
    "Document Files": {
        "Text Files": [".txt", ".md", ".rtf"],
        "Word Processing Files": [".docx", ".odt", ".pages"],
        "PDF Files": [".pdf"],
        "Spreadsheet Files": [".xls", ".xlsx", ".ods"],
        "Presentation Files": [".ppt", ".pptx", ".odp"],
        "Compressed Files": [".zip", ".rar", ".tar"]
    },
    "Image Files": {
        "Raster Image Files": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".jfif"],
        "Vector Image Files": [".svg", ".eps", ".ai"]
    },
    "Audio Files": {
        "Compressed Audio Files": [".mp3", ".aac", ".ogg", ".flac"],
        "Uncompressed Audio Files": [".wav", ".aiff"]
    },
    "Video Files": {
        "Video Formats": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv"]
    },
    "Executable Files": {
        "Windows Executables": [".exe", ".bat", ".msi"],
        "Mac Executables": [".app"],
        "Linux Executables": [".sh", ".bin"]
    },
    "Code Files": {
        "Programming Language Files": [".py", ".java",".php"],
        "Markup Language Files": [".xml", ".json", ".yaml", ".csv"]
    },
    "Database Files": {
        "SQL Databases": [".sql", ".sqlite"],
        "NoSQL Databases": [".json", ".mongodb"]
    },
    "System Files": {
        "Configuration Files": [".ini", ".config", ".env"],
        "Log Files": [".log", ".dmp"],
        "Temporary Files": [".temp", ".bak", ".swp"]
    },
    "Web Files": {
        "HTML Files": [".html", ".htm"],
        "CSS Files": [".css"],
        "JavaScript Files": [".js"],
        "Image Files for Web": [".svg", ".webp"]
    },
    "Archive Files": {
        "Compressed Archives": [".zip", ".tar.gz", ".rar", ".7z"]
    },
    "Backup Files": {
        "Backup Formats": [".bak", ".tar", ".iso"]
    },
    "Font Files": {
        "Font Formats": [".ttf", ".otf", ".woff", ".woff2"]
    },
    "Disk Image Files": {
        "Disk Images": [".iso", ".img", ".dmg"]
    },
    "Virtual Machine Files": {
        "VM Disk Files": [".vmdk", ".vdi"],
        "VM Configuration Files": [".vmx", ".vbox"]
    }
}

def changeDirectory(directoryPath):
    """
    Description:- 
        Change the current working directory to the specified path.

    Parameters:
        directoryPath (str): The path of directory where we want to make changes.
    """
    try:
        os.chdir(directoryPath)
    except FileNotFoundError:
        print(Fore.YELLOW+f"\t\tThe directory {directoryPath} does not exist!")
    except Exception as e:
        print(Fore.YELLOW+f"\t\tError while changing directory: {e}")

def createFile(fileName, directoryPath):
    """ 
    Description:- 
        Create a file with the filename in the specified directory.

    Parameters:
        fileName (str): The name of the file
        directoryPath (str): The directory path where the file should be created
    """
    try:
        changeDirectory(directoryPath)
        with open(fileName, 'x') as f:
            print(Fore.GREEN+f"\n\t\tFile name {fileName} created successfully in {directoryPath}!\n\n")
    except FileExistsError:
        print(Fore.YELLOW+f"\t\tFile name {fileName} already exists!\n\n")
        newFileName = input(Fore.BLUE+"\t\tEnter new file name: ")
        createFile(newFileName, directoryPath)
    except Exception:
        print(Fore.YELLOW+"\t\tSorry! Cannot create file. Some error occurred!\n\n")

def viewAllFiles(directoryPath):
    """
    Description:-
        Show all the files in the specified directory.

    Parameters:
        directoryPath (String): The directory path where the files are listed
    """
    try:
        changeDirectory(directoryPath)
        files = os.listdir()
        if not files:
            print(Fore.YELLOW+"\t\tThere are no files in your current directory.")
        else:
            print(Fore.YELLOW+"\t\tFiles in your current directory are as below: \n")
            for i, file in enumerate(files):
                print(Fore.GREEN+f"\t\t({i+1}) {file}")
    except Exception as e:
        print(Fore.YELLOW+f"\t\tError while viewing files: {e}")

def deleteFile(fileName, directoryPath):
    """ 
    Description:-
        Delete a file with the filename in the specified directory.

    Parameters:
        fileName (String): The name of the file
        directoryPath (String): The directory path where the file should be deleted
    """
    try:
        changeDirectory(directoryPath)
        os.remove(fileName)
        insertDeletedFile(fileName,directoryPath)
        print(Fore.GREEN+f"\t\tFile {fileName} deleted successfully!")
    except FileNotFoundError:
        print(Fore.YELLOW+f"\t\tThere is no file with {fileName}.\n\t\tPlease enter the correct file name.\n\n")
        newFileName = input(Fore.BLUE+"\t\tEnter correct file name: ")
        deleteFile(newFileName, directoryPath)
    except Exception:
        print(Fore.YELLOW+"\t\tSorry! Cannot delete file. Some error occurred!")

def readFile(fileName, directoryPath):
    """ 
    Description:- 
        Read the content of a file in the specified directory.

    Parameters:
        fileName (String): The name of the file
        directoryPath (String): The directory path where the file is located
    """
    try:
        changeDirectory(directoryPath)
        with open(fileName, 'r') as file:
            content = file.readlines()
            if content:
                print(Fore.YELLOW+f"\t\tContent of {fileName} is as below: \n")
                for line in content:
                    print(Fore.GREEN+f"\t\t{line}")
            else:
                print(Fore.RED+f"\t\tfile {fileName} is empty.")
    except FileNotFoundError:
        print(Fore.YELLOW+f"\t\tThere is no file with {fileName}.\n\t\tPlease enter the correct file name.\n\n")
        newFileName = input(Fore.BLUE+"\t\tEnter correct file name: ")
        readFile(newFileName, directoryPath)
    except Exception as e:
        print(Fore.YELLOW+"\t\tSorry! Cannot read file. Some error occurred!")

def editFile(fileName, directoryPath):
    """ 
    Desciption:- 
        Edit the content of a file in the specified directory.

    Parameters:
        fileName (String): The name of the file
        directoryPath (String): The directory path where the file is located
    """
    try:
        changeDirectory(directoryPath)
        with open(fileName, 'a') as file:
            editContent = input(Fore.BLUE+f"\t\tEnter content to add to {fileName}: \n")
            file.write(editContent + "\n")
            insertEditFiles(fileName,directoryPath,editContent)
            print(Fore.GREEN+f"\t\tYour content was added to {fileName} successfully!")
    except FileNotFoundError:
        print(Fore.YELLOW+f"\t\tThere is no file with {fileName}.\n\t\tPlease enter the correct file name.\n\n")
        newFileName = input(Fore.BLUE+"\t\tEnter correct file name: ")
        editFile(newFileName, directoryPath)
    except Exception as e:
        print(Fore.YELLOW+"\t\tSorry! Cannot edit file. Some error occurred!")

def createDirectories(directoryPath):

    """ 

    Desciption:- 
        Create directories for each category and subcategory inside the source directory if they don't exist.

    Parameters:
        directoryPath (String): The directory path where the file is located
    
    """

    for category, subcategories in file_categories.items():
        category_folder = os.path.join(directoryPath, category)
        if not os.path.exists(category_folder):
            os.makedirs(category_folder)
        for subcategory in subcategories:
            subcategory_folder = os.path.join(category_folder, subcategory)
            if not os.path.exists(subcategory_folder):
                os.makedirs(subcategory_folder)

def moveFile(filePath, target_dir, fileName):

    """ 

    Desciption:- 
        Create directories for each category and subcategory inside the source directory if they don't exist.

    Parameters:

        filePath (String): The file path where the file is located
        target_dir(String): The directory where file is supposed to be moved
        fileName(String): The name of the file
    
    """
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    if os.path.exists(filePath):
        target_file_path = os.path.join(target_dir, fileName)
        
        if os.path.exists(target_file_path):
            base, ext = os.path.splitext(fileName)
            counter = 1
            while os.path.exists(target_file_path):
                target_file_path = os.path.join(target_dir, f"{base}_{counter}{ext}")
                counter += 1
            logging.info(f"Renaming and moving file: {fileName} to {target_file_path}")
        
        shutil.move(filePath, target_file_path)
        
        insertFile(fileName, filePath, target_file_path)
        logging.info(f"Moved {fileName} to {target_dir}")
    else:
        logging.warning(f"File not found: {fileName}")


    
def organizeFile(directoryPath):
     
    """ 

    Desciption:- 
        Organizing the files in the specified directory.

    Parameters:
        directoryPath (String): The directory path where the file is located
    
    """

    createDirectories(directoryPath)

    for fileName in os.listdir(directoryPath):
        filePath = os.path.join(directoryPath, fileName)

        if os.path.isdir(filePath):
            continue

        # Get file extension and last modified date
        file_extension = os.path.splitext(fileName)[1].lower()
        file_modified_time = os.path.getmtime(filePath)
        file_modified_date = datetime.fromtimestamp(file_modified_time)
        year_folder = str(file_modified_date.year)
        month_folder = file_modified_date.strftime("%B")
        day_folder = str(file_modified_date.day)

        # Check file type category
        categorized = False
        for category, subcategories in file_categories.items():
            for subcategory, extensions in subcategories.items():
                if file_extension in extensions:
                    target_dir = os.path.join(directoryPath, category, subcategory)
                    moveFile(filePath, target_dir, fileName)
                    categorized = True
                    break
            
            if categorized:
                break
        
        if not categorized:
            # Move to 'Others' folder
            target_dir = os.path.join(directoryPath, 'Others')
            moveFile(filePath, target_dir, fileName)

        # Organize by date
        date_dir = os.path.join(directoryPath, year_folder, month_folder, day_folder)
        if not os.path.exists(date_dir):
            os.makedirs(date_dir)
        moveFile(filePath, date_dir, fileName)

def cleanEmptyFolders(directoryPath):

    """
    Description:-
        Clean up empty folders after organizing files.
    
    Parameters:- 
        directoryPath (String): The directory path where the file is located
    
    """
    for root, dirs, files in os.walk(directoryPath, topdown=False):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            if not os.listdir(dir_path):  
                os.rmdir(dir_path)
                logging.info(f"Deleted empty folder: {dir_path}")

def previewFiles(directoryPath):

    """

    Description:-
        Preview the files that are about to be moved.
    
    Parameters:- 
        directoryPath (String): The directory path where the file is located

    """
    preview_list = []
    for filename in os.listdir(directoryPath):
        file_path = os.path.join(directoryPath, filename)
        if os.path.isdir(file_path):
            continue
        file_extension = os.path.splitext(filename)[1].lower()
        preview_list.append(f"File: {filename} will be moved to {file_extension}")
    return preview_list

def getUserConfirmation():

    """

    Description:-
        Ask the user for confirmation before proceeding.

    """
    print("\n\n")
    user_input = input(Fore.BLUE+"\t\tDo you agree to proceed further? (yes/no): ")
    return user_input.lower() == "yes"


def getFilesByDate(date_str):

    """
    Description:- 

        Get all files organized on the given date.

    Parameters:
        date_str(String): Date in format YYYY-MM-DD.

    """
    connection = getConnection()
    if connection:
        cursor = connection.cursor()
        query = """
            SELECT file_name, original_path, target_path, move_date
            FROM organized_files
            WHERE DATE(move_date) = %s
        """
        cursor.execute(query, (date_str,))
        rows = cursor.fetchall()
        if rows:
            print(Fore.YELLOW + f"\t\tFiles organized on {date_str}:")
            for row in rows:
                print(Fore.GREEN + f"\t\tFile Name: {row[0]}")
                print(Fore.GREEN + f"\t\tOriginal Path: {row[1]}")
                print(Fore.GREEN + f"\t\tTarget Path: {row[2]}")
                print(Fore.GREEN + f"\t\tMove Date: {row[3]}\n")
        else:
            print(Fore.YELLOW + f"\t\tNo files organized on {date_str}.")
        cursor.close()
        connection.close()


def getConnection():
    """
    Description:-
        Connect to file organizer database
    """
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  
            database="file organizer" 
        )
        return connection
    except mysql.connector.Error as err:
        print(Fore.RED+f"\t\tError: {err}")
        return None


def insertFile(fileName, directoryPath, targetPath):

    """
    Description:- 

        Inserting file details which are organized in table.

    Parameters:
        fileName(String):- The name of the file
        directoryPath(String):- The directory path where file is located
        targetPath(String):- The directory path where file is moved

    """    

    connection = getConnection()
    if connection:
        cursor = connection.cursor()
        moveDate = datetime.now()
        query = """
            INSERT INTO organized_files (file_name, original_path, target_path, move_date)
            VALUES (%s, %s, %s, %s)
        """
        data = (fileName, directoryPath, targetPath, moveDate)
        cursor.execute(query, data)
        connection.commit()
        cursor.close()
        connection.close()

def insertDeletedFile(fileName, directoryPath):

    """
    Description:- 

        Inserting file details which are deleted in table.

    Parameters:-
        fileName(String):- The name of the file
        directoryPath(String):- The directory path where file is located

    """    

    connection = getConnection()
    if connection:
        cursor = connection.cursor()
        deletedTime = datetime.now()
        query = """
            INSERT INTO deleted_files (file_name, original_path, deleted_at)
            VALUES (%s, %s, %s)
        """
        cursor.execute(query, (fileName, directoryPath, deletedTime))
        connection.commit()
        cursor.close()
        connection.close()

def viewDeletedFile(date_str):

    """
    Description:- 

        Fetching file details of deleted file stored in table.

    Parameters:
        date_str(String):- Date in format YYYY-MM-DD.

    """    

    connection = getConnection()
    if connection:
        cursor = connection.cursor()
        query = """
            Select * from deleted_files
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        if rows:
            print(Fore.YELLOW + f"\t\tFiles deleted on {date_str}:")
            for row in rows:
                print(Fore.GREEN + f"\t\tFile Name: {row[1]}")
                print(Fore.GREEN + f"\t\tOriginal Path: {row[2]}")
                print(Fore.GREEN + f"\t\tDeleted Date: {row[3]}\n")
        else:
            print(Fore.YELLOW + f"\t\tNo files deleted on {date_str}.")
        cursor.close()
        connection.close()

def insertEditFiles(fileName,directoryPath,editContent):

    """
    Description:- 

        Inserting file details of edited file in table.

    Parameters:-
        fileName(String):- The name of the file
        directoryPath(String):- The directory path where file is located
        editContent(String):- Content edited by user

    """    


    connection = getConnection()
    if connection:
        cursor = connection.cursor()
        editedTime = datetime.now()
        query = """
            INSERT INTO edited_files (file_name, original_path, edit_content , edited_at)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(query, (fileName, directoryPath, editContent, editedTime))
        connection.commit()
        cursor.close()
        connection.close()

def viewEditedFile(fileName):

    """
    Description:- 

        Fetching file details of edited file stored in table.

    Parameters:
        fileName(String):-The name of the file. 

    """    

    connection = getConnection()
    if connection:
        cursor = connection.cursor()
        query = """
            Select * from edited_files where file_name=%s
        """
        cursor.execute(query,(fileName,))
        rows = cursor.fetchall()
        if rows:
            print(Fore.YELLOW + f"\t\tEdit information about File {fileName}:")
            for row in rows:
                print(Fore.GREEN + f"\t\tFile Name: {row[1]}")
                print(Fore.GREEN + f"\t\tOriginal Path: {row[2]}")
                print(Fore.GREEN + f"\t\tEdited Content: {row[3]}")
                print(Fore.GREEN + f"\t\tEdited Date: {row[4]}\n")
        else:
            print(Fore.YELLOW + f"\t\tFile {fileName} is not edited.")
        cursor.close()
        connection.close()


def main():
    """ 
    Description:- 
        To ask user which operation he wants to conduct
    """
    print(Fore.RED + "\t\t\t\t\t\tWelcome to our File Organizer!!\n")

    directoryPath = input(Fore.BLUE + "\t\tPlease enter the path of the directory you want to work in: ")

    while True:
        print("\n\n")
        print(Fore.YELLOW + "\t\t(1) To create a file")
        print(Fore.YELLOW + "\t\t(2) To delete file")
        print(Fore.YELLOW + "\t\t(3) To read content of file")
        print(Fore.YELLOW + "\t\t(4) To Edit the content of file")
        print(Fore.YELLOW + "\t\t(5) To View all files")
        print(Fore.YELLOW + "\t\t(6) To Organize files in given directory")
        print(Fore.YELLOW + "\t\t(7) To View files organized on a specific date")
        print(Fore.YELLOW + "\t\t(8) To View files deleted on a specific date")
        print(Fore.YELLOW + "\t\t(9) To Get information about edited file.")
        print(Fore.YELLOW + "\t\t(10) To exit the program\n")

        choice = int(input(Fore.BLUE + "\t\tEnter your choice: "))
        print("\n\n")

        if choice == 1:
            fileName = input(Fore.BLUE + "\t\tEnter the file name you want to create: ")
            createFile(fileName, directoryPath)
        
        elif choice == 2:
            fileName = input(Fore.BLUE + "\t\tEnter the file name you want to delete: ")
            deleteFile(fileName, directoryPath)

        elif choice == 3:
            fileName = input(Fore.BLUE + "\t\tEnter the file name you want to read: ")
            readFile(fileName, directoryPath)
        
        elif choice == 4:
            fileName = input(Fore.BLUE + "\t\tEnter the file name you want to edit: ")
            editFile(fileName, directoryPath)
        
        elif choice == 5:
            viewAllFiles(directoryPath)

        elif choice == 6:
            preview = previewFiles(directoryPath)
            print(Fore.YELLOW + "\t\tPreview of files to be organized:")
            for item in preview:
                print(Fore.GREEN + f"\t\t{item}")
        
            if getUserConfirmation():
                organizeFile(directoryPath)
                cleanEmptyFolders(directoryPath)
                print(Fore.GREEN + f"\t\tFiles in {directoryPath} have been organized successfully!")
            else:
                print(Fore.YELLOW + "\t\tFile organization aborted.")

        elif choice == 7:
            date_str = input(Fore.BLUE + "\t\tEnter the date (YYYY-MM-DD) to see organized files: ")
            getFilesByDate(date_str)

        elif choice == 8:
            date_str = input(Fore.BLUE + "\t\tEnter the date (YYYY-MM-DD) to see organized files: ")
            viewDeletedFile(date_str)

        elif choice == 9:
            fileName = input(Fore.BLUE+"\t\tEnter the file name: ")
            viewEditedFile(fileName)

        elif choice == 10:
            print(Fore.RED + "\t\tExiting the program...\n\n\n")
            print(Fore.RED + "\t\t\t\t\tThank you!!!\n\n")
            break

        else:
            print(Fore.RED + "\t\tInvalid choice\n\t\tPlease enter choice between 1 to 8.")

if __name__ == "__main__":
    
    main()