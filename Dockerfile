FROM python
WORKDIR /app
COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt
COPY . .
RUN python3 -m pytest tests.py
RUN flask run --host=0.0.0.0 --port=8000
