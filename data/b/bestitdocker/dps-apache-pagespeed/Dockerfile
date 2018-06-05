FROM ubuntu:xenial  
MAINTAINER Alexander Schneider <alexanderschneider85@gmail.com>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update -q \  
&& DEBIAN_FRONTEND=noninteractive apt-get dist-upgrade -y \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -y openssl apache2 wget  
  
# Add custom config  
ADD httpd.conf /etc/apache2/sites-enabled/000-default.conf  
ADD run.sh /usr/bin/run  
RUN chmod +x /usr/bin/run  
RUN a2enmod proxy_http proxy_fcgi ssl rewrite  
  
# Add pagespeed  
RUN wget https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-
beta_current_amd64.deb \  
&& dpkg -i mod-pagespeed-*.deb \  
&& apt-get -f install  
  
ENV APP_DIR '/var/www/app'  
ENV SSL_COUNTRY 'DE'  
ENV SSL_STATE 'BW'  
ENV SSL_CITY 'FREIBURG'  
ENV SSL_COMPANY 'best it'  
ENV SSL_HOST 'localhost'  
EXPOSE 80 443  
CMD ["/bin/bash", "/usr/bin/run"]

