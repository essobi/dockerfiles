FROM centos  
  
RUN curl http://download.opensuse.org/repositories/home:/holland-
backup/CentOS_7/home:holland-backup.repo > /etc/yum.repos.d/home:holland-
backup.repo  
  
RUN yum -y update && yum install -y holland holland-mysqldump mariadb  
  
ADD ./entrypoint.sh /entrypoint.sh  
  
RUN cp -r /etc/holland /etc/holland.orig  
  
VOLUME /etc/holland  
  
VOLUME /var/spool/holland  
  
ENTRYPOINT ["/entrypoint.sh"]

