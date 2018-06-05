FROM centos  
RUN yum -y update  
RUN yum install -y nano vim net-tools  
RUN yum install -y httpd  
RUN yum install -y php php-mysql libzip php-cli php-common php-pdo  
  
ADD run-httpd.sh /opt/run-httpd.sh  
RUN chmod +x /opt/run-httpd.sh  
  
ADD phpinfo.php /var/www/html/phpinfo.php  
  
EXPOSE 80  
CMD ["/opt/run-httpd.sh"]  

