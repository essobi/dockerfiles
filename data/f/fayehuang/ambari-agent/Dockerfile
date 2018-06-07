FROM fayehuang/centos-serf  
MAINTAINER FayeHuang  
  
RUN wget -nv http://public-
repo-1.hortonworks.com/ambari/centos6/1.x/updates/1.7.0/ambari.repo -O
/etc/yum.repos.d/ambari.repo  
RUN yum install -y sudo tar wget java-1.7.0-openjdk ambari-agent && yum clean
all && yum clean dbcache  
  
# reslove yum Error:database disk image is malformed  
RUN rm -rf /var/cache/yum  
RUN mkdir -p /etc/yum.repos.d/bk  
RUN mv /etc/yum.repos.d/*.repo /etc/yum.repos.d/bk  
  
EXPOSE 22  
COPY ambari-agent_init.sh /root/ambari-agent_init.sh  
RUN chmod +x /root/ambari-agent_init.sh  
COPY supervisord.conf /etc/supervisord.conf  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

