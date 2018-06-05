FROM alpine:3.3  
MAINTAINER Marc Richter <richter_marc@gmx.net>  
  
ENV GID=991 UID=991 VERSION=trunk DBHOST=dbhost DBUSER=postfix DBNAME=postfix
DBS=mysqli  
  
RUN echo "@commuedge http://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories \  
&& apk -U add \  
nginx \  
php-fpm \  
php-imap \  
php-mysql \  
php-mysqli \  
php-pgsql \  
dovecot \  
subversion \  
supervisor \  
tini@commuedge \  
&& rm -f /var/cache/apk/*  
  
RUN mkdir -p /etc/supervisor.d /postfixadmin ; svn co
http://svn.code.sf.net/p/postfixadmin/code/trunk /postfixadmin  
  
COPY config.local.php /postfixadmin/config.local.php  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY php-fpm.conf /etc/php/php-fpm.conf  
COPY postfixadmin.ini /etc/supervisor.d/postfixadmin.ini  
COPY startup /usr/local/bin/startup  
  
RUN chmod +x /usr/local/bin/startup ; \  
chown ${UID}:${GID} -R /etc/supervisor.d /postfixadmin  
  
EXPOSE 80  
CMD ["tini","--","startup"]  

