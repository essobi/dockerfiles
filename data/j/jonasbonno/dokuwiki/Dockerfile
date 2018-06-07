FROM alpine:3.6  
  
MAINTAINER Jonas Bonno Mikkelsen (https://github.com/JonasBonno)  
  
RUN apk --no-cache add \  
php7 php7-openssl php7-fpm php7-gd php7-session php7-xml php7-zlib nginx
supervisor curl tar  
  
RUN mkdir -p /run/nginx && \  
mkdir -p /var/www && \  
cd /var/www && \  
curl -O -L
"https://download.dokuwiki.org/src/dokuwiki/dokuwiki-2018-04-22a.tgz" && \  
tar -xzf dokuwiki-*.tgz \--strip 1 && \  
rm dokuwiki-*.tgz  
  
ADD nginx.conf /etc/nginx/nginx.conf  
ADD supervisord.conf /etc/supervisord.conf  
ADD start.sh /start.sh  
  
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php7/php-fpm.ini && \  
sed -i -e "s|;daemonize\s*=\s*yes|daemonize = no|g" /etc/php7/php-fpm.conf &&
\  
sed -i -e "s|listen\s*=\s*127\\.0\\.0\\.1:9000|listen = /var/run/php-
fpm7.sock|g" /etc/php7/php-fpm.d/www.conf && \  
sed -i -e "s|;listen\\.owner\s*=\s*|listen.owner = |g" /etc/php7/php-
fpm.d/www.conf && \  
sed -i -e "s|;listen\\.group\s*=\s*|listen.group = |g" /etc/php7/php-
fpm.d/www.conf && \  
sed -i -e "s|;listen\\.mode\s*=\s*|listen.mode = |g" /etc/php7/php-
fpm.d/www.conf && \  
chmod +x /start.sh  
  
EXPOSE 80  
VOLUME
["/var/www/data/","/var/www/lib/plugins/","/var/www/conf/","/var/www/lib/tpl/"]  
  
CMD /start.sh  

