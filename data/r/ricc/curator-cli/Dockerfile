FROM alpine:3.6  
RUN apk --update add python py-setuptools py-pip && \  
pip install elasticsearch-curator==5.4.1 && \  
pip install certifi && \  
apk del py-pip && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/curator_cli"]  

