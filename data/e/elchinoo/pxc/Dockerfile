FROM centos:centos7  
  
RUN \  
#  
# Install Epel and Percona repos  
yum -y install epel-release \  
&& rpm -Uhv http://www.percona.com/downloads/percona-
release/redhat/0.1-4/percona-release-0.1-4.noarch.rpm \  
&& curl -o /etc/pki/rpm-gpg/RPM-GPG-KEY-percona
https://www.percona.com/downloads/RPM-GPG-KEY-percona \  
&& rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-percona \  
  
# Install PXC and netcat  
&& yum -y install Percona-XtraDB-Cluster-57 nc \  
  
# Clean process  
&& yum clean all  
  
# Configuration file  
COPY my.cnf /etc/my.cnf  
  
# Database init script  
COPY mysql_start.sh /sbin/mysql_start  
RUN chmod 755 /sbin/mysql_start  
  
CMD ["mysql_start"]  

