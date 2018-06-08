# Base docker image  
FROM ubuntu:14.04  
  
# Docker image for OE-lite.org buildbot master data container  
MAINTAINER Esben Haabendal <esben@haabendal.dk>  
  
# Setup buildbot user  
RUN useradd -r -m -d /srv/buildbot -s /bin/bash buildbot && \  
install -o buildbot -g buildbot -d /srv/buildbot/master  
USER buildbot  
  
VOLUME /srv/buildbot/master  
  
CMD ["echo", "Data container for buildbot-master"]  

