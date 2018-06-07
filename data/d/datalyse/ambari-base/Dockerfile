FROM centos:centos6  
MAINTAINER Filip Krikava "filip.krikava@inria.fr"  
RUN rpm -Uvh http://download.fedoraproject.org/pub/epel/6/x86_64/epel-
release-6-8.noarch.rpm  
  
ADD http://public-
repo-1.hortonworks.com/ambari/centos6/2.x/updates/2.0.1/ambari.repo
/etc/yum.repos.d/ambari.repo  
ADD http://public-repo-1.hortonworks.com/HDP/centos6/2.x/GA/2.2.0.0/hdp.repo
/etc/yum.repos.d/hdp.repo  
  
RUN echo "timeout=60" >> /etc/yum.conf  
  
RUN yum install -y \  
ntp \  
crudini \  
java-1.7.0-openjdk-devel  
  
# Fix preventing Ambari setup to continue due to a missing file  
RUN touch /etc/sysconfig/network  
  
ADD join.sh /join.sh  
RUN chmod +x /join.sh

