FROM python:2.7  
MAINTAINER Praekelt Foundation <dev@praekeltfoundation.org>  
COPY . /var/app/  
COPY unicorecmsebola/static/ /var/app/static/  
WORKDIR /var/app/  
RUN pip install --no-cache-dir -e .  
EXPOSE 8080  

