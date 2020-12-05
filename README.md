# Tallinna Tööstushariduskeskus API
**TTHK REST API** for get changes, consultations and etc. in GET requests.
## How to run?
```pip install flask flask_restful bs4```

```python3 app.py```
## Dependencies
* Python 3.9
* Flask
* Flask-RESTful
* BeautifulSoup4
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
