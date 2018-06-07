FROM alpine:latest  
  
MAINTAINER hinkelsteinli <hinkelsteinli@hinkelstein.li>  
  
RUN apk update && \  
apk upgrade && \  
apk add apache2 apache2-utils && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir /web && \  
chown apache:apache /web  
  
RUN sed -i 's#^DocumentRoot ".*#DocumentRoot "/web/html"#g'
/etc/apache2/httpd.conf && \  
sed -i 's#ServerTokens.*#ServerTokens Prod#g' /etc/apache2/httpd.conf && \  
sed -i 's#AllowOverride [Nn]one#AllowOverride All#' /etc/apache2/httpd.conf &&
\  
sed -i 's#^ServerRoot .*#ServerRoot /web#g' /etc/apache2/httpd.conf && \  
sed -i 's/^#ServerName.*/ServerName webproxy/' /etc/apache2/httpd.conf && \  
sed -i 's#^IncludeOptional /etc/apache2.*#IncludeOptional /web/conf.d#g'
/etc/apache2/httpd.conf && \  
sed -i 's#Directory "/var/www/localhost/htdocs.*#Directory "/web/html" >#g'
/etc/apache2/httpd.conf && \  
sed -i 's/Options Indexes/Options /g' /etc/apache2/httpd.conf && \  
sed -i 's#/var/log/apache2/#/web/logs/#g' /etc/logrotate.d/apache2  
  
RUN mkdir -p /web/conf.d && \  
mkdir /web/html && \  
mkdir /web/logs && \  
mkdir -p /run/apache2 && \  
ln -s /usr/lib/apache2 /web/modules  
  
RUN echo '<Directory "/web">' > /web/conf.d/default.conf && \  
echo ' AllowOverride All' >> /web/conf.d/default.conf && \  
echo ' # Allow open access:' >> /web/conf.d/default.conf && \  
echo ' Require all granted' >> /web/conf.d/default.conf && \  
echo '</Directory>' >> /web/conf.d/default.conf  
  
RUN echo hello world > /web/html/index.html  
  
# Volumes  
VOLUME /web  
  
# Exposed Ports  
EXPOSE 80  
# Start Service  
CMD /usr/sbin/httpd -D FOREGROUND  

