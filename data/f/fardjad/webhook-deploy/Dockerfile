FROM alpine:3.4  
MAINTAINER Fardjad Davari <public@fardjad.com>  
LABEL Description="An Alpine Linux based image that can clone a Git repository
and execute a custom setup script upon receiving webhooks" Version="0.2.2"  
  
EXPOSE 8000  
ADD ./bootstrap.sh /tmp/  
ADD ./src /opt/webhook-deploy  
RUN chmod +x /tmp/bootstrap.sh && sync && /tmp/bootstrap.sh && rm
tmp/bootstrap.sh  
  
CMD [ "/opt/webhook-deploy/webhook-deploy" ]  

