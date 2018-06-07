FROM symball/docker-images:base_php7  
MAINTAINER Simon Ball <open-source@simonball.me>  
  
USER root  
  
RUN apk --update add \  
php7-mysqlnd \  
php7-pdo_mysql \  
php7-pdo_sqlite  
  
WORKDIR /srv  
  
CMD ["/bin/bash"]

