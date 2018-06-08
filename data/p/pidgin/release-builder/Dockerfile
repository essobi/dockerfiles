FROM debian:jessie  
  
RUN echo deb-src http://httpredir.debian.org/debian jessie main >>
/etc/apt/sources.list && \  
apt-get update && \  
apt-get build-dep -y pidgin && \  
apt-get install -y \--no-install-recommends mercurial ca-certificates libtool
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists*  
  

