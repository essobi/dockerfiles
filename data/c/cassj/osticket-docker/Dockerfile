FROM httpd  
MAINTAINER Cass Johnston <cassjohnston@gmail.com>  
  
RUN apt-get update && apt-get install -yqq wget bzip2 curl zlib1g-dev
libcurl4-openssl-dev vim build-essential libapr1-dev libaprutil1-dev
libxml2-dev zip mysql-client libpng12-dev libc-client2007e-dev libkrb5-dev
gettext git libgettextpo-dev sendmail libicu52 libicu-dev psmisc libldap2-dev
&& apt-get clean  
  
# Create a user & group (apache runs as this user)  
RUN groupadd --system osticket  
RUN useradd --system -g osticket osticket  
  
# Install PHP for this Apache  
COPY install_php.sh /tmp/install_php.sh  
RUN chmod +x /tmp/install_php.sh  
RUN /tmp/install_php.sh  
  
# PHP & Apache configuration  
COPY php.ini /usr/local/lib/php.ini  
COPY httpd.conf /usr/local/apache2/conf/httpd.conf  
COPY httpd-ssl.conf /usr/local/apache2/conf/extra/httpd-ssl.conf  
COPY httpd-vhosts.conf /usr/local/apache2/conf/extra/httpd-vhosts.conf  
  
# Install osticket  
COPY install_osticket.sh /tmp/install_osticket.sh  
RUN chmod +x /tmp/install_osticket.sh  
RUN /tmp/install_osticket.sh  
  
##VOLUME /usr/local/apache2/htdocs/osticket  
RUN chown -R osticket:osticket /usr/local/apache2/htdocs  
  
COPY setup_osticket.sh /tmp/setup_osticket.sh  
RUN chmod +x /tmp/setup_osticket.sh  
  
# Define default env vars for httpd - you can override these when you create
the container  
ENV SERVERNAME localhost  
ENV ADMINEMAIL root@localhost  
  
# and for php.ini  
ENV PHP_DATE_TIMEZONE Europe/London  
ENV PHP_POST_MAX_SIZE 8M  
ENV PHP_MEMORY_LIMIT 128M  
ENV PHP_DISPLAY_ERRORS Off  
ENV PHP_STARTUP_ERRORS Off  
  
CMD ["/bin/bash", "-mc", "/tmp/setup_osticket.sh"]  
  

