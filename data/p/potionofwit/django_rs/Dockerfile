FROM python:2.7-slim  
  
RUN mkdir -p /usr/src/app  
WORKDIR /usr/src/app  
  
COPY requirements.txt /usr/src/app/  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY . /usr/src/app  
  
RUN apt-get update && apt-get install -y \  
vim \  
sqlite3 \  
libwww-perl \  
jq \  
curl \  
\--no-install-recommends && rm -rf /var/lib/apt/lists/*  
  
EXPOSE 8000  
RUN ["python", "manage.py", "makemigrations"]  
RUN ["python", "manage.py", "migrate"]  
  
CMD ["/bin/bash", "/usr/src/app/start_service.sh", "admin-gateway.pow.tf"]  
  

