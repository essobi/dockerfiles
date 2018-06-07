FROM lazyants/docker-opencv-python:latest  
  
MAINTAINER Dmitriy Belyaev "dimabelyaev27@gmail.com"  
RUN pip install flask flask_api  
  
COPY . /var/app  
  
ENV SCANNER_ADDITIONAL_CONFIG="/var/app/production.py"  
WORKDIR /var/app  
  
CMD python web.py  
  
EXPOSE 5000  

