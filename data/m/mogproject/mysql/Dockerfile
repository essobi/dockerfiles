FROM centos:6.4  
#  
# SSH  
#  
RUN yum install -y --nogpgcheck openssh-server sudo  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key && ssh-keygen -t dsa -f
/etc/ssh/ssh_host_dsa_key && sed -i 's/UsePAM.*/UsePAM no/g'
/etc/ssh/sshd_config  
  
# create user  
RUN useradd ssh-user && echo 'ssh-user:ssh-user' | chpasswd && echo 'ssh-user
ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
#  
# Supervisor  
#  
# enable EPEL repository  
RUN yum install -y --nogpgcheck
http://dl.iuscommunity.org/pub/ius/stable/Redhat/6/x86_64/epel-
release-6-5.noarch.rpm  
  
# install supervisord  
RUN yum install -y --nogpgcheck supervisor  
  
# settings  
ADD supervisord.conf /etc/supervisord.conf  
RUN mkdir -p /var/log/supervisor  
  
#  
# MySQL  
#  
# enable MySQL official repository  
RUN yum localinstall -y http://repo.mysql.com/mysql-community-release-el6.rpm  
RUN yum install -y --nogpgcheck mysql-server mysql-community-libs-compat  
  
# example for additional settings  
#ADD my.cnf /etc/my.cnf  
#ADD my-optional.cnf /etc/mysql/conf.d/my-optional.cnf  
# allow remote access  
RUN mysql_install_db && chown -R mysql:mysql /var/lib/mysql &&
(/usr/bin/mysqld_safe &) && sleep 5 && mysql -uroot -e "GRANT ALL PRIVILEGES
ON *.* TO root@'%' WITH GRANT OPTION;" && mysqladmin -uroot shutdown  
  
EXPOSE 22 3306  
CMD ["/usr/bin/supervisord"]  
  

