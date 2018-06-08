# DOCKER-VERSION 1.0.1  
FROM grange74/centos6-java6  
MAINTAINER sergeimuller  
  
#Update and install wget  
RUN yum -y update; yum clean all  
RUN yum install -y --enablerepo=centosplus libselinux-devel  
RUN yum install -y --enablerepo=centosplus httpd  
RUN yum install -y wget  
RUN yum install -y --enablerepo=centosplus epel-release  
RUN yum install -y zip  
  
#Enables Centos EPL repository, and then installs python modules.  
RUN yum -y install ipython  
RUN yum install -y python-psutil  
RUN yum install -y python-pycurl  
  
# Install utility for AEM  
ADD aemInstallAuthor.py /aem/author/aemInstaller.py  
ADD aemInstallPublisher.py /aem/publish/aemInstaller.py  

