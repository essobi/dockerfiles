FROM centos:6  
MAINTAINER The U-TEST Team  
  
RUN yum install -y createrepo  
COPY createrepo.sh /createrepo.sh  
  
ENTRYPOINT ["/createrepo.sh"]  

