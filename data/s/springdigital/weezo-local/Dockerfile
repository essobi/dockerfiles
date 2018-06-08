# Weezo  
#  
# VERSION 0.1  
# DOCKER-VERSION 17.03.0-ce  
from centos:6  
run rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-6.noarch.rpm  
run rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
run curl --silent --location https://rpm.nodesource.com/setup_6.x | bash -  
  
run yum update -y --enablerepo=remi  
# run yum install httpd -y --enablerepo=remi  
run yum install php70 php70-php php70-php-pdo php70-php-mysqlnd php70-php-
mcrypt php70-php-gd php70-php-bcmath php70-php-xml php70-php-zip php70-php-
mbstring php70-php-fpm git nodejs supervisor openssh-server -y
--enablerepo=remi  
  
run npm install -g @angular/cli -y  
  
run sed -i 's/AllowOverride None/AllowOverride All/'
/etc/httpd/conf/httpd.conf  
run sed -i 's/\/var\/www\/html/\/var\/www\/html\/web/'
/etc/httpd/conf/httpd.conf  
  
add . /var/www/html/  
add composer /usr/local/bin/composer  
run ln -s /usr/bin/php70 /usr/bin/php  
run chmod 775 /usr/local/bin/composer  
run rm /var/www/html/Dockerfile  
run cat /var/www/html/app/config/parameters.yml.docker >
/var/www/html/app/config/parameters.yml  
run echo "172.17.0.2 docker.weezo.com.au" >> /etc/hosts  
run chown -R apache.apache /var/www/  
run mkdir -p /var/www/html/app/cache  
run chmod -R 777 /var/www/html/app/cache  
run cd /var/www/html/ && composer install -q  
run cd /var/www/html/web/weezo; npm install -y;  
  
run sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd  
#copy supervisord.conf /etc/supervisord.conf  
run echo 'root:w3ezZ0o' | chpasswd  
  
# patch Server.js to enable Docker host  
run cat /var/www/html/Server.js >
/var/www/html/web/weezo/node_modules/webpack-dev-server/lib/Server.js  
  
# add cron  
# run crontab -l | { cat; echo "0 0 0 0 0 touch
/var/www/html/web/weezo/src/app/app.module.ts"; } | crontab -  
# docker.weezo.com.au is a local NS pointer  
#entrypoint service sshd start && /bin/bash  
entrypoint service sshd start && cd /var/www/html/web/weezo && ng serve --host
docker.weezo.com.au --port 80 && /bin/bash

