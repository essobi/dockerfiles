# Dockerfile to build web server in container images  
# Based on Ubuntu  
############################################################  
# Set the base image to Ubuntu  
FROM ubuntu:14.04  
# File Author / Maintainer  
MAINTAINER Alex lanxic@gmail.com  
# set env with noninteractive  
ENV DEBIAN_FRONTEND=noninteractive  
# Update the repository sources list  
RUN apt-get update  
  
# install auditional tools build-essential  
RUN apt-get install -y wget curl vim openssh-server build-essential  
  
# set key for container  
RUN mkdir -p /root/.ssh && chmod 0700 /root/.ssh  
COPY files/authorized_keys /root/.ssh/authorized_keys  
  
# initialing user ubuntu and group admin  
RUN groupadd admins  
RUN useradd -d /home/ubuntu -m ubuntu -s /bin/bash  
RUN usermod -aG admins ubuntu  
  
RUN mkdir -p /home/ubuntu/.ssh && chmod 0700 /home/ubuntu/.ssh  
COPY files/authorized_keys /home/ubuntu/.ssh/authorized_keys  
RUN chown -R ubuntu: /home/ubuntu/.ssh/ -fR  
  
# initialing user and group git  
RUN groupadd -g 10000 git  
RUN useradd -u 10000 -g 10000 -d /home/git -m git -s /bin/bash  
  
RUN mkdir -p /home/git/.ssh && chmod 0700 /home/git/.ssh  
COPY files/authorized_keys /home/git/.ssh/authorized_keys  
RUN chown -R git: /home/git/.ssh/ -fR  
  
COPY files/sudoers-admins /etc/sudoers.d/admins  
  
################## BEGIN INSTALLATION ######################  
# Install Apache2 Following the Instructions at Apache2 Docs  
# Install Apache2 package  
RUN apt-get install -y apache2 mysql-client git  
  
# remove mpm_prefork because this will be conflic with mpm_event  
RUN rm -f /etc/apache2/mods-available/mpm_prefork.*  
# enable module  
RUN a2enmod access_compat  
RUN a2enmod alias  
RUN a2enmod auth_basic  
RUN a2enmod authn_file  
RUN a2enmod authn_core  
RUN a2enmod authz_core  
RUN a2enmod authz_host  
RUN a2enmod authz_user  
RUN a2enmod autoindex  
RUN a2enmod deflate  
RUN a2enmod dir  
RUN a2enmod env  
RUN a2enmod expires  
RUN a2enmod filter  
RUN a2enmod headers  
RUN a2enmod mime  
RUN a2enmod mpm_event  
RUN a2enmod negotiation  
RUN a2enmod proxy_fcgi  
RUN a2enmod proxy_http  
RUN a2enmod proxy  
RUN a2enmod remoteip  
RUN a2enmod rewrite  
RUN a2enmod setenvif  
RUN a2enmod socache_shmcb  
RUN a2enmod status  
  
# installing php5  
RUN apt-get update  
RUN apt-get install -y php5-fpm php5-curl php5-mcrypt php5-mysql php5-gd
php5-cli  
RUN mv /etc/php5/fpm/pool.d/www.conf /etc/php5/fpm/pool.d/www.disabled  
COPY files/php-fpm.default /etc/php5/fpm/pool.d/default.conf  
  
# Set default container command  
COPY files/start.sh /start.sh  
ENTRYPOINT /bin/sh /start.sh  

