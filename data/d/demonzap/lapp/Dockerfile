FROM debian:latest  
MAINTAINER ZapLin soldierzx0705@gmail.com  
  
RUN apt-get update && apt-get -y install apache2 libapache2-mod-php5  
RUN apt-get -y install postgresql php5-pgsql  
RUN a2enmod php5  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
  
RUN mkdir /share  
VOLUME ["/share"]  
# VOLUME ["/etc/postgresql", "/var/log/postgresql",
"/var/lib/postgresql","/var/www/html"]  
EXPOSE 80  
EXPOSE 5432  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.4/main/postgresql.conf  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
  
COPY pg_hba.conf /etc/postgresql/9.4/main/pg_hba.conf  
  
CMD /etc/init.d/postgresql start && /usr/sbin/apache2 -D FOREGROUND

