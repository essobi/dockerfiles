FROM python:2-slim  
  
WORKDIR /app  
  
RUN pip install Mako==1.0.0 gunicorn==19.3.0 falcon==0.3.0 pymongo==2.7  
  
COPY . /app  
WORKDIR /app  
  
ENTRYPOINT ["gunicorn", "-b", "0.0.0.0:8000", "--access-logfile",
"/dev/stdout", "--log-file", "-", "--log-level", "info", "playlister:app"]  

