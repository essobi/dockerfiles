FROM centos:7  
MAINTAINER ray.vafa@essentialneed.org  
  
# Install apache  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN rpm -Uvh https://mirror.webtatic.com/yum/el7/webtatic-release.rpm  
RUN yum update -y  
RUN yum install -y httpd php56w php56w-mysql php56w-gd  
  
# Copy app to apache root  
RUN echo "<?php phpinfo(); ?>" > /var/www/html/phpinfo.php  
COPY . /var/www/html  
  
# Install composer  
RUN cd /tmp  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Install app and dependencies into /src  
RUN cd /var/www/html; composer install  
  
# Set PHP timezone  
RUN echo -e "\ndate.timezone = 'Australia/Sydney';\n" >> /etc/php.ini  
  
# Set AllowOverride All  
RUN sed -i 's/AllowOverride none/AllowOverride All/g'
/etc/httpd/conf/httpd.conf  
RUN sed -i 's/AllowOverride None/AllowOverride All/g'
/etc/httpd/conf/httpd.conf  
  
# Setting default environment variables  
RUN touch /var/www/html/.env  
# for local docker use:  
# RUN cp /var/www/html/env.sample /var/www/html/.env  
EXPOSE 80  
CMD ["/usr/sbin/apachectl", "-D", "FOREGROUND"]  

