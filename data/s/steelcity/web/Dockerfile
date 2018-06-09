FROM thruio/docker-webapp:latest  
  
RUN apt-get update && \  
apt-get -yq install \  
php5-pspell \  
aspell-en \  
aspell-de \  
aspell-cy \  
aspell-fr && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN mkdir /etc/service/prune  
ADD docker/run.prune.sh /etc/service/prune/run  
RUN chmod +x /etc/service/*/run  
  
ADD . /app  
RUN composer install;

