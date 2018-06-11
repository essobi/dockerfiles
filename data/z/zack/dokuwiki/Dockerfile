FROM ubuntu:14.04  
MAINTAINER YuLun Shih <shih@yulun.me>  
  
RUN apt-get update && \  
apt-get install -y nginx php5-fpm php5-gd php5-ldap curl && \  
rm -rf /var/lib/apt/lists/*  
  
ENV DOKUWIKI_VERSION 2014-09-29d  
ENV MD5_CHECKSUM 2bf2d6c242c00e9c97f0647e71583375  
  
RUN mkdir -p /var/www \  
&& cd /var/www \  
&& curl -O
"http://download.dokuwiki.org/src/dokuwiki/dokuwiki-$DOKUWIKI_VERSION.tgz" \  
&& echo "$MD5_CHECKSUM dokuwiki-$DOKUWIKI_VERSION.tgz" | md5sum -c - \  
&& tar xzf "dokuwiki-$DOKUWIKI_VERSION.tgz" \--strip 1 \  
&& rm "dokuwiki-$DOKUWIKI_VERSION.tgz"  
  
RUN echo "cgi.fix_pathinfo = 0;" >> /etc/php5/fpm/php.ini  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
RUN rm /etc/nginx/sites-enabled/*  
ADD dokuwiki.conf /etc/nginx/sites-enabled/  
RUN mkdir -p /dokuwiki \  
&& rm -rf /var/www/data/pages /var/www/data/meta /var/www/data/media \  
/var/www/data/media_attic /var/www/data/media_meta /var/www/data/attic \  
&& ln -s /dokuwiki/data/pages /var/www/data/pages \  
&& ln -s /dokuwiki/data/meta /var/www/data/meta \  
&& ln -s /dokuwiki/data/media /var/www/data/media \  
&& ln -s /dokuwiki/data/media_attic /var/www/data/media_attic \  
&& ln -s /dokuwiki/data/media_meta /var/www/data/media_meta \  
&& ln -s /dokuwiki/data/attic /var/www/data/attic \  
&& rm -rf /var/www/conf && ln -s /dokuwiki/conf /var/www/conf \  
&& chown -R www-data:www-data /var/www  
  
EXPOSE 80  
VOLUME ["/dokuwiki", "/var/log/lighttpd"]  
  
CMD /usr/sbin/php5-fpm && /usr/sbin/nginx  

