# base-application-docker  
FROM ubuntu:14.04  
MAINTAINER Tadamasa Kimura <tadamasakimra@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
RUN apt-get -y upgrade  
RUN apt-get install -y python2.7 python-virtualenv libssl-dev libffi-dev
python-dev nginx gunicorn supervisor git ruby curl cron apache2-utils  
RUN easy_install -U distribute  
RUN curl https://bootstrap.pypa.io/get-pip.py | python  
RUN pip install -U pip  
RUN pip install -U setuptools  
RUN pip install -U requests  
RUN pip install pyopenssl ndg-httpsclient pyasn1 awscli awsebcli fabric flask
pymongo pytz  

