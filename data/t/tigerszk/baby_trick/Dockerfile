FROM centos:centos7  
MAINTAINER tigerszk  
  
#1. Update  
RUN yum -y update && yum clean all  
  
#2. Apahce&php install  
RUN yum -y install httpd php  
RUN > /etc/httpd/conf.d/welcome.conf  
  
#3. set contents  
WORKDIR /var/www/html  
COPY index.php index.php  
COPY config.php config.php  
COPY serialize.php serialize.php  
RUN chown apache:apache *  
RUN chmod 755 *.php  
  
#4. MySQL install  
RUN yum -y install mariadb-server php-mysql  
RUN mysql_install_db --user=mysql --ldata=/var/lib/mysql/  
COPY mysql_secure_installation.sql /opt/mysql_secure_installation.sql  
COPY user.sql /opt/user.sql  
COPY init.sql /opt/init.sql  
COPY startup.sh /opt/startup.sh  
RUN chmod 700 /opt/*.sql  
RUN chmod 700 /opt/startup.sh  
ENTRYPOINT /opt/startup.sh && /bin/bash --login  
  
EXPOSE 80  

