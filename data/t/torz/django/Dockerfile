FROM python:3.5  
RUN mkdir -p /usr/src/app  
  
WORKDIR /usr/src/app  
  
ONBUILD COPY requirements.txt /usr/src/app/  
ONBUILD RUN pip install --no-cache-dir -r requirements.txt  
  
RUN apt-get update && apt-get install -y \  
gcc \  
gettext \  
mysql-client libmysqlclient-dev \  
postgresql-client libpq-dev \  
sqlite3 \  
\--no-install-recommends && rm -rf /var/lib/apt/lists/*  
RUN pip install -U pip  
  
EXPOSE 8000  
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]  

