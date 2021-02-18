FROM python
WORKDIR /app
COPY requirements.txt requirements.txt 
RUN pip3 install -r requirements.txt
COPY . .
RUN python3 -m pytest tests.py
EXPOSE 8000:80/udp
EXPOSE 8000:80/tcp
