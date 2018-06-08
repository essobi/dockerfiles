FROM centos:6  
EXPOSE 80  
RUN yum clean all  
RUN yum -y install apache php php-pdo sqlite  
RUN mkdir /var/www/phpBB-database; mkdir /var/www/html/phpBB3; chown -R
apache:apache /var/www/phpBB-database  
COPY ./phpBB3 /var/www/html/phpBB3  
COPY ./phpBB.db /var/www/phpBB-database  
RUN chown -R apache:apache /var/www/html/; chown -R apache:apache
/var/www/phpBB-database  
ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]  

