FROM centos:6.8  
MAINTAINER Vladimir Rančev <rancev@gmail.com>  
  
# install http  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum -y install httpd vim-enhanced bash-completion unzip  
  
# install mysql  
RUN yum install -y mysql mysql-server  
RUN echo "NETWORKING=yes" > /etc/sysconfig/network  
  
# start mysqld to create initial tables  
CMD service mysqld start  
  
# install php  
RUN yum install -y php php-mysql php-devel php-gd php-pecl-memcache php-pspell
php-snmp php-xmlrpc php-xml  
CMD service httpd restart  
  
# install sshd  
RUN yum install -y openssh-server openssh-clients passwd  
RUN ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && ssh-keygen -q
-N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN sed -ri 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config && echo
'root:12321' | chpasswd  
  
# Install app  
COPY . /var/www/  
  
# Create DB  
CMD mysql -e "create database radimsa1_00"  
CMD mysql -e "GRANT ALL PRIVILEGES ON radimsa1_00.* TO 'radimsa1_00'@'%'
IDENTIFIED BY '6R)u(.lnkw^i'"  
CMD mysql radimsa1_00 < /var/www/radimsa1_00  
  
EXPOSE 22 80  

