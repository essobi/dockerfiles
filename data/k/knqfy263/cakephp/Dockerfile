FROM centos:6  
RUN yum -y update  
RUN yum -y install git  
  
# Install PHP  
RUN yum install -y epel-release  
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-6.rpm  
RUN yum -y install --enablerepo=remi --enablerepo=remi-php56 php php-intl php-
mbstring php-mysqlnd  
  
# Install Apache  
RUN yum install -y httpd httpd-devel  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/bin/composer  
  
# Install CakePHP  
RUN cd /var/www/html/ && \  
composer create-project -n --prefer-dist cakephp/app ./  
  
ADD ./contents/php.ini /etc/php.ini  
ADD ./contents/httpd.conf /etc/httpd/conf/httpd.conf  
ADD ./contents/HelloController.php
/var/www/html/src/Controller/HelloController.php  
ADD ./contents/Hello /var/www/html/src/Template/Hello  
  
EXPOSE 80 443  
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]  

