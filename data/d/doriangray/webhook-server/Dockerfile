FROM php:7.1-apache  
  
# Enable apache mod rewrite  
RUN a2enmod rewrite  
  
# Install docker  
RUN apt-get update \  
&& apt-get dist-upgrade -y \  
&& apt-get install apt-transport-https ca-certificates -y \  
&& echo deb https://apt.dockerproject.org/repo debian-jessie main >
/etc/apt/sources.list.d/docker.list \  
&& apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 \--recv-keys
58118E89F3A912897C070ADBF76221572C52609D \  
&& apt-get update \  
&& apt-cache policy docker-engine \  
&& apt-get install docker-engine -y \--force-yes  
  
# Install sudo and grant docker access for user www-data  
RUN apt-get update \  
&& apt-get install sudo -y \--force-yes \  
&& echo "www-data ALL=(ALL) NOPASSWD: /usr/bin/docker" >> /etc/sudoers  
  
COPY src /var/www/html

