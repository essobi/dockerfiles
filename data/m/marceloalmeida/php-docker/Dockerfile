FROM debian:jessie-backports  
  
MAINTAINER Marcelo Almeida <marcelo.almeida@jumia.com>  
  
WORKDIR "/root"  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# INSTALL DEPENDENCIES  
RUN apt-get update && apt-get install -y curl apt-transport-https && \  
echo "deb https://packages.sury.org/php/ jessie main" | tee
/etc/apt/sources.list.d/sury.list && \  
echo "deb-src https://packages.sury.org/php/ jessie main" | tee -a
/etc/apt/sources.list.d/sury.list && \  
curl -s https://packages.sury.org/php/apt.gpg | apt-key add \- && \  
apt-get update && \  
apt-get install -y php7.2-cli php7.2-fpm && \  
apt-get autoremove --purge && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
CMD ["php", "-a"]  

