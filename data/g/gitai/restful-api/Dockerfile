# https://github.com/francescou/docker-compose-ui  
# DOCKER-VERSION 1.12.3  
FROM python:2.7-alpine  
MAINTAINER Francesco Uliana <francesco@uliana.it>  
  
RUN pip install virtualenv  
  
RUN apk add -U --no-cache git  
  
COPY . /app  
RUN virtualenv /env && /env/bin/pip install --no-cache-dir -r
/app/requirements.txt  
  
VOLUME ["/opt/lattice/projects"]  
  
EXPOSE 5000  
ENTRYPOINT ["/env/bin/python", "/app/main.py"]  
  
WORKDIR /opt/lattice/projects

