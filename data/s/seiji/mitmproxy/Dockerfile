FROM alpine:latest  
  
ENV PYTHON_VERSION=2.7.9 \  
LANG=en_US.UTF-8  
RUN \  
apk --update add alpine-sdk libffi-dev libxml2-dev libxslt-dev libjpeg-turbo-
dev openssl-dev python-dev py-pillow && \  
wget "https://bootstrap.pypa.io/get-pip.py" -O /dev/stdout | python && \  
pip install mitmproxy  
  
RUN apk del --purge alpine-sdk openssl-dev && \  
rm -rf /var/cache/apk/* /tmp/* /var/tmp/*  
  
EXPOSE 8080  
CMD ["mitmproxy"]  

