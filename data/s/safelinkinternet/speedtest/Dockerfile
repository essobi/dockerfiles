FROM alpine:latest  
  
MAINTAINER Safelink Internet  
  
ENV Title Speedtest  
  
RUN apk --update add apache2 php-apache2 && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/apk/* && \  
# fix "httpd: Could not reliably determine the server's fully qualified domain
name" error && \  
sed -i '1s/^/ServerName localhost \r\n\r\n/' /etc/apache2/httpd.conf && \  
# fix "could not create /run/apache2/httpd.pid" error && \  
mkdir /run/apache2 && \  
# Download and install Ookla Speedtest Mini && \  
wget http://c.speedtest.net/mini/mini.zip -O /tmp/mini.zip && \  
unzip /tmp/mini.zip -d /tmp/ && \  
rm /tmp/mini.zip && \  
# mv /tmp/mini/index-php.html /tmp/mini/index.html && \  
rm -f /tmp/mini/index-*.html && \  
# Make sure default website dir is empty before moving files && \  
rm -rf /var/www/localhost/htdocs/* && \  
mv /tmp/mini/* /var/www/localhost/htdocs/  
  
#Adding Custom files  
ADD index.html /var/www/localhost/htdocs/index.html  
  
# Listen to required ports  
EXPOSE 80  
  
ENTRYPOINT ["/usr/sbin/httpd"]  
  
# /usr/sbin/httpd -D FOREGROUND  
CMD ["-D", "FOREGROUND"]  

