# Flower  
#  
# VERSION 0.1  
FROM alpine:latest  
MAINTAINER zhoujunqian <zjqzero@gmail.com>  
  
# update the package repository and install python pip  
RUN apk update && apk add py-pip  
  
# installing flower  
RUN pip install flower redis  
  
RUN rm -rf /var/cache/apk/*  
  
# Make sure we expose port 5555 so that we can connect to it  
EXPOSE 5555  
# Running flower  
ENTRYPOINT ["flower", "--port=5555"]

