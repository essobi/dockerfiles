FROM centos:centos6  
  
RUN yum -y update  
RUN yum -y upgrade  
  
RUN yum -y install epel-release  
RUN rpm -U http://dl.iuscommunity.org/pub/ius/stable/CentOS/6/x86_64/ius-
release-1.0-13.ius.centos6.noarch.rpm  
RUN yum -y install mysql55-server  
  
VOLUME /mysql  
  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
COPY first-time.sql /first-time.sql  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 3306  
CMD ["/usr/bin/mysqld_safe", "--datadir=/mysql", "--user=mysql"]  

