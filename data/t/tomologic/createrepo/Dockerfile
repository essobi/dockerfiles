FROM centos:7  
RUN yum install -y createrepo && \  
yum clean all  
  
WORKDIR /root  
  
ENTRYPOINT [ "createrepo" ]  

