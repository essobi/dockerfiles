FROM debian:jessie-slim  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY apt-install.sh /usr/local/bin/apt-install  
COPY apt-purge.sh /usr/local/bin/apt-purge  
  
RUN useradd -m -s /bin/bash -G audio,video user  

