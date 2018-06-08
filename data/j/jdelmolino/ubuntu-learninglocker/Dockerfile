# Learning Locker  
FROM ubuntu:14.04  
MAINTAINER Javier del Molino Matamala  
  
ARG DEBIAN_FRONTEND=noninteractive  
RUN apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927  
RUN echo "deb http://repo.mongodb.org/apt/ubuntu precise/mongodb-org/3.2
multiverse" | tee /etc/apt/sources.list.d/mongodb-org-3.2.list  
RUN echo "#!/bin/sh\nexit 0" > /usr/sbin/policy-rc.d  
RUN apt-get update && apt-get -y install apache2 libapache2-mod-php5 git
mongodb-org openssh-server php5 php5-curl php5-dev php5-mcrypt php-pear
supervisor  
RUN pecl install mongo  
RUN sed -i '/; If you wish/iextension=mongo.so\n' /etc/php5/cli/php.ini && sed
-i '/; If you wish/iextension=mongo.so\n' /etc/php5/apache2/php.ini  
RUN php5enmod mcrypt  
  
RUN cd /var/www/ && git clone -b master
https://github.com/LearningLocker/learninglocker.git learninglocker  
RUN cd /var/www/learninglocker/ && php -r
"readfile('https://getcomposer.org/installer');" | php  
RUN cd /var/www/learninglocker/ && php composer.phar install --no-interaction
--no-dev  
COPY database.php /var/www/learninglocker/app/config/local/database.php  
RUN mkdir -p /data/db/  
RUN mongod --fork --logpath /var/log/mongodb.log && mongo learninglocker
--eval "db.createUser({user: 'learnlockuser', pwd: 'learnlockpwd', roles:
['readWrite']});" && cd /var/www/learninglocker/ && php artisan migrate  
RUN gpasswd -a www-data `id -g -n $USER`  
RUN find /var/www/learninglocker/app/storage/ -type d -exec chmod 775 {} + &&
find /var/www/learninglocker/app/storage/ -type f -exec chmod 664 {} +  
RUN find /var/www/learninglocker/uploads/ -type d -exec chmod 775 {} + && find
/var/www/learninglocker/uploads/ -type f -exec chmod 664 {} +  
RUN cd /var/www/learninglocker/ && chown -R www-data:www-data *  
RUN sed -i 's/DocumentRoot \/var\/www\/html/DocumentRoot
\/var\/www\/learninglocker\/public\/\n\t<Directory
\/var\/www\/learninglocker\/>\n\t\tAllowoverride All\n\t<\/Directory>/'
/etc/apache2/sites-available/000-default.conf  
RUN a2enmod rewrite negotiation php5  
  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
EXPOSE 22 80  
CMD ["/usr/bin/supervisord"]  

