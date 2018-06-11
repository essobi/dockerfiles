FROM centos:7  
RUN yum -y install wget && \  
wget http://mirror.uv.es/mirror/fedora-epel//epel-release-latest-7.noarch.rpm
-O /tmp/epel-release-latest-7.noarch.rpm && \  
yum -y install /tmp/epel-release-latest-7.noarch.rpm  
  
RUN yum -y install git && \  
git clone https://github.com/egi-qc/umd-verification.git /tmp/umd-verification  
  
RUN yum -y install python-pip gcc python-devel python-ldap && \  
pip install fabric  
  
RUN cd /tmp/umd-verification && \  
pip install -r requirements.txt && \  
#fab ca:repository_url=http://repository.egi.eu/sw/production/cas/1/current/  
fab -l  

