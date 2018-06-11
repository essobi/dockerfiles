FROM alpine  
MAINTAINER Yusuf Ali "ali@yusuf.email"  
# install required packages  
RUN \  
apk --no-cache --update add \  
rtorrent \  
openvpn \  
lighttpd \  
php5 \  
php5-cgi \  
fcgi \  
tzdata \  
curl \  
lighttpd-mod_auth \  
php5-json \  
git && \  
mkdir -p /session /home/abc /downloads && \  
mkdir -p /var/run/lighttpd /run/lighttpd && \  
chown lighttpd /var/run/lighttpd /run/lighttpd && \  
addgroup -g 1000 abc && \  
adduser -DH -G abc -g "" -s /bin/sh abc && \  
chown abc:abc /downloads && \  
chown abc:abc /session && \  
sed -i 's/php\\-cgi/php-cgi5/g' /etc/lighttpd/mod_fastcgi.conf && \  
ln -s /usr/bin/php5 /usr/bin/php  
  
ADD root/ /  
  
EXPOSE 80  
VOLUME /downloads /vpn /config /session  
  
ENTRYPOINT ["/root/startup"]  

