FROM ubuntu:15.10  
  
RUN apt-get update \  
&& apt-get upgrade -y --no-install-recommends  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
openssl  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
apache2  
  
RUN rm -Rf /var/www/html \  
&& rm -f /apache2/sites-enabled/000-default.conf \  
&& rm -f /apache2/sites-available/000-default.conf  
  
#Copy configuration and content for deault site, foo.com (http sample),
bar.com (https sample) and real-foo  
ADD apache2 /etc/apache2  
ADD www /var/www  
  
RUN chmod -R 755 /var/www  
  
  
#Enable SSL support and create a selfsigned certificate for bar.com  
RUN a2enmod proxy proxy_http proxy_html substitute deflate xml2enc rewrite ssl
\  
&& mkdir /etc/apache2/ssl \  
&& mkdir /etc/apache2/ssl/bar \  
&& openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout
/etc/apache2/ssl/bar/bar.key -out /etc/apache2/ssl/bar/bar.crt -subj
"/C=ES/ST=Madrid/L=Madrid/O=Byteflair/OU=Docker Team/CN=bar.com"  
  
  
EXPOSE 80 443  
  
VOLUME ["/var/www", "/var/log/apache2", "/etc/apache2"]  
  
ENTRYPOINT ["apache2ctl","-DFOREGROUND","-d /etc/apache2","-e INFO"]

