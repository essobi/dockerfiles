FROM debian:jessie  
MAINTAINER tgagor, https://github.com/tgagor  
# Install rsync  
RUN apt-get update \  
&& apt-get install -y rsync gzip openssh-client curl \  
&& apt-get autoremove -y \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD ["/usr/bin/rsync"]  

