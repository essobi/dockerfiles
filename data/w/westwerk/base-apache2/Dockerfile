FROM westwerk/base-ubuntu  
MAINTAINER Michael Ruettgers <mr@westwerk.ac>  
  
# Copy image related files  
COPY files/ /  
  
# Define packages to be installed  
ENV PACKAGES \  
apache2  
  
# Install packages && cleanup  
RUN apt-get update && \  
apt-get -y install $PACKAGES  
  
RUN ([ -d /etc/apache2/ssl ] || /bin/mkdir -p /etc/apache2/ssl) && \  
/bin/ln -s /etc/ssl/certs/ssl-cert-snakeoil.pem /etc/apache2/ssl/ssl-cert.pem
&& \  
/bin/ln -s /etc/ssl/private/ssl-cert-snakeoil.key /etc/apache2/ssl/ssl-
cert.key && \  
/bin/sed -i 's#/etc/ssl/certs/ssl-cert-snakeoil#/etc/apache2/ssl/ssl-cert#g'
/etc/apache2/sites-available/default-ssl.conf  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
RUN /usr/sbin/a2ensite default-ssl  
RUN /usr/sbin/a2enmod ssl rewrite headers mime deflate filter expires  
RUN /usr/sbin/a2enconf westwerk-security  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

