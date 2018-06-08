FROM alpine:3.2  
ENV Build on 07/06/2015  
# Install security updates and required packages  
RUN apk add --update python py-pip bash libffi-dev openssl-dev && \  
rm /var/cache/apk/*  
  
# Install requirements from the project's requirements.txt  
RUN mkdir /app  
ADD requirements.txt /app/requirements.txt  
RUN pip install -r /app/requirements.txt  
  
ADD sloppytest.py /app/sloppytest.py  
ADD templates/ /app/templates  
  
WORKDIR /app  
  
ENTRYPOINT ["/usr/bin/python","sloppytest.py"]  

