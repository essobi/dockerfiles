FROM alpine:3.6  
  
RUN apk --update add python py-setuptools py-pip && \  
pip install elasticsearch-curator && \  
apk del py-pip && \  
rm -rf /var/cache/apk/*  

