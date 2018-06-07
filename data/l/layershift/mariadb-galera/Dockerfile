FROM bbania/centos:base  
MAINTAINER "Layershift" <jelastic@layershift.com>  
  
COPY ./configs/MariaDB.repo /etc/yum.repos.d/  
  
RUN yum install -q -y rsync bind-utils socat xinetd  
RUN rpm --import https://yum.mariadb.org/RPM-GPG-KEY-MariaDB  
RUN yum -q -y install http://www.percona.com/downloads/percona-
release/redhat/0.1-3/percona-release-0.1-3.noarch.rpm  
RUN yum -q --enablerepo=mariadb -y install MariaDB-Galera-server MariaDB-
client galera percona-xtrabackup.x86_64  
RUN yum -q clean all  
  
RUN echo "mysqlchk 9200/tcp" >> /etc/services  
  
RUN /sbin/chkconfig mysql on && \  
systemctl enable xinetd  
  
RUN touch /var/log/mysql.log && \  
chown mysql: /var/log/mysql.log  
  
RUN mkdir -p /root/scripts  
  
COPY ./configs/server.cnf /etc/my.cnf.d/server.cnf  
COPY ./configs/iptables /etc/sysconfig/iptables  
COPY ./configs/user.sql /tmp/  
COPY ./configs/mysqlchk /etc/xinetd.d/  
COPY ./configs/clustercheck /root/scripts/  
  
RUN chmod +x /root/scripts/clustercheck  
  
VOLUME /var/lib/mysql /etc/my.cnf.d/ /root/scripts /etc/xinetd.d  
  
EXPOSE 3306 4567 4444  

