FROM php:7.0-apache  
  
#Enable tideways repository  
RUN echo 'deb http://s3-eu-west-1.amazonaws.com/qafoo-profiler/packages debian
main' > /etc/apt/sources.list.d/tideways.list && \  
curl -sS 'https://s3-eu-west-1.amazonaws.com/qafoo-
profiler/packages/EEB5E8F4.gpg' | apt-key add -  
  
#Install php extension and Graphviz (dot binary is used to display graphs)  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get -yq install tideways-php graphviz && \  
apt-get autoremove --assume-yes && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
#Enable tideways module and conf  
RUN echo
'extension=tideways.so\ntideways.auto_prepend_library=0\nprofiler.output_dir=/traces'
> /usr/local/etc/php/conf.d/tideways.ini  
  
#Copy app in container  
COPY ./html /var/www/html/  
COPY ./lib /var/www/lib/  
  
#Set www-data uid/gid to the host owner uid/gid (generally 1000:1000)  
RUN usermod -u 1000 www-data  
RUN groupmod -g 1000 www-data  
  
#This is where you should link your XHProf traces  
VOLUME ["/traces"]  

