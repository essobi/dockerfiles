FROM centos:7  
MAINTAINER carcassi@umich.edu  
  
RUN rpm -Uvh https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm && \  
yum install -y yum-plugin-priorities && \  
rpm -Uvh https://repo.grid.iu.edu/osg/3.4/osg-3.4-el7-release-latest.rpm  
  
RUN yum clean all && \  
yum update -y && \  
yum install -y frontier-squid && \  
systemctl enable frontier-squid  
  
COPY app/ /app  
  
EXPOSE 3128  
CMD ["/app/entrypoint.sh"]  

