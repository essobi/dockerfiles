FROM python:3.6-alpine3.7  
RUN apk update &&\  
apk add curl git bash openssh-client  
  
RUN pip install rancher-autobackup==1.2.0  
  
COPY docker-entrypoint.sh /docker-entrypoint.sh  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

