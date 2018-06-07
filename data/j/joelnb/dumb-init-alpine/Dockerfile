FROM alpine:latest  
MAINTAINER Joel Noyce Barnham <joelnbarnham@gmail.com>  
  
RUN \  
apk add --update \  
python \  
python-dev \  
py-pip \  
build-base \  
&& \  
pip install dumb-init && \  
apk del \  
python \  
python-dev \  
py-pip \  
build-base \  
&& \  
rm -rf /var/cache/apk/* && \  
:  
  
ENTRYPOINT ["dumb-init"]  
CMD ["/bin/sh"]  

