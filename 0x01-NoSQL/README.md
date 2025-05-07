# 0x01. NoSQL

## Project Overview
This project focuses on NoSQL databases, specifically MongoDB. It covers the basics of MongoDB operations through both MongoDB command files and Python scripts. The tasks range from creating and querying collections to more advanced aggregation operations.

## Learning Objectives
- What NoSQL means
- The difference between SQL and NoSQL
- ACID properties
- Document storage in NoSQL
- Types of NoSQL databases
- Benefits of using NoSQL databases
- How to query information from a NoSQL database
- How to insert/update/delete information from a NoSQL database
- How to use MongoDB

## Requirements

### MongoDB Command File Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using MongoDB (version 4.2)
- All files should end with a new line
- The first line of all files should be a comment: `// my comment`
- A README.md file at the root of the folder of the project is mandatory

### Python Script Requirements
- All files will be interpreted/compiled on Ubuntu 18.04 LTS using Python 3.7 and PyMongo 3.10
- All files should end with a new line
- The first line of all files should be exactly `#!/usr/bin/env python3`
- Code should use the pycodestyle style (version 2.5.*)
- All modules should have documentation
- All functions should have documentation
- Code should not be executed when imported

## Tasks

### MongoDB Scripts
0. **List all databases** - `0-list_databases`: Script that lists all databases in MongoDB.
1. **Create a database** - `1-use_or_create_database`: Script that creates or uses a database.
2. **Insert document** - `2-insert`: Script that inserts a document in a collection.
3. **All documents** - `3-all`: Script that lists all documents in a collection.
4. **All matches** - `4-match`: Script that lists all documents with a specific field value.
5. **Count** - `5-count`: Script that displays the number of documents in a collection.
6. **Update** - `6-update`: Script that adds a new attribute to documents.
7. **Delete by match** - `7-delete`: Script that deletes documents with a specific field value.
8. **Regex filter** - `100-find`: Script that lists documents matching a regex pattern.

### Python Scripts
9. **List all documents in Python** - `8-all.py`: Function to list all documents in a collection.
10. **Insert a document in Python** - `9-insert_school.py`: Function to insert a document.
11. **Change school topics** - `10-update_topics.py`: Function to update documents.
12. **Where can I learn Python?** - `11-schools_by_topic.py`: Function to find documents by field value.
13. **Log stats** - `12-log_stats.py`: Script to analyze Nginx logs stored in MongoDB.
14. **Top students** - `101-students.py`: Function to sort students by average score.
15. **Log stats - new version** - `102-log_stats.py`: Enhanced log stats script with top IPs.

## Setup
The project includes automation scripts to help with environment setup and testing:
- `alx_nosql_setup_and_test.sh`: Sets up MongoDB, installs dependencies, and tests all tasks locally.
- `run_on_alx_sandbox.sh`: Automates the connection to the ALX sandbox and runs the tests.

## Usage Examples

### MongoDB Commands
```bash
# List all databases
cat 0-list_databases | mongo

# Create/use a database
cat 1-use_or_create_database | mongo

# Insert a document
cat 2-insert | mongo my_db
```

### Python Scripts
```python
# List all documents
from pymongo import MongoClient
list_all = __import__('8-all').list_all
client = MongoClient('mongodb://127.0.0.1:27017')
school_collection = client.my_db.school
schools = list_all(school_collection)

# Insert a document
insert_school = __import__('9-insert_school').insert_school
new_school_id = insert_school(school_collection, name="UCSF", address="505 Parnassus Ave")
```

## Author
YAS19SIN