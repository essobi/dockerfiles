FROM centos:latest  
MAINTAINER Maikel Dollé <maikel@itmagix.nl>  
  
RUN yum -y install epel-release wget git par2cmdline unrar openssl openssl-
devel python python-libs python-configobj python-pycurl python-pyudev python-
setuptools python-cheetah python-devel python-tools pyOpenSSL && \  
yum -y install p7zip python-pip && \  
yum -y groupinstall "Development Tools" && \  
yum -y install par2cmdline && \  
yum -y update && \  
rpm -Uvh
http://download1.rpmfusion.org/nonfree/el/updates/6/x86_64/unrar-4.0.7-1.el6.x86_64.rpm
&& \  
pip --no-cache-dir install cheetah requirements cryptography tzlocal && \  
wget http://www.golug.it/pub/yenc/yenc-0.4.0.tar.gz && \  
tar zxvf yenc-0.4.0.tar.gz && \  
cd yenc-0.4.0 && \  
python setup.py build && \  
python setup.py install  

