FROM centos:6  
ENV version 2.9.3  
RUN yum -y update  
RUN yum -y install wget php httpd vim unzip  
  
RUN wget https://codeload.github.com/cakephp/cakephp/zip/${version}  
RUN unzip $version  
RUN cp -r cakephp-${version} /var/www/cakephp  
RUN chown -R apache:apache /var/www/cakephp  
  
ADD ./contents/php.ini /etc/php.ini  
ADD ./contents/core.php /var/www/cakephp/app/Config/core.php  
ADD ./contents/httpd.conf /etc/httpd/conf/httpd.conf  
ADD ./contents/HelloController.php
/var/www/cakephp/app/Controller/HelloController.php  
ADD ./contents/Hello /var/www/cakephp/app/View/Hello  
  
EXPOSE 80 443  
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]  

