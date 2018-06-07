# VERSION 0.1  
# AUTHOR: Lionel Déglise <lionel.deglise@e-cosi.com>  
# DESCRIPTION: Image with DokuWiki & lighttpd with plantuml support  
# CREDIT: based on mprasil/dokuwiki  
# TO_BUILD: docker build -t e-cosi/dokuwiki .  
# TO_RUN: docker run -d -p 80:80 --name my_wiki e-cosi/dokuwiki  
FROM ubuntu:trusty  
MAINTAINER Lionel Deglise <lionel.deglise@e-cosi.com>  
  
# Set the version you want of DokuWiki  
ENV DOKUWIKI_VERSION 2017-02-19e  
ENV DOKUWIKI_CSUM 09bf175f28d6e7ff2c2e3be60be8c65f  
  
ENV LAST_REFRESHED 28. september 2017  
# Update & install packages & cleanup afterwards  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install wget lighttpd unzip php5-cgi php5-gd php5-sqlite && \  
apt-get clean autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}  
  
# Download & check & deploy dokuwiki & cleanup  
RUN wget -q -O /dokuwiki.tgz
"http://download.dokuwiki.org/src/dokuwiki/dokuwiki-$DOKUWIKI_VERSION.tgz" &&
\  
if [ "$DOKUWIKI_CSUM" != "$(md5sum /dokuwiki.tgz | awk '{print($1)}')" ];then
echo "Wrong md5sum of downloaded file!"; exit 1; fi && \  
mkdir -p /var/www/dokuwiki && \  
tar -zxf dokuwiki.tgz -C /var/www/dokuwiki --strip-components 1 && \  
rm dokuwiki.tgz  
  
# Set up ownership  
RUN chown -R www-data:www-data /var/www/dokuwiki  
  
# Configure lighttpd  
ADD dokuwiki.conf /etc/lighttpd/conf-available/20-dokuwiki.conf  
RUN lighty-enable-mod dokuwiki fastcgi accesslog  
RUN mkdir /var/run/lighttpd && chown www-data.www-data /var/run/lighttpd  
  
EXPOSE 80  
VOLUME
["/var/www/dokuwiki/data/","/var/www/dokuwiki/lib/plugins/","/var/www/dokuwiki/conf/","/var/www/dokuwiki/lib/tpl/","/var/log/"]  
  
ENTRYPOINT ["/usr/sbin/lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

