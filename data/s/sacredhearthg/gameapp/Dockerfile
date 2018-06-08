#pull centos 7 base image  
FROM centos:7  
MAINTAINER SHU  
  
RUN rpm -Uvh http://cdn.mysql.com//Downloads/Connector-Python/mysql-connector-
python-2.1.6-1.el7.x86_64.rpm  
  
RUN yum -y --setopt=tsflags=nodocs update && \  
yum -y --setopt=tsflags=nodocs install httpd && \  
yum -y --setopt=tsflags=nodocs install php && \  
yum clean all  
  
EXPOSE 80  
# Simple startup script to avoid some issues observed with container  
ADD run-httpd.sh /run-httpd.sh  
ADD httpd.conf /etc/httpd/conf/httpd.conf  
RUN chmod -v +r /etc/httpd/conf/httpd.conf  
ADD game1.py /var/www/cgi-bin/game1.py  
RUN chmod -v +x /var/www/cgi-bin/game1.py  
ADD testProjClient.js /var/www/html/testProjClient.js  
ADD GamePage.php /var/www/html/GamePage.php  
RUN chmod -v +r /var/www/html/testProjClient.js  
RUN chmod -v +r /var/www/html/GamePage.php  
ADD ReLogin.htm /var/www/html/ReLogin.htm  
ADD login.php /var/www/html/login.php  
ADD gamedbconnect.cnf /etc/mysql/gamedbconnect.cnf  
RUN chmod -v +r /etc/mysql/gamedbconnect.cnf  
  
RUN chmod -v +x /run-httpd.sh  
  
CMD ["/run-httpd.sh"]  
  

