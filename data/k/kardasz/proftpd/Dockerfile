FROM debian:jessie  
MAINTAINER Krzysztof Kardasz <krzysztof@kardasz.eu>  
  
# Update system and install required packages  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install git, download and extract Stash and create the required directory
layout.  
# Try to limit the number of RUN instructions to minimise the number of layers
that will need to be created.  
RUN apt-get update -qq \  
&& apt-get install -y wget curl proftpd openssl \  
&& apt-get clean autoclean \  
&& apt-get autoremove --yes \  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  
  
  
# FTP Port  
EXPOSE 21  
  
CMD ["proftpd", "-n"]

