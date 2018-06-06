# Basics  
#  
FROM griff/oracle-jdk7  
MAINTAINER Brian Olsen "brian@maven-group.org"  
# Install Crowd  
RUN wget -O /root/crowd.tar.gz
http://www.atlassian.com/software/crowd/downloads/binary/atlassian-
crowd-2.7.0.tar.gz  
run /usr/sbin/useradd --create-home --home-dir /usr/local/crowd --shell
/bin/bash crowd  
run mkdir -p /opt/crowd  
run tar zxf /root/crowd.tar.gz --strip=1 -C /opt/crowd  
run mkdir -p /opt/crowd-home  
run echo "crowd.home = /opt/crowd-home" > /opt/crowd/crowd-webapp/WEB-
INF/classes/crowd-init.properties  
  
ADD crowd.sh /opt/crowd.sh  
RUN chmod a+x /opt/crowd.sh  
  
# Launching Crowd  
workdir /opt/crowd  
expose 8095  
ENTRYPOINT ["/opt/crowd.sh"]  
CMD ["run"]  

