############################################################  
# Dockerfile to build Catchall HTTP container images  
# Based on php:7.2  
############################################################  
  
# Set the base image to php:7.0  
FROM php:7.2-apache  
  
# File Author / Maintainer  
MAINTAINER Probably Rational Ltd.  
  
#Set the work directory  
WORKDIR /var/www/html  
  
# Installl a sweet ass profile  
RUN curl -o ~/.bashrc
https://gist.githubusercontent.com/hcaz/1f98157bd8ae8c647ffb3ab243d69fc8/raw/.bashrc  
COPY motd /etc/motd  
RUN chmod 600 /etc/motd  
  
# Update the repository sources list  
RUN apt update --fix-missing  
  
# Install essentials  
RUN apt install -y git curl wget zip unzip htop nano ncdu screen sshfs sl
cowsay python-minimal openssh-server  
RUN apt install -y cron monit  
  
# Install Composer  
RUN mkdir -p ~/.composer/vendor/bin  
RUN curl -o installer.php https://getcomposer.org/installer && php
installer.php --install-dir ~/.composer/vendor/bin && rm installer.php  
  
# Clean up  
RUN rm -rf /var/www/*  
  
# Configure apache  
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf  
RUN a2enmod status rewrite  
  
# Copy in required files  
COPY app/ /var/www/html/  
  
# Add a crontab  
RUN touch crontab.tmp && echo '*/5 * * * * curl -fsS --retry 3
https://hchk.io/$healthcheck > /dev/null' > crontab.tmp && crontab crontab.tmp
&& rm -rf crontab.tmp  
  
# Make composer work globally ;)  
RUN mv ~/.composer/vendor/bin/composer.phar ~/.composer/vendor/bin/composer  
  
# Setup Monit  
COPY monitrc /etc/monit/monitrc  
RUN chmod 600 /etc/monit/monitrc  
  
# Expose ports  
EXPOSE 80  
EXPOSE 2812  
  
ENTRYPOINT service ssh start && service apache2 start && monit&& /bin/bash  

