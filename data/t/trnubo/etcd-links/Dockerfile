FROM alpine:latest  
  
MAINTAINER Tim Robinson <tim@panubo.com>  
  
COPY repositories /etc/apk/repositories  
  
RUN apk update && \  
apk add python py-pip py-cffi@testing py-cryptography@testing  
  
ENTRYPOINT ["/run.py"]  
  
COPY requirements.txt /requirements.txt  
  
RUN pip install -r requirements.txt && \  
mkdir /output  
  
COPY run.py /run.py  

