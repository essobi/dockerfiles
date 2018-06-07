FROM centos:6  
MAINTAINER george.niculae79@gmail.com  
  
COPY supervisord.conf /etc/supervisord.conf  
  
RUN useradd -r -g daemon -d /opt/kazoo kazoo && \  
groupadd -r kamailio && \  
useradd -r -g kamailio kamailio && \  
mkdir -p /opt/kazoo/ /var/log/2600hz \  
/var/log/kamailio \  
/var/log/httpd  
  
RUN chown kazoo:daemon /opt/kazoo /var/log/2600hz -R && \  
chown kamailio:kamailio /var/log/kamailio -R  
  
RUN curl -o /etc/yum.repos.d/2600hz.repo http://repo.2600hz.com/2600hz.repo &&
\  
yum install -y epel-release && \  
yum clean all && \  
yum install -y kazoo-R15B kazoo-kamailio haproxy rsyslog && \  
yum install -y httpd kazoo-ui && \  
yum install -y curl supervisor && \  
chkconfig supervisord on  
  
VOLUME ["/var/log", "/opt/kazoo/log"]  
  
CMD ["/usr/bin/supervisord"]  

