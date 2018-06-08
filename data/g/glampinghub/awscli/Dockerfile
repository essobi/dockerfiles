FROM alpine:latest  
MAINTAINER José Luis Salvador Rufo <salvador.joseluis@gmail.com>  
  
RUN apk add --no-cache less groff python py-pip && \  
pip install awscli && \  
apk del --no-cache --purge py-pip  
  
VOLUME /root/.aws  
ENTRYPOINT ["aws"]  
  

