FROM centos  
MAINTAINER Cheewai Lai <cheewai.lai@gmail.com>  
  
RUN yum -y update \  
&& yum -y install openssl pciutils wget \  
&& wget -O /tmp/pkg.tgz http://downloads.dell.com/FOLDER03240512M/1/OM-
MgmtStat-Dell-Web-LX-8.2.0-1739_A00.tar.gz \  
&& tar -C /tmp -xvf /tmp/pkg.tgz \  
&& cd /tmp/linux/rac/RHEL7/x86_64 \  
&& rpm -ivh *.rpm \  
&& ln -sf /usr/lib64/libssl.so.1.0.1e
/opt/dell/srvadmin/lib64/openmanage/private/libssl.so.0.9.8 \  
&& rm -rf /tmp/* \  
&& yum -y clean all  

