FROM babim/ubuntubase  
  
RUN apt-get update && \  
apt-get install software-properties-common -y && \  
add-apt-repository ppa:ondrej/apache2 -y && apt-get update && \  
apt-get install apache2 libapache2-mod-fcgid inetutils-ping telnet -y --force-
yes && \  
a2enmod proxy proxy_fcgi rewrite headers http2 ssl && \  
wget https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-
stable_current_amd64.deb && dpkg -i mod-pagespeed-stable_current_amd64.deb &&
rm -f mod-pagespeed-stable_current_amd64.deb && \  
apt-get clean && \  
apt-get autoclean && \  
apt-get autoremove && \  
rm -rf /var/lib/apt/lists/*  
  
# Define mountable directories.  
VOLUME ["/var/log/apache2", "/var/www", "/etc/apache2"]  
RUN mkdir -p /etc-start/apache2 && cp -R /etc/apache2/* /etc-start/apache2 &&
\  
mkdir -p /etc-start/www && cp -R /var/www/* /etc-start/www  
  
# Set Apache environment variables (can be changed on docker run with -e)  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_SERVERADMIN admin@localhost  
ENV APACHE_SERVERNAME localhost  
ENV APACHE_SERVERALIAS docker.localhost  
ENV APACHE_DOCUMENTROOT /var/www  
  
EXPOSE 80 443  
ADD start.sh /start.sh  
RUN chmod 0755 /start.sh  
CMD ["/start.sh"]  

