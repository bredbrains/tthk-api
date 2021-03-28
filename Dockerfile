FROM python
WORKDIR /app
COPY requirements.txt requirements.txt 
RUN pip3 install --no-cache-dir -r requirements.txt
COPY . .
RUN python3 -m pytest tests.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]
