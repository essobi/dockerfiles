FROM gliderlabs/logspout:master  
MAINTAINER Squaremouth, Inc. <devops@squaremouth.com>  
  
RUN apk update && apk add curl && rm -rf /var/cache/apk/*  
  
RUN curl https://papertrailapp.com/tools/papertrail-bundle.pem > papertrail-
bundle.pem  
RUN cp papertrail-bundle.pem /etc/ssl/certs/ca-certificates.crt  
RUN cp papertrail-bundle.pem /etc/ssl/ca-bundle.pem  
RUN chmod 644 /etc/ssl/certs/ca-certificates.crt  
RUN chmod 644 /etc/ssl/ca-bundle.pem  
RUN rm papertrail-bundle.pem  

