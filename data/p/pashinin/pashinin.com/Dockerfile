FROM python:3.6  
RUN apt-get update && \  
apt-get install -y libxslt-dev python3-dev libc-dev libxml2 libxml2-dev gcc
musl-dev g++ make libffi-dev ruby nginx && \  
rm -rf /var/lib/apt/lists/*  
  
COPY requirements.txt /tmp/  
RUN pip install pip -U  
RUN pip install psycopg2 -U  
RUN pip install -r /tmp/requirements.txt --no-cache-dir && \  
rm -rf /tmp/src && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir /mnt/files  
RUN chmod 777 /mnt/files  
WORKDIR /var/www/project/src  
EXPOSE 8000  

