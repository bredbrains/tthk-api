# Routes

| Title | Example | Return |
| ---- | ---- | ----- |
| Changes | /changes | Returns full list of changes |
| Consultations | /consultations | Returns full list of consultations |
| Consultations by department | /consultations?department=3 | Returns list of consultations for selected department |
| Teachers | /teachers | Returns full list of teachers |
| Groups | /groups | Returns full list of groups |
| Status | /status | Returns statuses of services |

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

```json
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

```json
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
  ]
}
```

#### Groups

```json
{
  "data": [
    {
      "group": "AUTpe20_1",
      "department": "transport",
      "language": "estonian",
      "teacher": "Luule Press",
      "contact": "luule.press@tthk.ee"
    }
  ]
}
```

#### Statuses

```json
{
    "data": {
        "TTHK": "OK",
        "Consultations Web": "OK",
        "API Consultations": "OK",
        "API Changes": "OK",
        "API Teachers": "OK",
        "API Groups": "OK"
    }
}
```
