FROM alpine:3.7  
RUN apk add --no-cache ansible=2.4.1.0-r0 openssh-client && \  
apk add --no-cache --virtual .deps py2-pip && \  
pip2 install awscli boto boto3 && \  
apk del .deps  
  
COPY entrypoint.sh /root/  
  
ENTRYPOINT ["/root/entrypoint.sh"]  

