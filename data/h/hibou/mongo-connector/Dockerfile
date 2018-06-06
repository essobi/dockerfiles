FROM python:3.4  
MAINTAINER Hibou Corp. <hello@hibou.io>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV TZ UTC  
RUN pip install mongo-connector==2.3 elastic-doc-manager elastic2-doc-manager  
  
RUN mkdir /conf && mkdir /var/log/mongo-connector  
COPY ./config.json /conf/  
  
CMD ["mongo-connector", "-c", "/conf/config.json"]  

