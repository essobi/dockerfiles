# Pull base image.  
FROM strongloop/strong-pm  
  
# File Author.  
MAINTAINER Robert Hänsel <robert@travojo.net>  
  
USER root  
  
RUN rm /etc/localtime && \  
ln -sf /usr/share/zoneinfo/Europe/Berlin /etc/localtime  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y graphicsmagick && \  
rm -rf /var/lib/apt/lists/*  
  
USER strong-pm  

