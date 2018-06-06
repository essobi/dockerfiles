FROM chenthilvel/fpm  
MAINTAINER ChenthilVel  
COPY mysql56-community.repo /etc/yum.repos.d/mysql56-community.repo  
RUN yum -y update && yum -y install gmp-devel mysql-community-devel && yum
clean all  
COPY strongswan build-rpm.sh postinstall postuninstall preuninstall /root/  
  
CMD ["/bin/bash", "/root/build-rpm.sh"]  

