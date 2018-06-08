FROM alpine  
  
MAINTAINER lioncui@163.com  
  
RUN apk add --update python python-dev py-pip && \  
pip install flask && \  
rm /var/cache/apk/*  
  
ADD localtime /etc/localtime  
  
ADD . /webapp/  
  
WORKDIR /webapp  
  
EXPOSE 8080/tcp  
  
CMD ["/usr/bin/python","web.py"]  
  

