FROM centos:latest  
  
MAINTAINER tsgkadot <tsgkadot@gmail.com>  
  
# Accept licence for Silent installation  
ENV ACCEPT_EULA=Y  
  
RUN \  
curl https://packages.microsoft.com/config/rhel/7/prod.repo >
/etc/yum.repos.d/msprod.repo && \  
yum install -y mssql-tools && \  
yum clean all  

