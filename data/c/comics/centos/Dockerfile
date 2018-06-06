FROM centos:latest  
MAINTAINER Ian Merrick <MerrickI@Cardiff.ac.uk>  
  
##############################################################  
# Dockerfile Version: 0.1  
# Software: -  
# Software Version: -  
# Software Website: -  
# Description: Base Centos7  
##############################################################  
  
RUN yum update -y ; \  
yum install -y epel-release ; \  
yum install -y ansible \  
git \  
gcc \  
gcc-c++ \  
make \  
net-tools \  
sudo \  
which ; \  
yum clean all ; \  
curl -o /usr/local/sbin/gosu -L
https://github.com/tianon/gosu/releases/download/1.9/gosu-amd64 ; \  
chmod 0755 /usr/local/sbin/gosu  
  
COPY user_entrypoint.sh /usr/local/bin/user_entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/user_entrypoint.sh"]  

