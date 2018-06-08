#Dockerfile lychee  
FROM tlnk/ubuntu:latest  
  
ARG VERSION  
ARG BUILD_DATE  
ARG VCS_REF  
  
EXPOSE 80  
#Install source + packages  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
git \  
apt-transport-https \  
apache2 \  
libapache2-mod-php \  
php-gd \  
php-json \  
php-mysql \  
php-curl \  
php-zip \  
php-imagick \  
php-mbstring  
  
#Setup site.conf and app  
COPY lychee.conf /etc/apache2/sites-available/000-default.conf  
COPY entrypoint /entrypoint  
  
RUN git clone https://github.com/electerious/Lychee.git /var/www/lychee && \  
chown -R www-data:www-data /var/www/lychee/ && \  
chmod -R 777 /var/www/lychee/uploads /var/www/lychee/data && \  
a2enmod rewrite && \  
echo "ServerName localhost" | tee /etc/apache2/conf-available/fqdn.conf && \  
a2enconf fqdn && \  
chmod +x /entrypoint/*sh && \  
chmod +x /entrypoint/entrypoint.d/*.sh  
  
#Cleaning  
RUN apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* /etc/apache2/sites-
available/default-ssl.conf && \  
rm -rf /var/www/html  
  
WORKDIR /var/www/lychee  
ENTRYPOINT ["/bin/bash", "/entrypoint/entrypoint.sh"]  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  
  
LABEL maintainer="support@tlnk.fr"  
LABEL org.label-schema.version=$VERSION  
LABEL org.label-schema.build-date=$BUILD_DATE  
LABEL org.label-schema.vcs-ref=$VCS_REF  
LABEL org.label-schema.vcs-url="https://github.com/tle06/Lychee.git"  
LABEL org.label-schema.name="lychee"  
LABEL org.label-schema.vendor="lychee"  
LABEL org.label-schema.schema-version="1.0"  

