FROM debian:wheezy  
  
MAINTAINER Bai Xiaoyong "lostitle@gmail.com"  
# make sure the package repository is up to date  
RUN apt-get update  
  
# Install OpenSSH  
RUN apt-get install -y openssh-server ca-certificates supervisor sudo ruby git  
RUN mkdir -p /var/run/sshd  
RUN mkdir -p /var/log/supervisor  
  
RUN echo 'root:root' |chpasswd  
  
# Set Password of MySQL root  
ENV MYSQL_PASSWORD letmein  
# Install MySQL Server in a Non-Interactive mode. Default root password will
be $MYSQL_PASSWORD  
RUN echo "mysql-server mysql-server/root_password password $MYSQL_PASSWORD" |
debconf-set-selections  
RUN echo "mysql-server mysql-server/root_password_again password
$MYSQL_PASSWORD" | debconf-set-selections  
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install mysql-server  
#RUN apt-get autoclean  
# Add MySQL configuration  
#ADD my.cnf /etc/mysql/conf.d/my.cnf  
#ADD mysqld_charset.cnf /etc/mysql/conf.d/mysqld_charset.cnf  
RUN sed -i -e"s/^bind-address\s*=\s*127.0.0.1/bind-address = 0.0.0.0/"
/etc/mysql/my.cnf  
RUN /usr/sbin/mysqld & sleep 10s && echo "GRANT ALL ON *.* TO root@'%'
IDENTIFIED BY 'letmein' WITH GRANT OPTION; FLUSH PRIVILEGES" | mysql -uroot
-pletmein  
  
# Add VOLUMEs to allow backup of config and databases  
#VOLUME ["/etc/mysql", "/var/lib/mysql"]  
RUN git clone https://github.com/quickbundle/cryptdb /opt/cryptdb  
WORKDIR /opt/cryptdb  
RUN ruby scripts/install.rb .  
  
RUN echo "EDBDIR=/opt/cryptdb" >> /etc/environment  
ADD cryptdb.sh /opt/cryptdb.sh  
RUN chmod 755 /opt/cryptdb.sh; ln -s /opt/cryptdb.sh /usr/bin/cryptdb.sh  
  
RUN echo "\  
[supervisord]\n\  
nodaemon=true\n\  
\n\  
[program:sshd]\n\  
command=/usr/sbin/sshd -D\n\  
\n\  
[program:mysql]\n\  
command=service mysql start\n\  
\n\  
[program:cryptdb]\n\  
command=/opt/cryptdb.sh start\n\  
environment=EDBDIR=\"/opt/cryptdb\"\n\  
\n\  
" > /etc/supervisor/conf.d/supervisord.conf  
  
CMD ["/usr/bin/supervisord"]  
  
EXPOSE 22 3306 3307  

