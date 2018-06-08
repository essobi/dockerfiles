# Base Dockerfile for django projects  
FROM python:3.6  
MAINTAINER chriscartydev@gmail.com  
  
ENV PYTHONBUFFERED 1  
ENV LANG C.UTF-8  
RUN apt-get update && \  
apt-get install -y python3-dev libgdal-dev && \  
apt-get clean;\  
pip install --upgrade pip;  
  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
COPY requirements.txt /build/requirements.txt  
  
RUN chmod +x /usr/local/bin/entrypoint.sh &&\  
pip install -r /build/requirements.txt --no-input  
  
CMD ["python","manage.py", "runserver"]

