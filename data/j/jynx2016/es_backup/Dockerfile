FROM centos:centos7  
MAINTAINER jl  
  
# Upgrade...  
RUN yum upgrade -y  
# add EPEL repo  
RUN rpm -iUvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm  
RUN yum -y update  
  
#install AWS CLI  
RUN yum -y update && \  
yum -y install python-pip && \  
pip install elasticsearch && \  
pip install elasticsearch-curator  
  
#install cronie  
RUN yum -y install cronie  
  
#add scripts and cronjob  
RUN mkdir /backup  
RUN mkdir /backup/keys  
ADD scripts/start-backup.sh /backup/start-backup.sh  
ADD scripts/esbackup.sh /backup/esbackup.sh  
ADD scripts/cronjob.conf /backup/cronjob.conf  
  
RUN chmod 755 /backup/start-backup.sh  
RUN chmod 755 /backup/esbackup.sh  
  
# register the bash as CMD  
#ENTRYPOINT ["/backup/start-backup.sh"]  
CMD ["/backup/start-backup.sh"]

