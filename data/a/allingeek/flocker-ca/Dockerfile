FROM alpine:3.4  
RUN apk --no-cache add python python-dev py-pip build-base ca-certificates gcc
libffi-dev linux-headers openssl-dev && \  
pip install --upgrade pip && \  
pip install https://clusterhq-
archive.s3.amazonaws.com/python/Flocker-1.15.0-py2-none-any.whl  
CMD flocker-ca \--help  

