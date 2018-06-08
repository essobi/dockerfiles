FROM debian:jessie  
  
MAINTAINER André Cianfarani <a.cianfarani@c2is.fr>  
  
RUN echo "deb http://ftp.es.debian.org/debian stable main contrib non-free" >
/etc/apt/sources.list  
RUN echo "deb-src http://ftp.es.debian.org/debian stable main contrib non-
free" >> /etc/apt/sources.list  
RUN echo "deb http://ftp.debian.org/debian/ wheezy-updates main contrib non-
free" >> /etc/apt/sources.list  
RUN echo "deb-src http://ftp.debian.org/debian/ wheezy-updates main contrib
non-free" >> /etc/apt/sources.list  
RUN echo "deb http://security.debian.org/ wheezy/updates main contrib non-
free" >> /etc/apt/sources.list  
RUN echo "deb-src http://security.debian.org/ wheezy/updates main contrib non-
free" >> /etc/apt/sources.list  
  
RUN apt-get update && apt-get -y install vim apache2 && apt-get clean  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
RUN mkdir /etc/apache2/ssl  
  
RUN /bin/ln -sf ../mods-available/ssl.conf /etc/apache2/mods-enabled/  
RUN /bin/ln -sf ../mods-available/ssl.load /etc/apache2/mods-enabled/  
ADD ports.conf /etc/apache2/ports.conf  
  
RUN usermod -u 1000 www-data  
  
EXPOSE 443  
RUN a2enmod proxy  
RUN a2enmod actions  
RUN a2enmod rewrite  
RUN a2enmod socache_shmcb  
RUN a2enmod proxy_http  
RUN a2enmod headers  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

