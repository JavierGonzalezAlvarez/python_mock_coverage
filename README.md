# Unittes with Mock and Coverage

* $ virtualenv entorno_virtual -p python3.11
* $ source entorno_virtual/bin/activate
* $ pip install -r requirements.txt

* $ systemctl start mongod
* $ mongodb-compass

* code .
* configure test in VSC for python
* $ python -m unittest

* add __init__.py to test folder
* $ coverage run -m unittest -v; coverage html
* open htmlcov/index.html
