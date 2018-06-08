FROM ubuntu:14.04  
MAINTAINER Javier Jerónimo <jjeronimo@packagepeer.com>  
  
# HowTo build: sudo docker build --tag=packagepeer/api-proxy .  
  
# HowTo run: sudo docker run --link ...:api packagepeer/api-proxy  
  
#
################################################################################
Setup  
RUN \  
apt-get update && \  
apt-get install -y nginx-core && \  
rm -rf /var/lib/apt/lists/* && \  
echo "\ndaemon off;" >> /etc/nginx/nginx.conf && \  
chown -R www-data:www-data /var/lib/nginx  
  
WORKDIR /etc/nginx  
  
RUN mkdir -p /var/log/nginx/  
  
ADD etc/nginx/sites-enabled/proxy /etc/nginx/sites-enabled/proxy  
  
ADD pkgp-run.sh /pkgp-run.sh  
RUN chmod u+x /pkgp-run.sh  
  
EXPOSE 80  
  
#
################################################################################
Entry point  
CMD ["/pkgp-run.sh"]  

