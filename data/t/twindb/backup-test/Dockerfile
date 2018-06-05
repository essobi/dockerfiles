FROM debian:jessie  
LABEL maintainer="TwinDB Development Team <dev@twindb.com>"  
EXPOSE 22  
EXPOSE 3306  
# Install packages  
RUN \  
apt-get update; \  
apt-get -y install curl lsb-release wget nmap sudo \  
openssh-client openssh-server  
  
# Install Oracle Repo  
RUN mysql_repo=mysql-apt-config_0.8.9-1_all.deb ; \  
curl --location https://dev.mysql.com/get/${mysql_repo} > /tmp/${mysql_repo} ;
\  
DEBIAN_FRONTEND=noninteractive dpkg -i /tmp/${mysql_repo} ; \  
apt-get update  
  
# Install/start sshd  
RUN \  
mkdir /var/run/sshd ; \  
mkdir -p /root/.ssh/ ; \  
/bin/chown root:root /root/.ssh ; \  
/bin/chmod 700 /root/.ssh/ ; \  
/usr/sbin/sshd  
  
COPY id_rsa.pub /root/.ssh/authorized_keys  
RUN \  
/bin/chmod 600 /root/.ssh/authorized_keys ; \  
/bin/chown root:root /root/.ssh/authorized_keys  
  
# Install/start MySQL  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y install mysql-community-server mysql-community-client  
  
COPY my-master-legacy.cnf /etc/mysql/mysql.conf.d/mysqld.cnf  
  
COPY docker-entrypoint.sh /usr/local/bin/  
RUN /bin/chmod 755 /usr/local/bin/docker-entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]  
  
CMD ["mysqld", "--user=root"]  

