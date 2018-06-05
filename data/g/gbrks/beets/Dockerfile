FROM alpine:latest  
MAINTAINER Gavin Brooks <gavin@brks.io>  
  
ENV VERSION 1.4.6  
  
# This points beets towards our external volume mount, for config and db files  
ENV BEETSDIR /config  
  
RUN adduser -D -u 1000 beets users  
  
RUN apk add \--update python py-pip && \  
pip install -U pip && \  
pip install -U beets==$VERSION requests pylast  
  
# Script that user can run to populate a config file  
ADD src/init_config.sh /usr/local/bin/init_config.sh  
RUN chmod +x /usr/local/bin/init_config.sh  
ADD src/config.yaml /home/beets/config.yaml  
  
USER beets  
  
VOLUME ["/config", "/music", "/working"]  
  
WORKDIR /working  
  
ENTRYPOINT ["/usr/bin/beet"]  

