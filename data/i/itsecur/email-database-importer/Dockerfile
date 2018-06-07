FROM python:3.6.3  
RUN apt-get update \  
&& apt-get install -y nfs-common \  
&& rm -r /var/lib/apt/lists/*  
  
WORKDIR /usr/src/app  
  
COPY requirements.txt ./  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY email-database-importer.py ./  
  
CMD [ "python", "./email-database-importer.py" ]

