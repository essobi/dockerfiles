FROM tsari/wheezy-apache-php  
MAINTAINER Tibor Sári <tiborsari@gmx.de>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get upgrade -y  
  
# install php and apache and clean up to minimize the image size  
RUN apt-get install -y \  
php5-dev \  
php-pear \  
openssh-server \  
make \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# install xdebug and use our own xdebug configuration  
RUN pecl install xdebug  
COPY xdebug/xdebug.ini /etc/php5/apache2/conf.d/20-xdebug.ini  
RUN sed -i -e '1izend_extension=\'`find / -name "xdebug.so"`
/etc/php5/apache2/conf.d/20-xdebug.ini  
  
# add an user for later ssh connection (remote phpunit)  
# sshd configuration  
COPY ssh/sshd_config /etc/ssh/sshd_config  
COPY ssh/docker-insecure-rsa.public.key /home/docker/docker-insecure-
rsa.public.key  
RUN adduser --disabled-password --gecos '' docker && \  
mkdir /var/run/sshd && \  
mkdir /home/docker/.ssh && \  
cat /home/docker/docker-insecure-rsa.public.key >
/home/docker/.ssh/authorized_keys2 && \  
chown -R docker:docker /home/docker  
  
EXPOSE 22  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
CMD ["/usr/bin/supervisord"]

