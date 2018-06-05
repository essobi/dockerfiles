FROM sanjose/centos7  
MAINTAINER sanjose  
  
RUN yum install -y epel-release && \  
yum install -y python-pip && \  
pip install beautifulsoup4 && \  
pip install lxml && \  
yum update -y && \  
yum install -y python-qt4 && \  
yum install -y PyQt4-webkit && yum clean all  
  

