FROM ubuntu:16.04  
RUN apt-get -y update && apt-get -y \  
install postgresql postgis \  
apache2 php ibapache2-mod-php7.0 php-zip php-curl php-gd php-ldap php-pgsql
libapache2-mod-jk php-xml \  
unzip supervisor  
RUN phpenmod xml  
  
ADD indicia_setup.sh indicia_setup.sh  
ADD postgres_setup.sh postgres_setup.sh  
RUN chmod gou+x /postgres_setup.sh  
RUN chmod gou+x /indicia_setup.sh  
  
RUN mkdir -p /var/lock/apache2 /var/run/apache2 /var/log/supervisor  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN mkdir /var/www/html/indicia  
RUN chown www-data:www-data /var/www/html/indicia  
  
COPY dump-1.32.0.sql dump-1.32.0.sql  
  
USER www-data  
  
ADD 1.32.0 /  
  
USER root  
RUN /indicia_setup.sh  
USER postgres  
  
RUN echo $HOME  
RUN /etc/init.d/postgresql start &&\  
/postgres_setup.sh  
  
# Adjust PostgreSQL configuration so that remote connections to the  
# database are possible.  
RUN echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/9.5/main/pg_hba.conf  
  
# And add ``listen_addresses`` to ``/etc/postgresql/9.5/main/postgresql.conf``  
RUN echo "listen_addresses='*'" >> /etc/postgresql/9.5/main/postgresql.conf  
  
# Resize shared_buffers  
RUN sed -i -e 's/shared_buffers = 128MB/shared_buffers = 512MB/g'
/etc/postgresql/9.5/main/postgresql.conf  
  
# Expose the PostgreSQL port  
EXPOSE 80 5432  
USER root  
  
CMD ["/usr/bin/supervisord"]  

