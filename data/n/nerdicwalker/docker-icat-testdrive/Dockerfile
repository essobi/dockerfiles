#FROM centos:7.3.1611  
FROM centos:centos7  
  
#LABEL name="CentOS iRODS Catalog Service Provider" \  
# build-date="20170724"  
# CMD [""]  
WORKDIR /tmp  
  
RUN yum install wget -y \  
&& yum install epel-release -y \  
&& wget -qO - https://packages.irods.org/renci-irods.yum.repo | tee
/etc/yum.repos.d/renci-irods.yum.repo \  
&& rpm --import https://packages.irods.org/irods-signing-key.asc \  
&& yum install python-psutil python-jsonschema irods-server -y  
  

