FROM alpine:latest  
#FROM alpine:3.6  
MAINTAINER Michel Labbe  
  
RUN apk add --no-cache apache2 php5-apache2 \  
# fix "httpd: Could not reliably determine the server's fully qualified domain
name" error \  
&& sed -i '1s/^/ServerName localhost \r\n\r\n/' /etc/apache2/httpd.conf \  
# fix "could not create /run/apache2/httpd.pid" error \  
&& mkdir /run/apache2 \  
# Change listen port to a port greater than 1024 to allow a non-root user to
start Apache \  
&& sed -i 's/Listen\ 80/Listen\ 8080/g' /etc/apache2/httpd.conf \  
# Download and install Ookla Speedtest Mini \  
&& wget http://c.speedtest.net/mini/mini.zip -O /tmp/mini.zip \  
&& unzip /tmp/mini.zip -d /tmp/ \  
&& rm /tmp/mini.zip \  
&& mv /tmp/mini/index-php.html /tmp/mini/index.html \  
&& rm -f /tmp/mini/index-*.html \  
# Make sure default website dir is empty before moving files \  
&& rm -rf /var/www/localhost/htdocs/* \  
&& mv /tmp/mini/* /var/www/localhost/htdocs/ \  
&& adduser -S speedtest \  
&& chown -R speedtest /var/www/logs \  
&& chown -R speedtest /var/www/run \  
&& chown -R speedtest /var/log/apache2 \  
&& chown -R speedtest /run/apache2 \  
&& chown speedtest /usr/sbin/httpd  
  
USER speedtest  
  
# Listen to required port(s)  
EXPOSE 8080  
ENTRYPOINT ["/usr/sbin/httpd"]  
  
# /usr/sbin/httpd -D FOREGROUND  
CMD ["-D", "FOREGROUND"]

