FROM ubuntu:utopic  
MAINTAINER Oleg Kossoy <oleg@kossoy.com>  
  
# Install packages  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update && \  
apt-get -y install supervisor git apache2 libapache2-mod-php5 mysql-server
php5-mysql pwgen php-apc php5-mcrypt mc openssh-server samba curl  
  
# Install node  
RUN curl -sL https://deb.nodesource.com/setup | sudo bash -  
RUN apt-get install nodejs -y  
RUN npm install -g grunt-cli bower  
  
# Install express  
RUN npm install -g express-generator  
  
# Install ssh  
RUN mkdir -p /var/run/sshd && sed -i
"s/UsePrivilegeSeparation.*/UsePrivilegeSeparation no/g" /etc/ssh/sshd_config
&& sed -i "s/UsePAM.*/UsePAM no/g" /etc/ssh/sshd_config && sed -i
"s/PermitRootLogin.*/PermitRootLogin yes/g" /etc/ssh/sshd_config  
ADD set_root_pw.sh /set_root_pw.sh  
  
# Add image configuration and scripts  
ADD start-apache2.sh /start-apache2.sh  
ADD start-mysqld.sh /start-mysqld.sh  
ADD run.sh /run.sh  
RUN chmod 755 /*.sh  
ADD my.cnf /etc/mysql/conf.d/my.cnf  
ADD supervisord-apache2.conf /etc/supervisor/conf.d/supervisord-apache2.conf  
ADD supervisord-mysqld.conf /etc/supervisor/conf.d/supervisord-mysqld.conf  
  
# Remove pre-installed database  
RUN rm -rf /var/lib/mysql/*  
  
# Add MySQL utils  
ADD create_mysql_admin_user.sh /create_mysql_admin_user.sh  
RUN chmod 755 /*.sh  
  
# config to enable .htaccess  
ADD apache_default /etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite  
  
# Configure /apps folder  
RUN mkdir -p /apps && rm -fr /var/www/html && ln -s /apps /var/www/html  
  
# Install samba  
ADD smb.cfg /etc/samba/smb.conf  
  
#Enviornment variables to configure php  
ENV PHP_UPLOAD_MAX_FILESIZE 10M  
ENV PHP_POST_MAX_SIZE 10M  
  
# Add volumes for MySQL  
VOLUME ["/apps"]  
  
EXPOSE 80 3306 22 445 9000 3000 8080  
CMD ["/run.sh"]  
  
# docker build -t <image_name> .  
# docker run -d -p 80:80 -p 9000:9000 -p 8080:8080 -p 2222:22 -p 445:445 -p
3000:3000 --name <container> <image_name>  

