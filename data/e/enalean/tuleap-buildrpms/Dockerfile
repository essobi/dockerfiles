FROM centos:7  
RUN yum install -y rpm-build \  
tar \  
util-linux \  
zip \  
make \  
libxslt &&\  
yum clean all  
  
COPY run.sh /run.sh  
  
VOLUME ["/rpms"]  
  
ENTRYPOINT ["/run.sh"]  

