##  
# Jb Nahan PHP 7.2 container  
##  
FROM macintoshplus/php:base  
MAINTAINER Jean-Baptiste Nahan <jean-baptiste@nahan.fr>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY certs/ /root/  
COPY install.sh /root/install.sh  
RUN chmod +x /root/install.sh  
RUN /root/install.sh  
  
COPY bin/fixright /  
RUN chmod +x /fixright  
  
VOLUME /sources  
  
WORKDIR /sources  
  

