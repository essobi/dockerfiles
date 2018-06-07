FROM centos:centos7  
  
MAINTAINER Mikael Keto  
  
# add stackdriver repository  
RUN curl -o /etc/yum.repos.d/stackdriver.repo
https://repo.stackdriver.com/stackdriver-el7.repo  
  
# install stackdriver  
RUN yum -y install initscripts stackdriver-agent && yum clean all && rm -rf
/var/cache/yum  
  
RUN mkdir -p /var/lock/subsys; exit 0  
ADD run.sh /run.sh  
RUN chmod 755 /run.sh  
  
CMD ["/run.sh"]  

