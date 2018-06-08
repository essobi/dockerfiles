  
from dockerfile/java  
maintainer Soundmite  
  
run wget -O - http://debian.neo4j.org/neotechnology.gpg.key | apt-key add -  
run echo 'deb http://debian.neo4j.org/repo stable/' >
/etc/apt/sources.list.d/neo4j.list  
run apt-get update ; apt-get install neo4j -y  
  
run echo 'root soft nofile 40000' >> /etc/security/limits.conf  
run echo 'root hard nofile 40000' >> /etc/security/limits.conf  
  
run sed -i 's|# session required pam_limits.so|session required
pam_limits.so|g' /etc/pam.d/su  
  
add launch.sh /opt/  
run chmod +x /opt/launch.sh  
  
workdir /opt  
  
cmd ["/bin/bash", "-c", "/opt/launch.sh"]  
  
expose 7474  

