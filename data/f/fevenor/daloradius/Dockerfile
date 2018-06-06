FROM alpine  
  
MAINTAINER fevenor <fevenor@outlook.com>  
  
  
# Set up runing environment  
RUN apk add --update lighttpd php-common php-gd fcgi php-cgi php-mysql php-
pear \  
&& pear install DB \  
&& rm -rf /var/cache/apk/* \  
  
# Configure Lighttpd  
&& set -x \  
&& sed -i 's/# include \"mod_fastcgi.conf\"/include \"mod_fastcgi.conf\"/'
/etc/lighttpd/lighttpd.conf \  
&& touch /var/log/daloradius.log \  
&& chown -R lighttpd:lighttpd /var/log/daloradius.log  
  
  
# Get the web  
ADD htdocs /var/www/localhost/htdocs  
  
# Configure daloRADIUS  
ADD config.sh /root/  
  
ENV DB_HOST_VALUE=localhost  
ENV DB_PORT_VALUE=3306  
ENV DB_USER_VALUE=radius  
ENV DB_PASS_VALUE=radpass  
ENV DB_NAME_VALUE=radius  
  
EXPOSE 80  
EXPOSE 443  
CMD /root/config.sh;lighttpd -D -f /etc/lighttpd/lighttpd.conf  

