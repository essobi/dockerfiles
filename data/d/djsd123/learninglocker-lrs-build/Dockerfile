# Learning Locker (http://learninglocker.net/) LRS container  
# Based on centos7 base image running httpd, php, and mongoDB  
# Instructions adapted from CentOS7.0 instructions provided by David Pesce
(https://github.com/davidpesce) posted to
http://docs.learninglocker.net/installation/  
# Version 1  
# Pull and use the centos7 image as the base  
FROM centos:centos7  
USER root  
  
# Persistent volume for mongodb  
VOLUME /data/db  
  
MAINTAINER Maintainer_Name  
  
# Update image  
RUN yum update -y  
  
# Install Remi Collet Repository  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm && rpm -Uvh
http://rpms.famillecollet.com/enterprise/remi-release-7.rpm  
  
# Install apache, php, mongoDB  
RUN yum -y --enablerepo=remi,remi-php56 install httpd php php-pdo php-common
php-cli php-pear php-mysqlnd php-pecl-mongo php-gd php-mbstring* php-mcrypt
php-xml mongodb mongodb-server nodejs npm git deltarpm mod_ssl  
  
# Install Bower  
RUN npm install -g bower  
  
# Install Composer and set global launch  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
# need to create directories per /usr/lib/tmpfiles.d/httpd.conf  
RUN rm -rf /run/httpd/*; mkdir -p /run/httpd/htcacheclean; chmod 710
/run/httpd; chmod 700 /run/httpd/htcacheclean; chown root:apache /run/httpd;
chown apache:apache /run/httpd/htcacheclean  
  
# clone learninglocker via git  
RUN git clone https://github.com/LearningLocker/learninglocker.git
learninglocker  
  
# install learninglocker  
RUN cd /learninglocker; composer install  
  
# modify database credentials  
RUN sed -i "s/^.*username.*/\t\t\'username\' => \'username\',/g"
/learninglocker/app/config/database.php; sed -i
"s/^.*username.*/\t\t\'password\' => \'password\',/g"
/learninglocker/app/config/database.php  
  
# Start mongodb and create a mongo user with rw perms then finalize learning
locker mongodb setup  
RUN exec /usr/bin/mongod & sleep 10; mongo learninglocker --eval
'printjson(db.createUser({user:"username",pwd:"password",roles:["readWrite"]}))';
cd /learninglocker; php artisan migrate  
  
# modify httpd configuration  
RUN echo '<Directory "/var/www/learninglocker/public">' >>
/etc/httpd/conf/httpd.conf; echo ' AllowOverride All' >>
/etc/httpd/conf/httpd.conf; echo '</Directory>' >> /etc/httpd/conf/httpd.conf  
RUN sed -i "s/^DocumentRoot.*/DocumentRoot
\'\/var\/www\/learninglocker\/public\/\'/g" /etc/httpd/conf/httpd.conf  
RUN chown -R apache:apache /learninglocker; ln -s /learninglocker/ /var/www/  
  
# modify encryption key .. this is required b/c the default one is only 14
characters  
RUN sed -i "s/'key.*/\'key\' => \'CHANGEME12345678\',/"
/learninglocker/app/config/app.php  
  
#SSL Setup  
ADD ca.crt /etc/pki/tls/certs/  
ADD ca.key /etc/pki/tls/private/  
ADD ca.csr /etc/pki/tls/private/  
  
RUN sed -i "s/^SSLCertificateFile.*/SSLCertificateFile
\/etc\/pki\/tls\/certs\/ca.crt/g" /etc/httpd/conf.d/ssl.conf  
RUN sed -i "s/^SSLCertificateKeyFile.*/SSLCertificateKeyFile
\/etc\/pki\/tls\/private\/ca.key/g" /etc/httpd/conf.d/ssl.conf  
  
# create our container startup script  
ADD llstartup /usr/bin/llstartup  
RUN chmod 755 /usr/bin/llstartup  
  
EXPOSE 443  
# define entrypoint so ll will start from docker run  
ENTRYPOINT ["/usr/bin/llstartup"]  

