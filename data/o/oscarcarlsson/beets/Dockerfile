FROM alpine:latest  
MAINTAINER Oscar Carlsson <oscar.carlsson@gmail.com>  
  
ENV VERSION v1.3.17  
  
# This points beets towards our external volume mount, for config and db files  
ENV BEETSDIR /config  
  
RUN adduser -D -u 1000 beets users  
  
RUN apk add \--update python py-pip && \  
apk add \--update faac faad2 ffmpeg flac lame libvorbis opus && \  
pip install -U pip && \  
pip install -U beets requests pylast  
  
# Script that user can run to populate a config file  
ADD src/init_config.sh /usr/local/bin/init_config.sh  
RUN chmod +x /usr/local/bin/init_config.sh  
ADD src/config.yaml /home/beets/config.yaml  
  
USER beets  
  
VOLUME ["/config", "/music", "/working", "/convert"]  
  
WORKDIR /working  
  
ENTRYPOINT ["/usr/bin/beet"]  

