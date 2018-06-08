FROM ubuntu:17.10  
MAINTAINER dev@dwolla.com  
USER root  
  
ENV SECURITY_MONKEY_VERSION=v0.9.2  
  
RUN apt-get update &&\  
apt-get -y install python-pip python-dev python-psycopg2 libpq-dev git libffi-
dev python-virtualenv libssl-dev &&\  
cd /usr/local/src &&\  
git clone \--depth 1 --branch $SECURITY_MONKEY_VERSION
https://github.com/Netflix/security_monkey.git &&\  
cd security_monkey &&\  
virtualenv venv &&\  
. venv/bin/activate &&\  
pip install \--upgrade setuptools &&\  
pip install \--upgrade pip &&\  
pip install \--upgrade urllib3[secure] &&\  
python setup.py install  
ADD config/config.py /usr/local/src/security_monkey/env-config/config.py  
  
ENV PATH=/usr/local/src/security_monkey/venv/bin:$PATH  

