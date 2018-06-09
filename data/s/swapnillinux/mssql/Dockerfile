FROM centos:7  
MAINTAINER Swapnil Jain <swapnil@linux.com>  
LABEL description="Microsoft SQL (mssql) server on centos7"  
RUN yum -y install epel-release && rm -rf /var/cache/yum/* && yum clean all  
ADD mssql-server.repo /etc/yum.repos.d/mssql-server.repo  
RUN yum -y install sysvinit-tools sudo perl mssql-server && rm -rf
/var/cache/yum/* && yum clean all  
ENV SA_PASSWORD RedHat123  
RUN /opt/mssql/bin/sqlservr-setup --accept-eula --set-sa-password  
EXPOSE 1433  
CMD ["/opt/mssql/bin/sqlservr"]  

