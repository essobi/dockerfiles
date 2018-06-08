# VERSION 0.1  
# AUTHOR: Miroslav Prasil <miroslav@prasil.info>  
# DESCRIPTION: Image with DokuWiki & lighttpd  
# TO_BUILD: docker build -t mprasil/dokuwiki .  
# TO_RUN: docker run -d -p 80:80 --name my_wiki mprasil/dokuwiki  
FROM ubuntu:16.04  
MAINTAINER Miroslav Prasil <miroslav@prasil.info>  
  
# Set the version you want of Twiki  
ARG S3_BUCKET  
ARG AWS_ACCESS_KEY_ID  
ARG AWS_SECRET_ACCESS_KEY  
ARG AWS_DEFAULT_REGION  
ENV S3_BUCKET=${S3_BUCKET}  
ENV AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}  
ENV AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}  
ENV AWS_DEFAULT_REGION=${AWS_DEFAULT_REGION}  
ENV DOKUWIKI_VERSION=2017-02-19e  
ENV DOKUWIKI_CSUM=09bf175f28d6e7ff2c2e3be60be8c65f  
  
# Update & install packages & cleanup afterwards  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install \  
wget \  
lighttpd \  
php-cgi \  
php-gd \  
php-ldap \  
php-curl \  
php-xml \  
php-mbstring \  
fuse \  
rsync \  
unzip \  
s3fs && \  
apt-get clean autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}  
  
# Configure lighttpd  
ADD dokuwiki.conf /etc/lighttpd/conf-available/20-dokuwiki.conf  
RUN lighty-enable-mod dokuwiki fastcgi accesslog  
RUN mkdir /var/run/lighttpd && chown www-data.www-data /var/run/lighttpd  
  
COPY docker-startup.sh /startup.sh  
  
EXPOSE 80  
  
ENTRYPOINT ["/startup.sh"]  
CMD ["run"]  

