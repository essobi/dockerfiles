FROM debian:jessie  
MAINTAINER Grzegorz Bizon <grzegorz.bizon@ntsn.pl>  
  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update # upd 2015022401  
  
# MySQL Server  
RUN echo 'mysql-server mysql-server/root_password password mysql_pass' |
debconf-set-selections  
RUN echo 'mysql-server mysql-server/root_password_again password mysql_pass' |
debconf-set-selections  
RUN apt-get -y install mysql-server --no-install-recommends  
RUN sed -ie "s/^bind-address\s*=\s*127\\.0\\.0\\.1$/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
  
# PHPMyAdmin  
RUN echo 'phpmyadmin phpmyadmin/dbconfig-install boolean true' | debconf-set-
selections  
RUN echo 'phpmyadmin phpmyadmin/app-password-confirm password
phpmyadmin_password ' | debconf-set-selections  
RUN echo 'phpmyadmin phpmyadmin/mysql/admin-pass password mysql_pass' |
debconf-set-selections  
RUN echo 'phpmyadmin phpmyadmin/mysql/app-pass password mysql_pass' | debconf-
set-selections  
RUN echo 'phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2' |
debconf-set-selections  
RUN /etc/init.d/mysql start; apt-get -y install phpmyadmin --no-install-
recommends  
  
RUN apt-get clean  
VOLUME [ "/var/log/mysql/", "/var/log/apache2/" ]  
  
EXPOSE 3306  
EXPOSE 80  
CMD service apache2 start; mysqld_safe  

