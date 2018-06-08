FROM saschaegerer/php-fpm:5.6  
USER root  
  
ARG DEBIAN_FRONTEND=noninteractive  
  
RUN set -xe && \  
apt-get update && \  
apt-get install --no-install-recommends -y imagemagick php5.6-mysqli
php5.6-intl php5.6-curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
COPY z_typo3.ini /etc/php/5.6/mods-available/  
  
RUN phpenmod z_typo3  
  
USER www-data  
  
ENV TYPO3_CONTEXT Production  

