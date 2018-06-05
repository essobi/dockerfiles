FROM centos:centos6  
MAINTAINER Alex Levin  
  
RUN yum -y install http://download.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
RUN yum -y upgrade  
RUN yum -y install monit  
  
#RUN mv /etc/monit /etc/monit.orig  
ADD etc_monit /etc/monit  
RUN chown -R root:root /etc/monit/monitrc  
RUN chmod 600 /etc/monit/monitrc  
RUN mkdir -p /var/lib/monit  
  
CMD ["/usr/bin/monit", "-I", "-c/etc/monit/monitrc"]  
  

