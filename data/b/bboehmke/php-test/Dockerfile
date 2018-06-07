FROM bboehmke/php:7-fpm  
  
# install doxygen dependencies  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -y install graphviz && \  
rm -rf /var/lib/apt/lists/*  
# install doxygen  
RUN curl -sS
http://ftp.stack.nl/pub/users/dimitri/doxygen-1.8.11.linux.bin.tar.gz | tar
xvz --strip-components=2 -C /usr/local/bin/ doxygen-1.8.11/bin/  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  

