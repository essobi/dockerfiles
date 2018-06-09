FROM stevenliebregt/alpine-base  
  
MAINTAINER Steven Liebregt <dev.s.liebregt@gmail.com>  
  
COPY root/. /  
  
RUN apk update && apk upgrade && \  
  
apk add apache2 libxml2-dev apache2-utils && \  
mkdir /web/ && chown -R apache.www-data /web && \  
  
sed -i 's#^DocumentRoot ".*#DocumentRoot "/web/html/default/public"#g'
/etc/apache2/httpd.conf && \  
sed -i 's#AllowOverride [Nn]one#AllowOverride All#' /etc/apache2/httpd.conf &&
\  
sed -i 's#^ServerRoot .*#ServerRoot /web#g' /etc/apache2/httpd.conf && \  
sed -i 's/^#ServerName.*/ServerName webproxy/' /etc/apache2/httpd.conf && \  
sed -i 's#^IncludeOptional /etc/apache2/conf#IncludeOptional
/web/config/conf#g' /etc/apache2/httpd.conf && \  
sed -i 's#PidFile "/run/.*#Pidfile "/web/run/httpd.pid"#g'
/etc/apache2/conf.d/mpm.conf && \  
sed -i 's#Directory "/var/www/localhost/htdocs.*#Directory "/web/html" >#g'
/etc/apache2/httpd.conf && \  
sed -i 's#Directory "/var/www/localhost/cgi-bin.*#Directory "/web/cgi-bin"
>#g' /etc/apache2/httpd.conf && \  
  
sed -i 's#/var/log/apache2/#/web/logs/#g' /etc/logrotate.d/apache2 && \  
sed -i 's/Options Indexes/Options /g' /etc/apache2/httpd.conf && \  
  
sed -i '/LoadModule rewrite_module.*/s/^#//g' /etc/apache2/httpd.conf && \  
  
rm -rf /var/cache/apk/*  
  
VOLUME /web  
  
EXPOSE 80 443  

