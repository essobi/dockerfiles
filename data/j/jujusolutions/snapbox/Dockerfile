FROM ubuntu:16.04  
VOLUME "/snaps"  
  
RUN apt-get update -qq -y && \  
apt-get install -y \  
build-essential \  
bzr \  
git \  
openssh-client \  
snapcraft \  
snapd \  
unzip  
  
WORKDIR /snaps  
ENTRYPOINT snapcraft clean  
ENTRYPOINT snapcraft  

