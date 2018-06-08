FROM sanjose/centos7  
MAINTAINER sanjose  
  
RUN curl https://packages.microsoft.com/config/rhel/7/prod.repo >
/etc/yum.repos.d/microsoft.repo  
RUN yum -y install powershell  
  
CMD ["powershell"]  

