# Dockerfile for scottabernethy/debian  
FROM debian:jessie  
  
MAINTAINER Scott Abernethy <scott@pixietwin.com>  
  
# Install base tools (previously had installed git, htop, man, software-
properties-common, wget)  
RUN \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
locales \  
unzip \  
vim-tiny \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
# Install gosu for easy step-down from root  
RUN \  
curl -o /usr/local/bin/gosu -sSL
"https://github.com/tianon/gosu/releases/download/1.4/gosu-amd64" && \  
echo "6f3a72f474cafacb3c7b4a7397a1f37d82fcc27b596cbb66e4ea0a8ee92eee76
/usr/local/bin/gosu" | sha256sum -c && \  
chmod +x /usr/local/bin/gosu  
  
# Set the locale  
RUN dpkg-reconfigure locales && \  
locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8  
ENV LC_ALL C.UTF-8  
ENV TZ Pacific/Auckland  

