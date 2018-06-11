FROM ubuntu:14.04  
MAINTAINER John Lynn <jlynn@hearsaycorp.com>  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
libmysqlclient-dev \  
python \  
python-dev \  
python-setuptools  
  
RUN easy_install pip  
RUN pip install virtualenv  
  
VOLUME /opt/virtualenv  
  
WORKDIR /opt  
CMD virtualenv /opt/virtualenv && ls /opt/requirements/*.txt | xargs -n 1
/opt/virtualenv/bin/pip install -r  

