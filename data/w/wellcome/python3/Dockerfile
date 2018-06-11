FROM alpine  
  
LABEL maintainer = "Wellcome Digital Platform team
<wellcomedigitalplatform@wellcome.ac.uk>"  
LABEL description = "Python base image"  
  
RUN apk update && apk add build-base libffi-dev openssl-dev libzip-tools  
RUN apk update && apk add python3 python3-dev  
  
RUN python3 -m ensurepip && pip3 install --upgrade pip

