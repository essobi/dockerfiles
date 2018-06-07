FROM centos:6  
MAINTAINER george.niculae79@gmail.com  
  
COPY supervisord.conf /etc/supervisord.conf  
  
RUN useradd -r -g daemon freeswitch && \  
mkdir -p /srv /var/log/freeswitch && \  
chown freeswitch:daemon /var/log/freeswitch -R  
  
RUN curl -o /etc/yum.repos.d/2600hz.repo http://repo.2600hz.com/2600hz.repo &&
\  
yum install -y epel-release && \  
yum clean all && \  
yum install -y kazoo-freeswitch-R15B haproxy && \  
yum install -y curl supervisor && \  
chkconfig supervisord on  
  
VOLUME ["/srv"]  
  
CMD ["/usr/bin/supervisord"]  

