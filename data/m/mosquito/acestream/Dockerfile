# Set the base image to use to Ubuntu  
FROM ubuntu:14.04  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN sed -i -re
's/([a-z]{2}\\.)?archive.ubuntu.com|security.ubuntu.com/mirror.yandex.ru/g'
/etc/apt/sources.list  
  
RUN apt-get update && apt-get upgrade -y && apt-get install python-minimal
python-setuptools -y && apt-get clean  
  
RUN echo 'deb http://repo.acestream.org/ubuntu/ trusty main' | sudo tee
/etc/apt/sources.list.d/acestream.list && \  
python -c "import urllib; print
urllib.urlopen('http://repo.acestream.org/keys/acestream.public.key').read()"
| apt-key add -  
  
RUN apt-get update && apt-get install -y acestream-engine && apt-get clean  
  
EXPOSE 62062 6878 8621  
ENTRYPOINT ["/usr/bin/acestreamengine"]  

