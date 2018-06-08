FROM gtrias/node-consul-template  
  
MAINTAINER Genar <genar@acs.li>  
  
WORKDIR /app  
  
RUN echo "deb http://httpredir.debian.org/debian jessie-backports main non-
free\ndeb-src http://httpredir.debian.org/debian jessie-backports main non-
free" >> /etc/apt/sources.list.d/backports.list && \  
apt-get update && \  
apt-get install certbot -y -t jessie-backports && \  
apt-get clean && \  
mkdir -p /var/www/letsencrypt  

