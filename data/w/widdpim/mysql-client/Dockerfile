FROM centos:7  
COPY mysql57-community.repo /etc/yum.repos.d/  
  
RUN yum makecache fast && \  
yum install -y mysql-community-client curl && \  
yum clean all && \  
rm -rf /var/cache/yum/*  
  
CMD ["bash"]  

