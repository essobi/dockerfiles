FROM jonhartley/c7-systemd  
  
COPY configcreate.service /etc/systemd/system/configcreate.service  
COPY configcreate.sh /configcreate.sh  
  
RUN yum -y upgrade; \  
yum -y install epel-release; \  
yum -y install http://www.percona.com/downloads/percona-
release/redhat/0.1-4/percona-release-0.1-4.noarch.rpm; \  
yum -y install
https://dl.influxdata.com/telegraf/releases/telegraf-1.5.2-1.x86_64.rpm; \  
yum -y install Percona-XtraDB-Cluster-shared-57 Percona-XtraDB-Cluster-57
Percona-XtraDB-Cluster-client-57 Percona-XtraDB-Cluster-server-57 percona-
toolkit percona-xtrabackup-24 pigz openssl; \  
rm -rf /var/lib/mysql/*; \  
yum clean all; \  
systemctl daemon-reload; \  
systemctl enable configcreate.service  
  
EXPOSE 3306 4444 4567 4568 9104  
ENTRYPOINT ["/usr/sbin/init"]  
  
  
  
  

