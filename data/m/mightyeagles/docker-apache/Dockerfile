FROM alpine:latest  
  
MAINTAINER Ashik Patel <ashik.kalavadiya@gmail.com>  
  
RUN apk update && apk upgrade && \  
  
# info of build  
printf "Build of mighty-eagles/docker-apache, date: %s\n" `date -u +"%d/%m/%Y
T%H:%M:%SZ"` >> /etc/BUILD && \  
  
apk add apache2 libxml2-dev apache2-utils && \  
mkdir /webdev/ && chown -R apache.www-data /webdev && \  
  
#replace all default parameters as per our requirement  
sed -i 's#^DocumentRoot ".*#DocumentRoot "/webdev/html"#g'
/etc/apache2/httpd.conf && \  
sed -i 's#AllowOverride none#AllowOverride All#' /etc/apache2/httpd.conf && \  
sed -i 's#^ServerRoot .*#ServerRoot /webdev#g' /etc/apache2/httpd.conf && \  
sed -i 's/^#ServerName.*/ServerName webdevproxy/' /etc/apache2/httpd.conf && \  
sed -i 's#^IncludeOptional /etc/apache2/conf#IncludeOptional
/webdev/config/conf#g' /etc/apache2/httpd.conf && \  
sed -i 's#PidFile "/run/.*#Pidfile "/webdev/run/httpd.pid"#g'
/etc/apache2/conf.d/mpm.conf && \  
sed -i 's#Directory "/var/www/localhost/htdocs.*#Directory "/webdev/html" >#g'
/etc/apache2/httpd.conf && \  
sed -i 's#Directory "/var/www/localhost/cgi-bin.*#Directory "/webdev/cgi-bin"
>#g' /etc/apache2/httpd.conf && \  
  
sed -i 's#/var/log/apache2/#/webdev/logs/#g' /etc/logrotate.d/apache2 && \  
sed -i 's/Options Indexes/Options /g' /etc/apache2/httpd.conf && \  
  
#remove all cache of downloaded packages  
rm -rf /var/cache/apk/*  
  
RUN mkdir /scripts/  
  
ADD run.sh /scripts/run.sh  
  
RUN chmod -R 755 /scripts  
  
#sharable vaolume to host  
VOLUME /webdev  
  
#sharable ports to host  
EXPOSE 80 443  
  
ENTRYPOINT ["/scripts/run.sh"]  

