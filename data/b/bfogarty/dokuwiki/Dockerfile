FROM ubuntu:14.04  
MAINTAINER Brian Fogarty <bri@nfogarty.me>  
  
ENV DOKUWIKI_VERSION 2017-02-19a  
ENV MD5_CHECKSUM 78e8c27291fbc3de04c7f107c3f7725a  
  
RUN apt-get update && \  
apt-get install -y wget lighttpd php5-cgi php5-gd php5-ldap && \  
wget -q -O /dokuwiki.tgz
"http://download.dokuwiki.org/src/dokuwiki/dokuwiki-$DOKUWIKI_VERSION.tgz" &&
\  
if [ "$MD5_CHECKSUM" != "$(md5sum /dokuwiki.tgz | awk '{print($1)}')" ];then
echo "Checksum does not match downloaded file."; exit 1; fi && \  
mkdir /dokuwiki && \  
tar -zxf dokuwiki.tgz -C /dokuwiki --strip-components 1 && \  
rm dokuwiki.tgz && \  
apt-get clean && \  
apt-get autoremove && \  
rm -rf /tmp/* /var/tmp/* && \  
rm -rf /var/lib/apt/lists/*  
  
RUN chown -R www-data:www-data /dokuwiki  
  
ADD dokuwiki.conf /etc/lighttpd/conf-available/20-dokuwiki.conf  
RUN lighty-enable-mod dokuwiki fastcgi accesslog  
RUN mkdir /var/run/lighttpd && chown www-data.www-data /var/run/lighttpd  
  
EXPOSE 80  
VOLUME
["/dokuwiki/data/","/dokuwiki/lib/plugins/","/dokuwiki/conf/","/dokuwiki/lib/tpl/","/var/log/"]  
  
ENTRYPOINT ["/usr/sbin/lighttpd", "-D", "-f", "/etc/lighttpd/lighttpd.conf"]  
  

