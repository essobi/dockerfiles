FROM migros/cf-deploy-php7.0:latest  
  
MAINTAINER smartive AG <hello@smartive.ch>  
  
RUN sed -i "s/httpredir.debian.org/debian.ethz.ch/g" /etc/apt/sources.list  
RUN find /etc/apt/sources.list.d/ -type f -exec sed -i
's/httpredir.debian.org/debian.ethz.ch/g' {} \;  
  
# install additional PHP packages  
RUN apt-get update && \  
apt-get install -y git \  
curl \  
mysql-client \  
vim \  
nano \  
php7.0-fpm \  
php7.0-mcrypt \  
php7.0-imap \  
php7.0-gd && \  
apt-get clean && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  
  
ADD ./docker/php-fpm/symfony.ini /etc/php/7.0/fpm/conf.d/  
ADD ./docker/php-fpm/symfony.ini /etc/php/7.0/cli/conf.d/  
  
ADD ./docker/php-fpm/symfony.pool.conf /etc/php/7.0/fpm/pool.d/  
  
ADD ./docker/ssh-agent.sh /ssh-agent.sh  
ADD ./docker/run.sh /run.sh  
  
WORKDIR /app  
  
CMD ["/run.sh"]  

