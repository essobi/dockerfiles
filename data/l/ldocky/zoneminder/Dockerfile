FROM ubuntu:xenial  
MAINTAINER ldocky  
  
VOLUME ["/config", "/var/cache/zoneminder"]  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update  
RUN apt-get install -y software-properties-common  
RUN add-apt-repository -y ppa:iconnor/zoneminder  
RUN apt-get update  
RUN apt-get install -y mysql-server \  
apache2 \  
php7.0 \  
libapache2-mod-php \  
php7.0-mysql \  
nano \  
curl \  
zoneminder  
  
RUN adduser www-data video  
RUN chmod 775 /etc/zm/zm.conf  
RUN chown root:www-data /etc/zm/zm.conf  
RUN chown -R www-data:www-data /usr/share/zoneminder  
RUN a2enconf zoneminder && \  
a2enmod cgi && \  
a2enmod rewrite && \  
a2enmod ssl  
RUN echo sql_mode = NO_ENGINE_SUBSTITUTION >>
/etc/mysql/mysql.conf.d/mysqld.cnf  
  
EXPOSE 80 443  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY scripts/startup.sh /startup.sh  
RUN chmod 777 /startup.sh  
ENTRYPOINT ["/startup.sh"]  

