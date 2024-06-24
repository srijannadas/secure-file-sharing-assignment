
# Secure File Sharing Backend ✨

## Overview

Secure File Sharing is helps Ops team to upload files securely and encrypted also normal user can register and see all the uploaded file + user can download it securely.

## Getting Started


### Technologies Used

- python
- fastAPI framework
- postgres
- uvicorn
- SQLAlchemy

### Prerequisites

Make sure you have the following installed on your system:

- [Python](https://www.python.org/downloads/)
- [VS Code](https://code.visualstudio.com)
- Browser

### Installation

1. Clone this repository to your local machine using the following command:
   ```bash
   git clone https://github.com/srijannadas/secure-file-sharing-assignment.git
   ```
2. Navigate to the project directory:
   ```bash
   cd secure-file-sharing-assignment
   ```
3. Create Virtual Environment:
   ```bash
   For Linux:
   python3 -m venv env

   For Windows:
   py -m venv env
   ```
4. Start Virtual Environment:
    ```bash
    For Linux:
    source env/bin/activate

    For Windows:
    env/Scripts/activate
    ```
5. Install required packages:
    ```bash
    pip install -r requirements.txt
    ```
6. Start app:
    ```bash
    uvicorn main:app --reload
    ```


## Features

The assessment consists of the following features:

- password hashing for security.
- file encryption.
- schemas for each api to take required details only. 

---

Made With ❤️ by [Srijanna Das](https://www.linkedin.com/in/srijanna-das-1705641b8/)