FROM centos:7  
RUN yum install -y https://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm && \  
yum install -y supervisor prosody && \  
yum clean all  
  
ADD supervisord.conf /etc/  
  
VOLUME ["/etc/prosody", "/var/lib/prosody", "/var/log/prosody"]  
  
EXPOSE 5222 5269  
CMD ["/usr/bin/supervisord"]  
  

