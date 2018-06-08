# LICENSE GPL 2.0  
#  
#centos with tsinghua repo and update  
#centos with cloudera repo  
#also install procps-ng and net-tools  
FROM centos:latest  
  
MAINTAINER pilchard <ludundun@126.com>  
ENV TERM=xterm  
RUN echo "[cloudera-cdh5]" > /etc/yum.repos.d/cdh.repo && \  
echo "# Packages for Cloudera's Distribution for Hadoop, Version 5, on RedHat
or CentOS 7 x86_64" >> /etc/yum.repos.d/cdh.repo && \  
echo "name=Cloudera's Distribution for Hadoop, Version 5" >>
/etc/yum.repos.d/cdh.repo && \  
echo "baseurl=https://archive.cloudera.com/cdh5/redhat/7/x86_64/cdh/5/" >>
/etc/yum.repos.d/cdh.repo && \  
echo "gpgkey =https://archive.cloudera.com/cdh5/redhat/7/x86_64/cdh/RPM-GPG-
KEY-cloudera" >> /etc/yum.repos.d/cdh.repo && \  
echo "gpgcheck = 1" >> /etc/yum.repos.d/cdh.repo && \  
yum update -y && yum install -y procps-ng net-tools bind-utils iputils which
hostname && yum clean all  

