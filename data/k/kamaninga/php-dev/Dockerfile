FROM kamaninga/php  
  
COPY conf/ /opt/docker/  
  
RUN /usr/local/bin/apk-install \  
graphviz \  
php7-xdebug \  
&& docker-service-enable syslog ssh \  
&& /opt/docker/bin/provision run --tag bootstrap \--role webdevops-dev \--role
webdevops-php-dev \  
&& /opt/docker/bin/bootstrap.sh \  
&& docker-image-cleanup  

