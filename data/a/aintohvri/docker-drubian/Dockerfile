FROM debian:6  
MAINTAINER Ain Tohvri <ain@flashbit.net>  
  
ENV USERNAME deploy  
  
# Apache environment variables. Override in Compose if required.  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_SERVERADMIN admin@localhost  
ENV APACHE_SERVERNAME drupal.dev  
ENV APACHE_SERVERALIAS www.docker.dev  
ENV APACHE_DOCUMENTROOT /var/www  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update && apt-get install -y \  
debconf-utils \  
apt-utils \  
curl \  
git \  
wget \  
imagemagick \  
vim \  
apache2 \  
php5 \  
libapache2-mod-php5 \  
sudo \  
php5-curl  
  
# Necessary to fall through Drupal installation.  
ADD config/dbconfig-common/drupal6.conf /etc/dbconfig-common/drupal6.conf  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -y drupal6 drush  
  
RUN adduser --disabled-password --gecos '' $USERNAME  
RUN mkdir -p $HOME/.ssh  
RUN touch $HOME/.ssh/known_hosts  
RUN usermod -a -G sudo,www-data $USERNAME  
RUN echo "%$USERNAME ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers  
  
RUN echo "ServerName $APACHE_SERVERNAME" >> /etc/apache2/apache2.conf  
RUN echo 'sudo service apache2 start' >> /etc/bash.bashrc \  
&& /etc/init.d/apache2 start  
COPY "config/apache/sites-available/$APACHE_SERVERNAME" "/etc/apache2/sites-
available/"  
COPY config/apache/apache2-foreground /usr/local/bin/  
RUN a2enmod rewrite \  
&& a2dissite 000-default \  
&& a2ensite "$APACHE_SERVERNAME" \  
&& /etc/init.d/apache2 stop  
  
RUN mkdir -p "/var/www/$APACHE_SERVERNAME/modules" \  
&& mkdir -p "/var/www/$APACHE_SERVERNAME/themes" \  
&& mkdir -p "/var/www/$APACHE_SERVERNAME/files" \  
&& mkdir -p "/usr/share/drupal6/sites/$APACHE_SERVERNAME" \  
&& cd "/etc/drupal/6/sites/$APACHE_SERVERNAME" \  
&& ln -s "/var/www/$APACHE_SERVERNAME/modules" "modules" \  
&& ln -s "/var/www/$APACHE_SERVERNAME/files" "files" \  
&& ln -s "/var/www/$APACHE_SERVERNAME/themes" "themes"  
  
COPY "config/drupal/*.php" "/etc/drupal/6/sites/$APACHE_SERVERNAME/"  
  
RUN chown :www-data -R "/var/www/$APACHE_SERVERNAME" \  
&& chown :www-data "/etc/drupal/6/sites/$APACHE_SERVERNAME/"*.php \  
&& chmod +r "/etc/drupal/6/sites/$APACHE_SERVERNAME/"*.php \  
&& chmod g+w -R "/var/www/$APACHE_SERVERNAME"  
  
EXPOSE 80  
USER "$USERNAME"  
WORKDIR "/var/www/$APACHE_SERVERNAME"  
  
CMD ["apache2-foreground"]  

