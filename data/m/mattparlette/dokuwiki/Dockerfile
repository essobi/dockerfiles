# VERSION 0.5  
# AUTHOR: Matthew Parlette <matthew.parlette@gmail.com>  
# ORIGINAL AUTHOR: Miroslav Prasil <miroslav@prasil.info>  
# DESCRIPTION: Image with DokuWiki & lighttpd  
# TO_BUILD: docker build -t mattparlette/dokuwiki .  
# TO_RUN: docker run -d -p 80:80 --name my_wiki mattparlette/dokuwiki  
# This assumes dokuwiki has been extracted in a local directory  
# This docker image should be used with https://github.com/matthew-
parlette/dokuwiki-formula  
FROM ubuntu:14.04  
MAINTAINER Matthew Parlette <matthew.parlette@gmail.com>  
  
# Update & install packages & cleanup afterwards  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get -y install wget lighttpd php5-cgi php5-gd php5-ldap php5-curl && \  
apt-get clean autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/{apt,dpkg,cache,log}  
  
# Configure lighttpd  
ADD dokuwiki.conf /etc/lighttpd/conf-available/20-dokuwiki.conf  
RUN lighty-enable-mod dokuwiki fastcgi accesslog  
RUN mkdir /var/run/lighttpd && chown www-data.www-data /var/run/lighttpd  
  
EXPOSE 80  
  
ENTRYPOINT ["/usr/sbin/lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

