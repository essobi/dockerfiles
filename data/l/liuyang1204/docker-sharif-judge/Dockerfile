FROM ubuntu:latest  
  
RUN \  
apt-get install -y software-properties-common && \  
echo oracle-java8-installer shared/accepted-oracle-license-v1-1 select true |
debconf-set-selections && \  
add-apt-repository -y ppa:webupd8team/java && \  
apt-get update && \  
apt-get install -y oracle-java8-installer php5 php5-cli gcc g++ perl
php5-pgsql php5-mysql make apache2 && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /var/cache/oracle-jdk8-installer  
  
RUN rm -rf /var/www/html && mkdir -p /var/lock/apache2 /var/run/apache2
/var/log/apache2 /var/www/html && chown -R www-data:www-data /var/lock/apache2
/var/run/apache2 /var/log/apache2 /var/www/html  
  
RUN a2dismod mpm_event && a2enmod mpm_prefork && a2enmod rewrite  
  
RUN mv /etc/apache2/apache2.conf /etc/apache2/apache2.conf.dist && rm
/etc/apache2/conf-enabled/* /etc/apache2/sites-enabled/*  
COPY apache2.conf /etc/apache2/apache2.conf  
  
COPY apache2-foreground /usr/local/bin/  
WORKDIR /var/www/html  
  
COPY html /var/www/html  
COPY data /data  
  
RUN cd /data/tester/easysandbox && chmod +x runalltests.sh runtest.sh && make
runtests  
  
RUN chown -R www-data:www-data /var/www/html /data  
  
ENV DB_DRIVER postgre  
ENV DB_HOST localhost  
ENV DB_USER postgres  
ENV DB_PASS postgres  
ENV DB_NAME oj  
  
EXPOSE 80  
CMD ["apache2-foreground"]  
  

