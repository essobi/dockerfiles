FROM debian:latest  
MAINTAINER Ghislain LE MEUR <my.email@gmail.com>  
# Install base packages  
RUN apt-get update && \  
apt-get -yq install \  
apache2 \  
libapache2-mod-php5 && \  
touch /etc/update-startup && \  
rm -rf /tmp/* /var/tmp/*  
  
#USER root  
EXPOSE 80 443  
WORKDIR /var/www  
#VOLUME /etc/apache2/sites-enabled  
#VOLUME /var/log/apache  
CMD ["apache2", "-D", "FOREGROUND"]  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN chmod +x /usr/local/bin/docker-entrypoint.sh  
COPY docker-entrypoint-initdb.d/ /docker-entrypoint-initdb.d/  
#HEALTHCHECK --interval=5m --timeout=3s \  
# CMD curl -f http://localhost/ || exit 1  

