# SBCA
Singapore Birth Count Analysis (SBCA) is a program for analysing the total birth count 
in Singapore from 2016 to 2018. The main goal is to provide a user-friendly interface for user to show the 
Singapore’s Live Birth Dataset in different sights.

## Features of SBCA 
- An Interactive GUI for the project
- Data Filtering 
- Data Visualisation
- Data Exportation 

## Requirements

- `python` 3.x
- `pip`
- `virtualenv`

## Installation

Instructions for how to download/install the code onto your machine.

### Create Virtual Environment

The following command creates a new virtual environment named `venv` in the current directory, usually this will be your project's directory.

```
# Windows (CMD.exe)
python -m venv venv
```

### Activate Virtual Environment

The following commands activate an existing virtual environment on Windows and Unix systems. The command assume that the virtual environment is named `venv` and that its location is in the current directory.

```
# Windows (CMD.exe)
venv\Scripts\activate.bat
```

Once the virtual environment has been activated your console cursor might prepend the name of the virtual environment as shown below.

```
(venv) echo 'Hello World!'
```

### Install Dependencies in Virtual Environment

To install dependencies in the current environment from a `requirements.txt` file the command below can be used.

```
(venv) pip install -r requirements.txt
```
## Running the Program
Once you activated your virtual enviroment, you can run the program. To run the program, 
```
python main.py
```

### Deactivate Virtual Environment

The following command deactivates the current virtual environment, any dependency installed after this command will be installed globally.

```
(venv) deactivate
```
---


