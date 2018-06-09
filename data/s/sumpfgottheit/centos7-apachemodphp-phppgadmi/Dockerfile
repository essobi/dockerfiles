FROM sumpfgottheit/centos7-apachemodphp  
  
RUN yum -y install phpPgAdmin  
RUN yum -y clean all  
RUN rm -f /etc/httpd/conf.d/welcome.conf  
COPY config.inc.php /etc/phpPgAdmin/config.inc.php  
COPY httpd.phppgadmin.conf /etc/httpd/conf.d/phpPgAdmin.conf  
  

