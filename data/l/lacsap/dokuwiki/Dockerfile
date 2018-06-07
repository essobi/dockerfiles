############################################################  
# Dockerfile to build a Dokuwiki server  
############################################################  
  
FROM debian:8  
  
# Install Requirements  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
wget \  
lighttpd \  
php5-cgi \  
php5-gd  
  
# Getting dokuwiki  
RUN wget http://download.dokuwiki.org/src/dokuwiki/dokuwiki-stable.tgz -O
dokuwiki.tgz  
RUN mkdir /data  
RUN tar -zxf dokuwiki.tgz -C /data --strip-components 1  
RUN rm dokuwiki.tgz  
  
# Permission  
RUN chown -R www-data:www-data /data  
  
# Configuring lighttpd  
COPY dokuwiki.conf /etc/lighttpd/conf-available/20-dokuwiki.conf  
RUN lighty-enable-mod dokuwiki fastcgi accesslog  
RUN mkdir /var/run/lighttpd && chown www-data.www-data /var/run/lighttpd  
  
EXPOSE 80  
VOLUME ["/data"]  
ENTRYPOINT ["/usr/sbin/lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  

