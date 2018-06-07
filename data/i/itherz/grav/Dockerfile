FROM phusion/baseimage:0.9.18  
MAINTAINER Ahumaro Mendoza <ahumaro@ahumaro.com>, Dmitrii Zolotov
<dzolotov@herzen.spb.ru>  
  
CMD ["/sbin/my_init"]  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
#Install core packages  
RUN apt-get update -q && apt-get upgrade -y -q && apt-get install -y -q php5
php5-cli php5-fpm php5-gd php5-curl php5-apcu ca-certificates nginx git-core
&& apt-get clean -q && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#Get Grav  
RUN rm -fR /usr/share/nginx/html/ && git clone
https://github.com/getgrav/grav.git /usr/share/nginx/html/  
  
#Install Grav  
WORKDIR /usr/share/nginx/html/  
RUN bin/composer.phar self-update  
RUN bin/grav install  
RUN chown www-data:www-data . && chown -R www-data:www-data *  
  
RUN find . -type f | xargs -d '\n' chmod 664  
RUN find . -type d | xargs -d '\n' chmod 775  
RUN find . -type d | xargs -d '\n' chmod +s  
  
RUN umask 0002 && chmod 777 -R assets && \  
chmod +x bin/gpm  
RUN sed -i 's/allow_url_fopen.*/allow_url_fopen = Off/ig'
/etc/php5/cli/php.ini && \  
sed -i 's/allow_url_fopen.*/allow_url_fopen = Off/ig' /etc/php5/fpm/php.ini  
RUN bin/gpm install -y admin youtube snappygrav toc tidyhtml pages-json
shortcodes markdown-color logerrors instagram gravstrap markdown-sections
leaflet data-manager breadcrumbs highlight pagination random simplesearch
taxonomylist github lightslider relatedpages page-inject optimus read_later
metadata_extended external_links mathjax filesource qrcode && \  
echo "Europe/Moscow" > /etc/timezone && dpkg-reconfigure tzdata  
  
#Configure Nginx - enable gzip  
RUN sed -i 's|# gzip_types| gzip_types|' /etc/nginx/nginx.conf  
  
#Setup Grav configuration for Nginx  
RUN touch /etc/nginx/grav_conf.sh && chmod +x /etc/nginx/grav_conf.sh && echo
'#!/bin/bash \n\  
echo "" > /etc/nginx/sites-available/default \n\  
ok="0" \n\  
while IFS="" read line \n\  
do \n\  
if [ "$line" = "server {" ]; then \n\  
ok="1" \n\  
fi \n\  
if [ "$ok" = "1" ]; then \n\  
echo "$line" >> /etc/nginx/sites-available/default \n\  
fi \n\  
if [ "$line" = "}" ]; then \n\  
ok="0" \n\  
fi \n\  
done < /usr/share/nginx/html/webserver-configs/nginx.conf' >>
/etc/nginx/grav_conf.sh  
  
RUN /etc/nginx/grav_conf.sh && sed -i \  
-e 's|root html|root /usr/share/nginx/html|' \  
-e 's|127.0.0.1:9000;|unix:/var/run/php5-fpm.sock;|' \  
-e 's|/home/USER/www/html|/usr/share/nginx/html|ig' \  
/etc/nginx/sites-available/default  
  
#Setup Php service  
RUN mkdir -p /etc/service/php5-fpm && touch /etc/service/php5-fpm/run && chmod
+x /etc/service/php5-fpm/run && echo '#!/bin/bash \n\  
exec /usr/sbin/php5-fpm -F' >> /etc/service/php5-fpm/run  
  
#Setup Nginx service  
RUN mkdir -p /etc/service/nginx && touch /etc/service/nginx/run && chmod +x
/etc/service/nginx/run && echo '#!/bin/bash \n\  
exec /usr/sbin/nginx -g "daemon off;"' >> /etc/service/nginx/run  
  
RUN mkdir /init && cd /usr/share/nginx/html/user/ && cp -R . /init/  
  
RUN mkdir -p /etc/service/mrun  
ADD run /etc/service/mrun/run  
  
#Expose configuration and content volumes  
VOLUME /usr/share/nginx/html/user  
  
#Public ports  
EXPOSE 80  

