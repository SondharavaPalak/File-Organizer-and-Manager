# 📁 File Organizer and Manager

A powerful command-line tool built in **Python** to help you manage and organize your files efficiently. The project supports directory cleanup, file creation/editing, file categorization, and database integration to track operations like **create**, **edit**, **delete**, and **organize** with MySQL.

---

### Features

* 🔍 **Preview before organizing** files
* 📂 Automatically **categorizes files** by type and organizes them into folders
* 🗓️ **Organizes files by modified date**
* 📁 **Create**, ✏️ **Edit**, 🗑️ **Delete**, and 📜 **Read** files from the command line
* 🧹 Cleans up **empty directories**
* 🧾 **Tracks activities** (deleted, organized, and edited files) in a **MySQL database**
* 📊 View files organized, deleted, or edited on specific dates
* 📦 Built-in logging to `file_organizer_log.txt`

---

### Technologies Used

* Python 3.x
* MySQL
* `colorama` for colorful CLI interface
* `os`, `shutil`, `datetime`, `logging` for file and system handling

---

### 🧾 MySQL Tables

The project uses these tables:

* `organized_files`
* `deleted_files`
* `edited_files`

Each operation logs metadata like:

* File name
* Original and target path
* Date and time of operation
* Edited content (for edits)

---

---

### 📌 Future Enhancement

* GUI version (Tkinter or PyQt)
* Add support for cloud storage syncing
* File restoration options
* Backup to ZIP option

---
