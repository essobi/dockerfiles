FROM fayehuang/centos-serf  
MAINTAINER FayeHuang  
  
RUN wget -nv http://public-
repo-1.hortonworks.com/ambari/centos6/1.x/updates/1.7.0/ambari.repo -O
/etc/yum.repos.d/ambari.repo  
  
# ambari-server install  
RUN yum install -y sudo tar wget java-1.7.0-openjdk ambari-server && yum clean
all && yum clean dbcache  
  
# ambari-server setup  
RUN ambari-server setup --silent  
  
# ambari & ssh service  
EXPOSE 8080 22  
COPY supervisord.conf /etc/supervisord.conf  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]  

