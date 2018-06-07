FROM alpine:3.5  
MAINTAINER GP Orcullo  
  
ENV FP_VER 4.2.2  
  
RUN apk add --no-cache curl dnsmasq freeswitch-flite nginx php7-curl php7-fpm
\  
php7-imap php7-json php7-mcrypt php7-odbc php7-pdo php7-pdo_pgsql \  
php7-pgsql php7-session php7-sqlite3 php7-xml php7 postgresql \  
supervisor \  
&& echo "pid /tmp/nginx.pid;" >> /etc/nginx/nginx.conf \  
&& sed -e 's_nobody_nginx_g' \  
-e 's_127.0.0.1:9000_/tmp/fpm.sock_g' \  
-e 's_;listen.o_listen.o_g' \  
-e 's_;listen.g_listen.g_g' \  
-e 's_;listen.m_listen.m_g' \  
-i /etc/php7/php-fpm.d/www.conf \  
&& ln /usr/bin/php7 /usr/bin/php \  
&& cd /var/www \  
&& curl -L https://github.com/fusionpbx/fusionpbx/archive/${FP_VER}.tar.gz |
tar xzf - \  
&& mv fusionpbx*/ fusionpbx \  
&& chown -Rf nginx:nginx fusionpbx \  
&& chmod -R 755 fusionpbx/secure \  
&& rm -rf /etc/freeswitch/* \  
&& cp -R /var/www/fusionpbx/resources/templates/conf/* /etc/freeswitch \  
&& mkdir /usr/share/freeswitch/scripts \  
&& chown -R nginx:nginx /etc/freeswitch \  
&& chown -R nginx:nginx /var/lib/freeswitch \  
&& chown -R nginx:nginx /usr/share/freeswitch \  
&& chown -R nginx:nginx /var/log/freeswitch \  
&& chown -R nginx:nginx /var/run/freeswitch \  
&& mkdir /etc/fusionpbx \  
&& chown -R nginx:nginx /etc/fusionpbx \  
&& mkdir -p /data.org/lib /data.org/share /data \  
&& chmod 0777 -R /data.org \  
&& mv /etc/freeswitch /etc/fusionpbx /var/log /data.org \  
&& mv /var/lib/freeswitch /data.org/lib/freeswitch \  
&& mv /usr/share/freeswitch /data.org/share/freeswitch \  
&& ln -sf /data/freeswitch /etc/freeswitch \  
&& ln -sf /data/lib/freeswitch /var/lib/freeswitch \  
&& ln -sf /data/share/freeswitch /usr/share/freeswitch \  
&& ln -sf /data/fusionpbx /etc/fusionpbx \  
&& ln -sf /data/log /var/log \  
&& ln -sf /data.org/freeswitch /data/freeswitch \  
&& ln -sf /data.org/lib /data/lib \  
&& ln -sf /data.org/share /data/share \  
&& ln -sf /data.org/fusionpbx /data/fusionpbx \  
&& ln -sf /data.org/log /data/log \  
&& touch /data/.ok  
  
ENV PGDATA /data/postgresql  
  
VOLUME /data  
  
ADD fusionpbx /etc/nginx/conf.d/default.conf  
ADD start-freeswitch.sh /usr/bin  
ADD start-postgresql.sh /usr/bin  
ADD supervisord.conf /etc/  
ADD start.sh /  
  
CMD /start.sh  

