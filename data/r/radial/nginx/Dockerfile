# Spoke Dockerfile for nginx  
FROM radial/spoke-base:latest  
MAINTAINER Brian Clements <radial@brianclements.net>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get -q update && apt-get -qyV install \  
wget  
RUN echo "deb http://nginx.org/packages/ubuntu/ trusty nginx" >
/etc/apt/sources.list.d/nginx.list &&\  
wget -q -O /tmp/nginx.key http://nginx.org/keys/nginx_signing.key &&\  
apt-key add /tmp/nginx.key  
RUN apt-get -q update && apt-get -qyV install \  
curl libcurl3 bzip2 openssl ssl-cert sharutils libmcrypt4\  
nginx &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/*  
  
# Generate DH parameter  
RUN mkdir -p /etc/nginx/ssl &&\  
openssl dhparam -out /etc/nginx/ssl/dhparam.pem 2048  
  
# Set Spoke ID  
ENV SPOKE_NAME nginx  
  
COPY /entrypoint.sh /entrypoint.sh  
  
EXPOSE 80  
EXPOSE 443  

