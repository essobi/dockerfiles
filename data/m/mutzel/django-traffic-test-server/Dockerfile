FROM python:2.7.9  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
RUN apt-get update && apt-get install -y \  
sqlite3 \  
gcc \  
\--no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
COPY requirements.txt /usr/src/app/  
COPY . /usr/src/app/  
RUN pip install -r requirements.txt  
  
EXPOSE 8000  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

