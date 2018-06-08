FROM alpine  
RUN apk update  
RUN apk add pjsua  
RUN apk add \--update bash  
RUN apk add \--no-cache python && \  
python -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip install --upgrade pip setuptools && \  
rm -r /root/.cache  
  
RUN mkdir -p /opt/sipmqtt  

