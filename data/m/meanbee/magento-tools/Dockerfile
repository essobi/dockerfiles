FROM meanbee/magento:5.6-cli  
  
MAINTAINER Tom Robertshaw <tom.robertshaw@meanbee.com>  
  
RUN apt-get update && apt-get install -y git groff mysql-client python-pip
sudo  
  
RUN docker-php-ext-install zip  
  
RUN pip install awscli  
  
# Download composer, magedbm, magerun and mageconfigsync  
RUN curl https://getcomposer.org/composer.phar -o /composer.phar & \  
curl https://s3-eu-west-1.amazonaws.com/magedbm-releases/magedbm.phar -o
/magedbm.phar & \  
curl http://files.magerun.net/n98-magerun-latest.phar -o /n98-magerun.phar & \  
curl -L
https://github.com/punkstar/mageconfigsync/releases/download/0.4.0/mageconfigsync-0.4.0.phar
-o /mageconfigsync.phar & \  
curl https://raw.githubusercontent.com/colinmollenhour/modman/master/modman -o
/modman & \  
wait  
  
RUN chmod +x /composer.phar  
RUN chmod +x /magedbm.phar  
RUN chmod +x /n98-magerun.phar  
RUN chmod +x /mageconfigsync.phar  
RUN chmod +x /modman  
  
# Copy wrappers commands  
COPY composer /usr/local/bin/  
COPY magerun /usr/local/bin/  
COPY magedbm /usr/local/bin/  
COPY magemm /usr/local/bin/  
COPY mageconfigsync /usr/local/bin/  
COPY modman /usr/local/bin/  
  
RUN chmod +x /usr/local/bin/composer  
RUN chmod +x /usr/local/bin/magerun  
RUN chmod +x /usr/local/bin/magedbm  
RUN chmod +x /usr/local/bin/magemm  
RUN chmod +x /usr/local/bin/mageconfigsync  
RUN chmod +x /usr/local/bin/modman  

