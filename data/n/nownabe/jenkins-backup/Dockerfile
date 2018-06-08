FROM centos:6.6  
MAINTAINER nownabe <nownabe@idcf.jp>  
  
VOLUME ["/jenkins_backup/jenkins_home", "/jenkins_backup/backups"]  
  
# Update  
RUN yum -y -q update && yum clean all  
  
# Install packages  
RUN yum -y -q install tar && yum clean all  
  
# Install Ruby  
RUN yum -y -q install ruby && yum clean all  
  
# Install s3sync  
RUN curl -s http://s3.amazonaws.com/ServEdge_pub/s3sync/s3sync.tar.gz | tar zx
-C /opt  
RUN mkdir /etc/s3conf  
  
# Install jenkins-backup-script  
RUN curl -s -o /usr/local/bin/jenkins-backup
https://raw.githubusercontent.com/sue445/jenkins-backup-script/master/jenkins-
backup.sh && \  
chmod +x /usr/local/bin/jenkins-backup  
  
# Add backup script  
ADD backup.sh /usr/local/bin/backup  
RUN chmod +x /usr/local/bin/backup  
  
CMD ["/usr/local/bin/backup"]  

