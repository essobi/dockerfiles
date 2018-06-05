# A container for Python3  
FROM alpine:3.4  
MAINTAINER Amo Chumber <root.demon.net@gmail.com>  
  
RUN apk add --no-cache \  
python3 \  
&& python3 -m ensurepip \  
&& python3 -m pip install --upgrade pip setuptools  
  
ENTRYPOINT ["python3"]  

