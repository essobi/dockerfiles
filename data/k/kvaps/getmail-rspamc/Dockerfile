FROM centos:centos6  
MAINTAINER kvaps <kvapss@gmail.com>  
ENV REFRESHED_AT 2016-05-12  
RUN yum -y install epel-release  
RUN curl -o /etc/yum.repos.d/rspamd.repo http://rspamd.com/rpm-
stable/centos-6/rspamd.repo  
RUN rpm --import http://rspamd.com/rpm-stable/gpg.key  
RUN yum -y install rspamd ripmime getmail file  
  
ENTRYPOINT ["/bin/start.sh"]  
VOLUME ["/var/spool/mail", "/tmp/attachments"]  
  
ADD start.sh /bin/start.sh  

