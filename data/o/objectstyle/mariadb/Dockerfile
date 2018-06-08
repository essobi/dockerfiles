FROM centos:latest  
  
MAINTAINER Andrus Adamchik <andrus at objectstyle dot com>  
  
LABEL name=objectstyle-mariadb  
  
RUN yum -y install mariadb-server  
RUN yum -y update; yum clean all  
  
COPY setupdb.sql /root/setupdb.sql  
COPY startup.sh /root/startup.sh  
COPY dockerenv.sh /etc/profile.d/dockerenv.sh  
  
VOLUME /var/oc/mysql  
  
CMD [ "/root/startup.sh" ]  

