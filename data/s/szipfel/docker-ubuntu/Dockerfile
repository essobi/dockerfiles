FROM ubuntu:16.04  
MAINTAINER Steve Zipfel <steve@webrepublic.ca>  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Install packages.  
RUN apt-get update  
RUN apt-get install -y vim git apache2 php7.0 curl wget php7.0-gd php7.0-dom
php7.0-curl php7.0-mbstring php7.0-bz2 libapache2-mod-php7.0 supervisor unzip
composer  
  
RUN export DEBIAN_FRONTEND="noninteractive"  
RUN debconf-set-selections <<< "mysql-server mysql-server/root_password
password rootpw"  
RUN debconf-set-selections <<< "mysql-server mysql-server/root_password_again
password rootpw"  
  
RUN apt-get install -y mysql-server php7.0-mysql  
  
RUN apt-get clean  
  
RUN apt-get update && apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
RUN echo 'root:webrepublic | chpasswd'  
  
ENV NOTVISIBLE "in users profile"  
RUN echo "export VISIBLE=now" >> /etc/profile  
  
#Apache 2  
RUN sed -i 's/AllowOverride None/AllowOverride All/' /etc/apache2/apache2.conf  
RUN a2enmod rewrite  
  
# Install Drush 8 (master) as phar.  
RUN wget http://files.drush.org/drush.phar  
RUN mv drush.phar /usr/local/bin/drush && chmod +x /usr/local/bin/drush  
  
# Setup Supervisor.  
RUN echo -e '[program:apache2]\ncommand=/bin/bash -c "source
/etc/apache2/envvars && exec /usr/sbin/apache2
-DFOREGROUND"\nautorestart=true\n\n' >> /etc/supervisor/supervisord.conf  
RUN echo -e '[program:mysql]\ncommand=/usr/bin/pidproxy
/var/run/mysqld/mysqld.pid /usr/sbin/mysqld\nautorestart=true\n\n' >>
/etc/supervisor/supervisord.conf  
RUN echo -e '[program:sshd]\ncommand=/usr/sbin/sshd -D\n\n' >>
/etc/supervisor/supervisord.conf  
  
RUN /etc/init.d/mysql start  
  
RUN echo mysql -uroot -prootpw -e "create database drupal;"  
RUN echo mysql -uroot -prootpw -e "GRANT ALL PRIVILEGES ON drupal.* To
'drupal'@'localhost' IDENTIFIED BY 'drupal';"  
  
RUN echo git config --global user.email "info@webrepublic.com" && git config
--global user.name "Web Republic"  
RUN echo cd /var/www && \  
composer clear-cache && \  
export COMPOSER_PROCESS_TIMEOUT=2000 && \  
composer create-project --no-interaction acquia/blt-project blt  
RUN echo cd /var/www/blt  
RUN echo composer run-script blt-alias && echo source /root/.bashrc && echo
blt local:setup  
RUN echo ln -s /var/www/blt/docroot html  
#Start up Apache  
RUN /etc/init.d/apache2 start  
  
EXPOSE 80 3306 22  
CMD exec supervisord -n  

