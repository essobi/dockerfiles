FROM ubuntu  
  
MAINTAINER m.adnan80@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
# Repository update and install Apache, OpenSSH Server and Supervisor  
RUN apt-get update --fix-missing && apt-get -y install openssh-server apache2
supervisor --no-install-recommends  
  
# MySQL Server install and configure  
RUN echo 'mysql-server mysql-server/root_password password mysqladmin' |
debconf-set-selections; \  
echo 'mysql-server mysql-server/root_password_again password mysqladmin' |
debconf-set-selections;  
RUN apt-get -y install mysql-server --no-install-recommends; \  
sed -ie "s/^bind-address\s*=\s*127\\.0\\.0\\.1$/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf;  
  
# Setup ssh-server root access and password.  
RUN cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bkup; \  
chmod a-w /etc/ssh/sshd_config.bkup; \  
sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/'
/etc/ssh/sshd_config; \  
echo 'root:passwdroot' | chpasswd  
  
# PHPMyAdmin installation and configuration  
RUN echo 'phpmyadmin phpmyadmin/dbconfig-install boolean true' | debconf-set-
selections; \  
echo 'phpmyadmin phpmyadmin/app-password-confirm password mysqladmin ' |
debconf-set-selections; \  
echo 'phpmyadmin phpmyadmin/mysql/admin-pass password mysqladmin' | debconf-
set-selections; \  
echo 'phpmyadmin phpmyadmin/mysql/app-pass password mysqladmin' | debconf-set-
selections; \  
echo 'phpmyadmin phpmyadmin/reconfigure-webserver multiselect apache2' |
debconf-set-selections  
RUN /etc/init.d/mysql start; apt-get -y install phpmyadmin --no-install-
recommends  
  
# Set apache hostname  
RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf  
RUN mkdir -p /var/run/sshd /var/run/apache2 /var/lock/apache2
/var/log/supervisor  
  
# Copy supersvisord.conf file from local directory to required location on
docker images  
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# Copy script to the root directory and make it executable  
COPY run.sh /run.sh  
RUN chmod +x /run.sh  
  
RUN mkdir -p /data && cp -rp /var/lib/mysql/* /data && rm -rf /var/lib/mysql  
  
# Create persistent volumes for Apache data direcotry and MySql data directory  
VOLUME ["/var/www/html/","/var/lib/mysql/"]  
  
# Clean up all packages and remove all temporary files  
RUN apt-get clean && apt-get autoremove -y && rm -rf /var/lib/apt/lists/*
/tmp/* /var/tmp/*  
  
# Expose SSH, Apache and MySql ports  
EXPOSE 22 80 3306  
# Run script to setup mysql and run supervisord daemon to start SSH, Apache
and MySql on container run.  
CMD ["/run.sh"]  

