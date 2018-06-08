FROM python:3.5-alpine  
MAINTAINER Jean-Avit Promis <docker@katagena.com>  
  
WORKDIR /usr/src/docker-image-updater  
  
COPY requirements.txt /usr/src/docker-image-updater/  
RUN pip install --no-cache-dir -r requirements.txt  
  
COPY app.py /usr/src/docker-image-updater/  
  
ENV ROUTE /images/pull  
  
ENTRYPOINT ["python", "-u", "app.py"]  

