# Busybox version  
# FROM python:3.5-alpine  
# RUN apk update && apk add git build-base linux-headers tzdata  
# Normal debian version  
FROM python:3.5  
RUN apt-get update && apt-get install build-essential -y  
  
RUN pip3 install --upgrade pip setuptools  
  
WORKDIR /src  
COPY requirements.txt ./  
  
RUN pip3 install -r requirements.txt  
  
COPY setup.py setup.cfg ./  
COPY overlock_agent overlock_agent/  
RUN python setup.py install  
  
COPY overlock_agent/settings/dev/overlock_id /etc/  
CMD overlock_server.sh  
#CMD uwsgi --ini=overlock_agent/config/uwsgi.conf  

