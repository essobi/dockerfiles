FROM alpine:3.4  
ARG CURATOR_VERSION="5.1.2"  
RUN apk --update add python py-setuptools py-pip && \  
pip install elasticsearch-curator==${CURATOR_VERSION} && \  
apk del py-pip && \  
rm -rf /var/cache/apk/*  
  
ENTRYPOINT ["/usr/bin/curator"]  

