FROM python:2.7  
MAINTAINER Peter Salanki <peter.salanki@proceranetworks.com>  
  
WORKDIR /tmp  
  
RUN wget
http://download.proceranetworks.com/pldownload/python/plapi/.builds/17.2.0py1/plapi-17.2.0py1-py2.7-linux-x86_64.egg  
RUN easy_install plapi-17.2.0py1-py2.7-linux-x86_64.egg  
RUN rm plapi-17.2.0py1-py2.7-linux-x86_64.egg  

