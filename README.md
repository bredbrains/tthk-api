# Tallinna Tööstushariduskeskus API
**TTHK REST API** for get changes, consultations and etc. in GET requests.
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
pytest api_tests.py
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
## Routes
| Title | Example | Return |
| ---- | ---- | ----- |
| Changes | /changes | Returns full list of changes |
| Consultations | /consultations | Returns full list of consultations |
| Consultations by department | /consultations?department=3 | Returns list of consultations for selected department |
### Departments
| ID | Department |
| ---- | ---- |
| 0 | General subjects |
| 1 | Transports |
| 2 | Mechanics |
| 3 | Energy |
| 4 | IT |
| 5 | Logistics |
| 6 | Textile & Sales |
### Response examples
#### Consultations
*Keep in mind that email will be returned, when it defined on the page.*
```
{
    "data": [
        {
            "teacher": "Baum, Eduard",
            "room": "B 148",
            "email": "eduard.baum@tthk.ee",
            "department": "general",
            "times": [
                {
                    "weekday": "Wednesday",
                    "time": "15.10-15.55"
                },
                {
                    "weekday": "Thursday",
                    "time": "15.10-15.55"
                }
            ]
        }
     ]
}
```
#### Changes
```
{
  "data": [
      {
          "dayofweek": "T",
          "date": "15.12.2020",
          "group": "KRRgeÕ20",
          "lessons": "algus kell 16.30",
          "teacher": "K.Kuiv – Töökorraldus",
          "room": "Distantsõpe"
      }
   }
}
```

