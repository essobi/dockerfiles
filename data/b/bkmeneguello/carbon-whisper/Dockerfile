FROM alpine:3.6  
  
ARG WHISPER_VERSION=1.0.2  
ARG CARBON_VERSION=1.0.2  
RUN apk add \--no-cache python python-dev py-pip git gcc musl-dev &&\  
pip install --no-cache-dir -U pip setuptools &&\  
pip install --no-cache-dir git+https://github.com/graphite-
project/whisper.git@1.0.2 &&\  
pip install --no-cache-dir git+https://github.com/graphite-
project/carbon.git@1.0.2 &&\  
apk del --no-cache python-dev git gcc musl-dev &&\  
rm -rf /tmp/*  
  
#VOLUME /opt/graphite/conf  
VOLUME /opt/graphite/storage  
  
EXPOSE 2003 2004 7002  
  
ADD run.sh /  
  
ENTRYPOINT ["/run.sh"]  

