FROM centos:7  
MAINTAINER Sergey Nartimov <just.lest@gmail.com>  
  
RUN yum install -y rpm-build rpm-sign redhat-rpm-config rpmdevtools createrepo
&& \  
yum clean all  
RUN echo '%_topdir /rpmbuild' > /root/.rpmmacros  
  
WORKDIR /rpmbuild  
  
ADD bin/build-spec /usr/local/bin/build-spec  

