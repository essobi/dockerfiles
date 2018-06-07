FROM debian:stretch-slim  
  
MAINTAINER Andras Foldesi <andras.foldesi@novadin.com>  
  
RUN apt-get update && \  
apt-get install -y wget && \  
apt-get install -y php7.0-cli && \  
apt-get install -y php7.0-curl && \  
apt-get install -y php7.0-zip && \  
apt-get install -y unzip && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
mkdir /app && \  
cd /app && \  
wget https://github.com/getgrav/grav/releases/download/1.2.4/grav-v1.2.4.zip
&& \  
unzip grav-v1.2.4.zip && \  
rm -f grav-v1.2.4.zip && \  
mv grav www_root && \  
cd www_root && \  
bin/gpm install archives -n && \  
bin/gpm install feed -n && \  
bin/gpm install simplesearch -n && \  
bin/gpm install sitemap -n && \  
bin/gpm install taxonomylist -n && \  
chown -R www-data:www-data /app/www_root  
  
VOLUME ["/app"]  
  
CMD ["/bin/sh"]

