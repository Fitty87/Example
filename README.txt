
Clone project:   
git clone https://github.com/Fitty87/Example

Create virtual enviroment:   
py -m venv env 

Activate virtual enviroment:   
cd env\scripts\
activate.bat 

Install requirements 
cd ..
cd ..
py -m pip install -r Example\requirements.txt

Settings Flask
set FLASK_APP=common_database.py
set FLASK_DEBUG=1

Start Server
Flask run

Use localhost
http://127.0.0.1:5000/


