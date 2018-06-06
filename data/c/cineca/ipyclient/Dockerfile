  
##########################################################################  
FROM ubuntu:15.10  
MAINTAINER "Paolo D'Onorio De Meo <p.donoriodemeo@cineca.it>"  
  
RUN apt-get update && apt-get install -y \  
wget git vim \  
python python-psutil python-requests python-jsonschema \  
python-setuptools python-dev build-essential \  
libxml2-dev libxslt1-dev libz-dev \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* /var/tmp/*  
  
WORKDIR /tmp  
RUN easy_install pip  
  
#ftp://ftp.renci.org/pub/irods/releases/4.1.7/ubuntu14/irods-
icommands-4.1.7-ubuntu14-x86_64.deb  
  
#######################  
# Python libraries  
RUN pip install --upgrade pip \  
simplejson commentjson httplib2 requests defusedxml lxml queuelib dweepy \  
py2neo neomodel \  
flask-sqlalchemy flask-security flask-restful \  
flask-admin flask-restplus flask-cors \  
git+git://github.com/irods/python-irodsclient.git  
  
# Icommands?  

