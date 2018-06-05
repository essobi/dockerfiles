FROM gliderlabs/alpine  
MAINTAINER Tyler Jones <tyler@squirly.ca>  
  
RUN apk add --update python3 && \  
rm /var/cache/apk/*  
  
RUN pip3 install awscli==1.11.127  
  
ENTRYPOINT ["aws"]  

