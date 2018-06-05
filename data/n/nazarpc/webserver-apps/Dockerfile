FROM nazarpc/webserver:php-fpm-v1  
MAINTAINER Nazar Mokrynskyi <nazar@mokrynskyi.com>  
  
RUN \  
  
# We'll need LibreOffice for Documents app  
  
apt-get update && \  
apt-get upgrade -y && \  
apt-get install --no-install-recommends -y libreoffice && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

