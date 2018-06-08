FROM ubuntu:16.04  
ARG LOVE_VERSION=0.10.2  
# Install some helpful utilities for building things.  
RUN apt-get update && apt-get -y install \  
binutils \  
curl \  
graphviz \  
lua5.1 \  
luarocks \  
make \  
snapcraft \  
xz-utils \  
zip  
  
# Install some Lua modules.  
RUN for package in \  
lunatest \  
lrandom \  
luasocket \  
; do luarocks install $package; done  
  
# Install LÖVE itself.  
RUN curl -LO
https://bitbucket.org/rude/love/downloads/love_${LOVE_VERSION}ppa1_amd64.deb \  
&& curl -LO
https://bitbucket.org/rude/love/downloads/liblove0_${LOVE_VERSION}ppa1_amd64.deb
\  
&& apt -y install ./liblove0_${LOVE_VERSION}ppa1_amd64.deb \  
&& apt -y install ./love_${LOVE_VERSION}ppa1_amd64.deb  

