FROM ubuntu:17.04  
MAINTAINER https://github.com/mowfax/webControl_docker  
  
EXPOSE 443/tcp  
  
ENV PORT_PREFIX=3429 \  
ADMINUSER=admin \  
ADMINPASS=password  
  
RUN apt-get update -y && apt-get install -y curl  
  
# run from master branch:  
# RUN curl -s
https://raw.githubusercontent.com/3RaGaming/Web_Control/master/install.sh >
/install.sh && \  
# chmod +x /install.sh && \  
# /install.sh --silent && \  
# apt-get autoremove -y  
# run from temporary patch branch:  
RUN curl -s
https://raw.githubusercontent.com/mowfax/Web_Control/patch-1/install.sh >
/install.sh && \  
chmod +x /install.sh && \  
/install.sh --silent && \  
apt-get autoremove -y  
  
# enable user www-data to sudo screen and gcc  
COPY sudoers /etc/sudoers  
RUN adduser www-data sudo  
  
# increase upload filesize for webinterface  
RUN mv /etc/php/7.0/apache2/php.ini /etc/php/7.0/apache2/php_org.ini && \  
sed -e 's:upload_max_filesize = 2M:upload_max_filesize = 100M:' \  
-e 's:post_max_size = 8M:post_max_size = 100M:' /etc/php/7.0/apache2/php_org.ini > /etc/php/7.0/apache2/php.ini  
  
COPY ./docker-entrypoint.sh /  
  
CMD ["/bin/bash","/docker-entrypoint.sh"]  

