FROM centos:7  
MAINTAINER "Alin Voinea" <alin.voinea@eaudeweb.ro>  
  
RUN \  
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-CentOS-7 && \  
yum -y updateinfo && \  
yum -y install \  
yum-utils \  
epel-release \  
http://yumrepo.eea.europa.eu/centos/eea-release-1-0.1.noarch.rpm && \  
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EPEL-7 && \  
rpm --import /etc/pki/rpm-gpg/RPM-GPG-KEY-EEA && \  
yum clean all  
  
ADD install-dependencies.sh /bin/install-dependencies  
ADD *.yum /etc/yum/  
RUN install-dependencies /etc/yum/  
  
ONBUILD ADD . /opt/app  
ONBUILD RUN install-dependencies /opt/app  
  
#  
# Python 2.4  
#  
RUN \  
cd /tmp && \  
curl -o Python-2.4.6.tgz
https://www.python.org/ftp/python/2.4.6/Python-2.4.6.tgz && \  
tar -zxvf Python-2.4.6.tgz && \  
cd Python-2.4.6 && \  
./configure && \  
make && \  
make install && \  
rm -rf /tmp/Python*  
  
#  
# Python 2.6  
#  
RUN \  
cd /tmp && \  
curl -o Python-2.6.9.tgz
https://www.python.org/ftp/python/2.6.9/Python-2.6.9.tgz && \  
tar -zxvf Python-2.6.9.tgz && \  
cd Python-2.6.9 && \  
./configure && \  
make && \  
make install && \  
rm -rf /tmp/Python* && \  
mv /usr/local/bin/python /usr/local/bin/python-2.6 # Fix default python  
  
#  
# Start  
#  
CMD ["bash"]  

