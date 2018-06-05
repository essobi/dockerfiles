from centos:6.6  
#change timezone to Asia/Taipei  
RUN rm -f /etc/localtime && cp /usr/share/zoneinfo/Asia/Taipei /etc/localtime  
  
#install jdk1.7  
ADD ./install_jdk1.7.sh /tmp/install_jdk1.7.sh  
RUN chmod +x /tmp/install_jdk1.7.sh  
RUN /bin/bash -c "source /tmp/install_jdk1.7.sh"  
  
#add repository  
RUN curl public-
repo-1.hortonworks.com/ambari/centos6/2.x/updates/2.2.0.0/ambari.repo -o
/etc/yum.repos.d/ambari.repo  
  
RUN yum clean all  
  

