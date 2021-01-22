# Tallinna Tööstushariduskeskus API
![Lines of code](https://img.shields.io/tokei/lines/github/bredbrains/tthk-api)
![CodeFactor Grade](https://img.shields.io/codefactor/grade/github/bredbrains/tthk-api)
![GitHub Workflow Status](https://img.shields.io/github/workflow/status/bredbrains/tthk-api/CodeQL%20+%20pyTest)
![Uptime Robot ratio (30 days)](https://img.shields.io/uptimerobot/ratio/m786991239-d3351dfc1019b145e07f8548)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/flask)

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
