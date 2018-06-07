FROM centos:7  
  
RUN set -x && \  
yum -y update && \  
yum -y upgrade && \  
yum -y install epel-release wget curl && \  
yum -y install p7zip p7zip-plugins && \  
yum -y install xterm httpd && \  
yum -y groupinstall "Development Tools"  

