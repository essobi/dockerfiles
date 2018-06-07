FROM ubuntu:14.04  
MAINTAINER Brian Johnson  
  
RUN apt-get install sudo  
RUN apt-get update -y  
RUN apt-get -y install libssl-dev libxml2-dev libxslt1-dev python-dev gcc
libldap2-dev libsasl2-dev lib32z1-dev wget python-setuptools libffi-dev mysql-
client  
RUN sudo easy_install certifi ndg-httpsclient urllib3  
RUN sudo python --version  
RUN sudo apt-get install -y python-openssl libssl-dev  
RUN sudo easy_install -i http://release.divvycloud.com mysql-connector-python  
RUN sudo easy_install -i http://packages.divvycloud.com/simple divvycloud
divvycloudprocessmanager divvy-ui botfactory  
RUN mkdir config/  
COPY divvy.json config/divvy.json  
COPY entrypoint.py entrypoint.py  
COPY wait-for-it.sh wait-for-it.sh  
RUN chmod +x /entrypoint.py  
RUN chmod +x /wait-for-it.sh  

