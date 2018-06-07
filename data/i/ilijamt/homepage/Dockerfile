FROM debian:stretch  
  
MAINTAINER Ilija Matoski <ilijamt@gmail.com>  
  
# Install base required applications  
RUN apt-get update  
RUN apt-get install -yqq --no-install-recommends \  
wget \  
rsync \  
curl \  
sudo \  
sshpass \  
openssh-client  
  
# cleanup and optimization  
RUN apt-get install -yqq --no-install-recommends \  
jpegoptim \  
optipng \  
yui-compressor  
  
# node.js  
RUN apt-get install -y gnupg2  
RUN curl -sL https://deb.nodesource.com/setup_8.x | sudo -E bash -  
RUN apt-get install -y nodejs  
RUN npm install gulp -g  
  
# Download hugo  
RUN wget --no-check-certificate
https://github.com/gohugoio/hugo/releases/download/v0.30.2/hugo_0.30.2_Linux-64bit.deb
\  
&& dpkg -i hugo_0.30.2_Linux-64bit.deb  
  
# Cleanup image  
RUN apt-get clean -y \  
&& apt-get autoclean -y \  
&& apt-get autoremove -y  
  
# Delete all the unneceseary things  
RUN rm -rf /usr/share/locale/* && \  
rm -rf /var/cache/debconf/* && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /usr/share/doc/*  

