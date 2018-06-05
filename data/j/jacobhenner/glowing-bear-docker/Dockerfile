FROM python:3  
MAINTAINER Jacob Henner "code@ventricle.us"  
RUN apt-get update && apt-get install -y git  
  
RUN mkdir /srv/glowing-bear && git clone https://github.com/glowing-
bear/glowing-bear /srv/glowing-bear  
  
WORKDIR /srv/glowing-bear  
  
CMD git pull && python -m http.server  
  
EXPOSE 8000  

