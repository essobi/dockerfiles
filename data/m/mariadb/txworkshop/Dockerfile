FROM centos:7  
RUN yum -y update  
RUN yum -y install wget mysql sudo which epel-release python-pip gcc python-
devel mysql-devel  
RUN yum -y install python-pip  
RUN pip install --upgrade pip  
RUN pip install MySQL-python  
  
## Get and install Maxscale  
RUN wget
https://downloads.mariadb.com/MaxScale/2.2.9/rhel/7/x86_64/maxscale-2.2.9-1.rhel.7.x86_64.rpm  
RUN yum -y install maxscale-2.*.rpm  
RUN rm /maxscale-2.*.rpm  
COPY scripts/maxscale.cnf /etc/maxscale.cnf  
  
WORKDIR /root  
COPY mariadb10_2.repo /etc/yum.repos.d/  
RUN yum -y install MariaDB-server  
  
RUN mkdir -p /usr/local/mysql/{1,2,3,4}/data  
  
RUN mkdir -p /var/lib/mysql/{1,2,3,4}  
  
RUN touch /var/log/mysqld{1,2,3,4}.log  
RUN chmod o-r /var/log/mysqld{1,2,3,4}.log  
COPY scripts/masking_rules.json /etc/  
COPY scripts/my.cnf /etc/  
COPY scripts/* /root/scripts/  
  
RUN mkdir -p /root/scripts  
  
RUN chmod +x /root/scripts/init.sh  
RUN chmod +x /root/scripts/docker-entrypoint.sh  
RUN chmod +x /root/scripts/startup.sh  
  
RUN mkdir -p /var/run/mysqld/  
  
RUN /root/scripts/init.sh  
RUN cat scripts/mariadb_sig.txt >> /etc/MOTD  
RUN echo "cat /etc/MOTD" >> ~/.bashrc  
RUN echo "export MYSQL_HOST=127.0.0.1" >> ~/.bashrc  
RUN echo "export MYSQL_PWDP=password" >> ~/.bashrc  
  
#STOPSIGNAL SIGKILL  
ENTRYPOINT ["scripts/docker-entrypoint.sh"]  

