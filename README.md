# arXiv-Papers-SQLite-Database
This project establishes a SQLite database for arXiv papers. Data from a .JSON file is processed using a Python script, and then queries are written and tested using SQLite Workbench.

**Prerequisites**
SQLite 3
SQLite Workbench (or your preferred SQLite management tool)

**Initialize the Database:**
If you run the script for the first time, it will initialize and set up the necessary tables in the SQLite database.
**
Insert Data into the Database:**
Have your arXiv21.json file in the same directory. The script will read each line, process the data, and insert it into the database.

**Run the Script:**
python read_json.py

**Query the Database Using SQLite Workbench:**
Open SQLite Workbench.
Connect to the database.db file.
Now you can write and test your queries directly in SQLite Workbench.

**Database Schema**
Authors: Contains the first name and last name of authors.
Paper: Contains information about the paper, such as its title, submitter, and last update date.
Citations: Lists the papers cited by other papers.
Categories: Contains the different categories each paper falls under.
