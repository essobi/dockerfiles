FROM ubuntu:14.04  
RUN apt-get update && \  
apt-get install -qy build-essential libffi-dev libssl-dev python-dev python-
setuptools python-pip git supervisor  
  
ADD requirements.txt /app/requirements.txt  
WORKDIR /app  
RUN pip install -r requirements.txt  
  
ADD . /app  
  
CMD /usr/bin/supervisord -c /app/supervisord.conf  

