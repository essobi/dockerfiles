FROM centos:6.8  
MAINTAINER Roman <sometime.developer@gmail.com>  
  
ADD sipxecs.repo /etc/yum.repos.d/  
RUN yum install -y yum-utils  
RUN yum install -y sipxtacklib sipxportlib unixODBC mongo-cxx-driver  
RUN yumdownloader sipxcommserverlib  
RUN cd /var/tmp  
  
RUN yumdownloader sipxregistry  
  
RUN rpm -i --nodeps ./*.rpm  
  
CMD /usr/bin/sipregistrar  

