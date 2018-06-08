FROM python:3.5.1  
MAINTAINER Undefined Network - Piotr 'Piotron' Radosz mail@piotron.net  
  
RUN apt-get update && apt-get install -y \  
libssl-dev \  
&& rm -rf /var/lib/apt/lists/*  
COPY configs /  
  
RUN pip install -r requirements.txt  
  
COPY templates/u2fval.conf /etc/yubico/u2fval/u2fval.conf  
COPY templates/logging.conf /etc/yubico/u2fval/logging.conf  
  
RUN useradd -u 503 u2fval  
VOLUME ["/u2fval-data","/etc/yubico/u2fval" ]  
CMD [ "/usr/local/bin/uwsgi", "uwsgi.yaml" ]  
EXPOSE 8080  
# Initiate database schema  
# If you didn't modified config file, it will create SQLITE database file.  
# docker run {args} u2fval db init  
# Upgrade database schema basing on connection string in u2fval.conf file  
# docker run {args} u2fval db upgrade  
# run standalone webserver  
# docker run {args} u2fval run -i0.0.0.0  
#LABEL network.undefined.vendor="Undefined Network - Piotr Radosz" \  
#description="This Dockerfile runs by default Yubico u2fval server in uwsgi
mode." \  
#version="1.0.0"  

