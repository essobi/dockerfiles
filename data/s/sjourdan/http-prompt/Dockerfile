FROM python:alpine  
MAINTAINER Stephane Jourdan <sjourdan@greenalto.com>  
ENV REFRESHED_AT 2016-05-23  
COPY requirements.txt .  
RUN pip install -r requirements.txt  
ENTRYPOINT ["/usr/local/bin/http-prompt"]  

