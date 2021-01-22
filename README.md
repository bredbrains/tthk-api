# Tallinna Tööstushariduskeskus API
**TTHK REST API** for get changes, consultations and etc. in GET requests.
Routes can be seen [there](https://github.com/bredbrains/tthk-api/blob/master/routes/README.md).
## Team
* Nikolas Laus ([@blinchk](https://github.com/blinchk))
* Vladislav Narožni ([@JamesEST](https://github.com/JamesEST))
## Powered applications
* [TTHK Consultations Web](https://github.com/bredbrains/tthk-api)
## How to run?
* ### Install requirements
```
pip install -r requirements.txt 
```
* ### Run tests
```
pytest tests.py
```
* ### Run application with Gunicorn
```
gunicorn app:app
```
## Dependencies
* Python 3.9
* Flask
* Flask-CORS
* Flask-RESTful
* BeautifulSoup4
* Gunicorn
* Requests
