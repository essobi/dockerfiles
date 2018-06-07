FROM alpine  
  
MAINTAINER Henrique Chehad <hchehad@gmail.com>  
  
RUN apk update && apk upgrade  
RUN apk add ca-certificates  
RUN apk add curl  
RUN apk add curl-dev  
RUN apk add py-curl  
RUN apk add python  
  
RUN curl -sS https://bootstrap.pypa.io/get-pip.py | python  
  
ADD requirements.txt /root/requirements.txt  
RUN pip install -r /root/requirements.txt  
  
# Clean APK cache  
RUN rm -rf /var/cache/apk/*  
  

