FROM centos:centos7  
MAINTAINER Antoni Segura Puimedon <toni@midokura.com>  
  
RUN yum install -y http://ftp.rediris.es/mirror/fedora-epel/7/x86_64/e/epel-
release-7-5.noarch.rpm http://resources.ovirt.org/releases/ovirt-
release/ovirt-release35.rpm  
RUN yum update -y  
RUN yum install -y rpm-build git  
  
RUN git clone git://gerrit.ovirt.org/ovirt-engine.git  
  
RUN yum install -y autoconf \  
automake \  
java-devel \  
jpackage-utils \  
make \  
maven  
  
ADD scripts/build.sh /build.sh  
ENTRYPOINT ["/build.sh"]  

