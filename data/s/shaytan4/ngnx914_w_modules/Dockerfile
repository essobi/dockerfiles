FROM ubuntu:14.04.4  
# Version 0.1  
# run docker build --rm -t ubuntu:viy . # to build image  
MAINTAINER Viy <shaytan4@gmail.com>  
  
# Update base image  
# Add sources for latest nginx  
# Install software requirements  
RUN apt-get update && \  
apt-get install -y software-properties-common && \  
apt-get install wget dpkg-dev build-essential zlib1g-dev libpcre3 libpcre3-dev
git unzip lua5.1 liblua5.1-0 liblua5.1-0-dev -y  
  
RUN add-apt-repository ppa:maxmind/ppa && \  
apt-get update && \  
apt-get install libmaxminddb0 libmaxminddb-dev mmdb-bin -y  
  
#RUN sudo add-apt-repository ppa:nginx/development  
#RUN sudo apt-get update  
##BUILD_PACKAGES="supervisor nginx php5-fpm git php5-mysql php-apc php5-curl
php5-gd php5-intl php5-mcrypt php5-memcache php5-sqlite php5-tidy php5-xmlrpc
php5-xsl php5-pgsql php5-mongo php5-ldap pwgen" && \  
#RUN BUILD_PACKAGES="php5-fpm unzip bash git php5-mysql ssh tcpdump nmap vim
mc php-apc php5-curl php5-gd php5-intl php5-mcrypt php5-memcache php5-sqlite
php5-tidy php5-xmlrpc php5-xsl php5-pgsql php5-mongo php5-ldap pwgen" && \  
RUN BUILD_PACKAGES="telnet supervisor unzip bash git ssh tcpdump nmap vim mc"
&& \  
apt-get -y install $BUILD_PACKAGES && \  
apt-get remove --purge -y software-properties-common && \  
apt-get autoremove -y && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /usr/share/man/?? && \  
rm -rf /usr/share/man/??_*  
  
RUN mkdir -p /etc/apt/sources.list.d/  
RUN echo "deb http://nginx.org/packages/mainline/ubuntu/ trusty nginx" >
/etc/apt/sources.list.d/nginx.list  
RUN echo "deb-src http://nginx.org/packages/mainline/ubuntu/ trusty nginx" >>
/etc/apt/sources.list.d/nginx.list  
RUN wget http://nginx.org/keys/nginx_signing.key && \  
apt-key add nginx_signing.key && apt-get update && \  
apt-get upgrade -y && apt-get dist-upgrade -y  
  
# -------------------------------  
RUN mkdir /root/custom-nginx && \  
cd /root/custom-nginx && \  
apt-get source nginx=1.9.14 && apt-get build-dep nginx -y && \  
mkdir -p /root/custom-nginx/nginx-1.9.14/debian/modules && \  
cd /root/custom-nginx/nginx-1.9.14/debian/modules && \  
wget -O "nginx_lua.zip" "https://github.com/openresty/lua-nginx-
module/archive/master.zip" && \  
wget -O "redis2-nginx-module.zip" "https://github.com/openresty/redis2-nginx-
module/archive/master.zip" && \  
wget -O "ngx_pagespeed.zip"
"https://github.com/pagespeed/ngx_pagespeed/archive/master.zip" && \  
wget -O "ngx_http_geoip2_module.zip"
"https://github.com/leev/ngx_http_geoip2_module/archive/master.zip" && \  
unzip nginx_lua.zip && \  
unzip redis2-nginx-module.zip && \  
unzip ngx_pagespeed.zip && \  
unzip ngx_http_geoip2_module.zip && \  
rm nginx_lua.zip && \  
rm redis2-nginx-module.zip && \  
rm ngx_pagespeed.zip && \  
rm ngx_http_geoip2_module.zip && \  
cd ngx_pagespeed-master && \  
wget https://dl.google.com/dl/page-speed/psol/1.11.33.0.tar.gz && \  
tar -zxf 1.11.33.0.tar.gz && \  
rm 1.11.33.0.tar.gz  
# -----------------------------  
ADD scripts/rules /root/custom-nginx/nginx-1.9.14/debian/rules  
RUN chmod 755 /root/custom-nginx/nginx-1.9.14/debian/rules  
RUN cd /root/custom-nginx/nginx-1.9.14/ && \  
dpkg-buildpackage -b && cd .. && \  
dpkg -i nginx_1.9.14-1~trusty_amd64.deb  
  
RUN apt-get autoremove && apt-get autoclean  
# Configuring timezone  
RUN cp /usr/share/zoneinfo/Europe/Kiev /etc/localtime  
  
RUN mkdir -p /etc/nginx/ssl/  
ADD conf/nginx.conf /etc/nginx/nginx.conf  
ADD conf/ssl/* /etc/nginx/ssl/  
  
# Supervisor Config  
ADD conf/supervisord.conf /etc/supervisord.conf  
  
RUN mkdir -p /var/www/nginx && chown www-data:www-data /var/www/nginx  
  
VOLUME ["/var/www"]  
  
# add test PHP file  
ADD src/index.html /var/www/nginx/index.html  
ADD src/index.php /var/www/nginx/index.php  
RUN chown -Rf www-data.www-data /var/www/nginx  
RUN mkdir /var/run/sshd  
RUN chown root:root /var/run/sshd  
RUN chmod 755 /var/run/sshd  
  
# Expose Ports  
EXPOSE 443  
EXPOSE 80  
EXPOSE 22  
EXPOSE 9000  
#CMD ["/etc/init.d/nginx", "start"]  
CMD ["/usr/sbin/nginx", "-g", "daemon off;"]  
#CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisord.conf"]  

